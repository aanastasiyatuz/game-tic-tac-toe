from animations import loading
from boxing import boxing
from abc import ABC

class Game(ABC):
    gamers = []

    def __str__(self):
        return self.__class__.__name__
    
    def accept_gamer(self, gamer):
        """You may change this method in your game"""
        if gamer in self.gamers:
            return False
        self.gamers.append(gamer)
        return True
    
    def display_gamers(self):
        gamers = "\n".join([boxing(gamer.name, margin=0, padding=0) for gamer in self.gamers])
        line = f"GAMERS IN {str(self).upper()}:" + f"\n{gamers}" + f"\nTOTAL: {len(self.gamers)} gamers"
        box = boxing(line, style="classic")
        print(box)

    def play(self):
        self.display_gamers()
        if not self.is_available(): return
        print(f"STARTING GAME {str(self).upper()}")
        loading(5)
        self._game()
    
    def _game(self):
        """Change this method in your game"""
        raise Exception("Change this method in your game")
    
    def is_available(self):
        """Change this method in your game"""
        raise Exception("Change this method in your game")

    def show_rating(self, gamers=None):
        gamers = gamers if gamers else sorted(self.gamers, key=lambda x:x.rating(self), reverse=True)
        res = ''
        for gamer in gamers:
            res += f"\n{gamer.name}: {gamer.rating()}"
        print(boxing(res))
