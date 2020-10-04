import random


def pick_first_player():
    player_list = []
    while True:
        player = input("Enter a players name (leave blank to end)\n")
        if player == '':
            break
        player_list.append(player)
    fplayernumber = random.randint(0,len(player_list))
    print(f'{player_list[fplayernumber]} is the first player\n')