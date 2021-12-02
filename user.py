import json

class User:
    __users = []
    games = []

    def __init__(self, name):
        self.name = name.title()
        while self.name in User.__users:
            print("User with same name is already exists!")
            self.name = input("Enter new name:\n").title()
        User.__users.append(self.name)

    def join(self, game):
        confirm = input(f"Do you want to join game {game}? (y/n)").lower()
        if confirm == 'y':
            self._join(game)

    def _join(self, game):
        if game.accept_gamer(self):
            self.games.append(game)
            print(f"Successfully joined to game {game}!")
            return
        print(f"You are in order! Please wait")

    # PROGRESS
    def get_unsaved_progress(self, game):
        with open("unsaved_progress.json") as file:
            if not file.read():
                return 0
            file.seek(0)
            progresses = json.load(file)
        if progresses.get(self.name):
            if progresses.get(self.name).get(str(game)):
                return progresses.get(self.name).get(str(game))
        return 0
    
    def discard_unsaved_progress(self, game):
        with open("unsaved_progress.json") as file:
            if not file.read():
                return
            file.seek(0)
            progresses = json.load(file)
            if not progresses.get(self.name):
                return
            if not progresses.get(self.name).get(str(game)):
                return
            progresses.get(self.name).pop(str(game))
        with open("unsaved_progress.json", "w") as file:
            json.dump(progresses, file)
    
    def _save_to_progress(self, progress, game):
        with open("progress.json") as file:
            if not file.read():
                with open("progress.json", "w") as file:
                    json.dump({self.name:{str(game):progress}}, file)
                return
            file.seek(0)
            progresses = json.load(file)
            if progresses.get(self.name):
                last_progress = progresses[self.name].get(str(game))
                if last_progress:
                    progresses[self.name][str(game)] = last_progress + progress
                else:
                    progresses[self.name][str(game)] = progress
            else:
                progresses[self.name] = {str(game):progress}
        with open("progress.json", "w") as file:
            json.dump(progresses, file)

    def save_progress(self, game, progress=None):
        confirm = input("Save progress? (y/n): ").lower()
        if confirm == 'n':
            self.discard_unsaved_progress(game)
            return
        u_progress = self.get_unsaved_progress(game)
        if u_progress:
            self.discard_unsaved_progress(game)
            self._save_to_progress(u_progress, game)
        if progress:
            self._save_to_progress(progress, game)

    def autosave(self, progress, game):
        with open("unsaved_progress.json") as file:
            read = file.read()
            if not read:
                with open("unsaved_progress.json", "w") as file:
                    json.dump({self.name:{str(game):progress}}, file)
                return
            file.seek(0)
            progresses = json.load(file)
            if progresses.get(self.name):
                last_progress = progresses[self.name].get(str(game))
                if last_progress:
                    progresses[self.name][str(game)] = last_progress + progress
                else:
                    progresses[self.name][str(game)] = progress
            else:
                progresses[self.name] = {str(game):progress}
        with open("unsaved_progress.json", "w") as file:
            json.dump(progresses, file)

    def progress(self, game):
        with open("progress.json") as file:
            if not file.read():
                return 0
            file.seek(0)
            progresses = json.load(file)
        if progresses.get(self.name):
            if progresses.get(self.name).get(str(game)):
                return progresses.get(self.name).get(str(game))
        return 0

    @property
    def progresses(self):
        with open("progress.json") as file:
            if not file.read():
                return {}
            file.seek(0)
            progresses = json.load(file)
        if progresses.get(self.name):
            return progresses.get(self.name)
        return {}

    def rating(self, game=None):
        progresses = self.progresses
        if not progresses:
            return 0.0
        if not game:
            from functools import reduce
            return reduce(lambda x,y: x+y, [float(i) for i in progresses.values()])
        return float(progresses.get(str(game)))
