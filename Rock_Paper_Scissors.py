"""

Rock, paper, scissors

"""

import pyinputplus as pyip
from random import choice as rnd

player_points = 0
comp_points = 0
tie = 0

while True:
    choice = pyip.inputMenu(['Rock', 'Paper', 'Scissors', 'Quit'], numbered=True)
    comp_choice = rnd(['Rock', 'Paper', 'Scissors'])

    if choice == 'Quit':
        break

    elif choice == comp_choice:
        tie += 1
        print(f'It is a tie!\nScore: (Player: {player_points} Computer: {comp_points} Tie: {tie})\n')

    elif choice == 'Rock' and comp_choice == 'Paper' or \
            choice == 'Paper' and comp_choice == 'Scissors' or \
            choice == 'Scissors' and comp_choice == 'Rock':

        comp_points += 1
        print(f'Player: {choice}\nComputer: {comp_choice}\nPlayer LOSS!\nScore: Player {player_points}'
              f' Computer {comp_points} Tie {tie}\n')

    else:
        player_points += 1
        print(f'Player: {choice}\nComputer: {comp_choice}\nPlayer WINS!\nScore: Player {player_points}'
              f' Computer {comp_points} Tie {tie}\n')
