# Make a rock-paper-scissors game where it is the player vs the computer.
# The computer’s answer will be randomly generated, while the program will ask the user for their input.

import random

flag = True


def rock_paper_scissor(play):
    comp = random.randint(1, 3)
    if comp == 1:
        print("Computer selected rock")
    elif comp == 2:
        print("Computer selected paper")
    else:
        print("Computer selected scissor")
    if play == comp:
        print("that's a TIE")
    elif (play == 1 and comp == 3) or (play == 2 and comp == 1) or (play == 3 and comp == 2):
        print("YOU WON")
    else:
        print("YOU ARE A LOSER;) \n better luck next time")


while flag:
    print("Instructions...blah blah")
    player = int(input("please enter 1 for rock \n 2 for paper \n 3 for scissor"))
    rock_paper_scissor(player)
    put = input("Press Y to play again\n press N to quit")
    if put == "Y":
        flag = True
    else:
        print("Will see you next time BYE")
        flag = False
