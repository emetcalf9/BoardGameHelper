from GameOps import *
from PlayerOps import *
from os import path

if path.exists('BGList') == 0:
    create_default_list()

while True:
    choice = input("""What would you like to do?
    1. Play a game
    2. Add a game
    3. Remove a game
    4. List games
    5. Reset the list
    6. Pick a first player
    7. Quit\n""")
    if int(choice) == 1:
        play_a_game()
    elif int(choice) == 2:
        name = input("Enter the name of the game:\n")
        minPlay = input("Enter the minimum number of players:\n")
        maxPlay = input("Enter the maximum number of players:\n")
        difficulty = input("Enter the difficulty (1-4):\n")
        add_game(name, minPlay, maxPlay, difficulty)
    elif int(choice) == 3:
        name = input("Which game would you like to remove?\n")
        remove_game(name)
    elif int(choice) == 4:
        list_all_games()
    elif int(choice) == 5:
        confirm = input('Are you completely sure? Type "Yes" to continue\n')
        if confirm == 'Yes':
            reset_list()
    elif int(choice) == 6:
        pick_first_player()
    elif int(choice) == 7:
        print("Bye for now!")
        break
