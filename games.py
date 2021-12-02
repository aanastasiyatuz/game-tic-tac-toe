from boxing import boxing
from game import Game

class TicTacToe(Game):
    board = [[0,0,0],[0,0,0],[0,0,0]]
    order = []
    positions = {
        "1":(0,0),
        "2":(0,1),
        "3":(0,2),
        "4":(1,0),
        "5":(1,1),
        "6":(1,2),
        "7":(2,0),
        "8":(2,1),
        "9":(2,2)
    }

    def accept_gamer(self, gamer):
        if len(self.gamers) == 2:
            self.order.append(gamer)
            return False
        if gamer in self.gamers:
            return False
        self.gamers.append(gamer)
        return True

    def remove_gamer(self, gamer):
        gs = self.gamers
        gamer.save_progress(self)
        gs.pop(gs.index(gamer))

    def is_available(self):
        if len(self.gamers) > 1:
            return True
        print(boxing("Sorry, there is no available gamers"))

    @staticmethod
    def _choose_sign(gamer1, gamer2):
        g1 = input(f"{gamer1.name} choose your sign:\n")
        while len(g1) > 1 or not len(g1):
            print("Choose a sign with one symbol")
            g1 = input(f"{gamer1.name} choose your sign:\n")
        
        g2 = input(f"{gamer2.name} choose your sign:\n")
        while len(g2) > 1 or not len(g2):
            print("Choose a sign with one symbol")
            g2 = input(f"{gamer2.name} choose your sign:\n")
        
        return g1, g2

    def _clean(self):
        self.board = [[0,0,0],[0,0,0],[0,0,0]]

    def _finish(self):
        for row in self.board:
            if 0 in row:
                return False
        return True

    def _win(self, gamer):
        b = self.board
        return (
            # ROWS
            (b[0][0] + b[0][1] + b[0][2] == gamer*3) or
            (b[1][0] + b[1][1] + b[1][2] == gamer*3) or
            (b[2][0] + b[2][1] + b[2][2] == gamer*3) or
            # COLUMNS
            (b[0][0] + b[1][0] + b[2][0] == gamer*3) or
            (b[0][1] + b[1][1] + b[2][1] == gamer*3) or
            (b[0][2] + b[1][2] + b[2][2] == gamer*3) or
            # DIAGONALS
            (b[0][0] + b[1][1] + b[2][2] == gamer*3) or
            (b[2][0] + b[1][1] + b[0][2] == gamer*3)
        )

    def _makemove(self, gamer, name):
        i, j = self.positions.get(input(f"{name} choose position on board:\n"), (3,3))
        while self._checkmove(i, j):
            print(self._checkmove(i,j))
            i, j = self.positions.get(input(f"{name} choose position on board:\n"), (3,3))
        self.board[i][j] = gamer

    def _checkmove(self, i, j):
        if i<0 or i>2 or j<0 or j>2:
            return "Invalid position!"
        if self.board[i][j] == "X" or self.board[i][j] == "O":
            return "Position occupied!"

    def display(self, s1="X", s2="O"):
        from functools import reduce
        res = ''
        b = self.board
        for i in [0,1,2]:
            for j in [0,1,2]:
                if b[i][j] == 1: res += s1
                elif b[i][j] == -1: res += s2
                else: res += reduce(lambda x,y:x if x[-1] == (i,j) else y,  self.positions.items())[0]
                if j<2: res += "|"
            if i<2: res += "\n-----\n"
        print(boxing(res))

    def _game(self):
        self._clean()
        gamer1, gamer2 = self.gamers
        g1, g2 = 1, -1
        self.display()
        self._makemove(g1, gamer1.name)
        self.display()
        while not self._finish() and not (self._win(g1) or self._win(g2)):
            self._makemove(g2, gamer2.name)
            self.display()
            if not self._win(g2):
                self._makemove(g1, gamer1.name)
                self.display()

        # ENDGAME
        self.show_rating()
        if self._win(g1):
            print(f"{gamer1.name} win!")
            gamer1.autosave(1, self)
        elif self._win(g2):
            print(f"{gamer2.name} win!")
            gamer2.autosave(1, self)
        if input(f"{gamer1.name}, do you want to play again? (y/n):\n").lower() != 'y':
            self.remove_gamer(gamer1)
            if self.order:
                self.gamers.append(self.order.pop(0))
        if input(f"{gamer2.name}, do you want to play again? (y/n):\n").lower() != 'y':
            self.remove_gamer(gamer2)   
            if self.order:
                self.gamers.append(self.order.pop(0))
        if self.is_available():
            self.play()

    def show_rating(self):  
        gamers = sorted(self.gamers+self.order, key=lambda x:x.rating(self), reverse=True)
        return super().show_rating(gamers)
