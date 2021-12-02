from games import TicTacToe
from user import User

basic = TicTacToe()

choice = input("Enter a name:\n").lower()
while choice != 'q':
    while not choice.strip():
        choice = input("Enter a valid name:\n").lower()
    if choice == 'q':
        continue
    new = User(choice)
    new.join(basic)
    choice = input("Enter a name:\n").lower()

basic.show_rating()
basic.play()