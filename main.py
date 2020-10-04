from GameOps import *

while True:
    choice = input("""What would you like to do?
    1. Play a game
    2. Add a game
    3. Remove a game
    4. List games
    5. Reset the list
    6. Quit""")
    if choice == 1:
        play_a_game()
    elif choice == 2:
        name = input("Enter the name of the game")
        minPlay = input("Enter the minimum number of players")
        maxPlay = input("Enter the maximum number of players")
        difficulty = input("Enter the difficulty (1-4)")
        add_game(name,minPlay,maxPlay,difficulty)
    elif choice == 3:
        name = input("Which game would you like to remove?")
        remove_game(name)
    elif choice == 4:
        print("This function has not been implemented yet")
    elif choice == 5:
        confirm = input('Are you completely sure? Type "Yes" to continue')
        if confirm == 'Yes':
            reset_list()
    elif choice == 6:
        print("Bye for now!")
        break