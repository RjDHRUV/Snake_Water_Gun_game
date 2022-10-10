#Snake , Water or Gun game.

import random 
# importing random module 
def winner(computer,a):
    # When both you and computer chooses the same
    if computer==a:
        return None
    # check for all possibility when computer chooses Water
    elif computer=='w':
        if a=='s':
            return True
        elif a=='g':
            return False
     # check for all possibility when computer chooses Gun
    elif computer=='g':
        if a=='w':
            return True
        elif a=='s':
            return False
     # check for all possibility when computer chooses Snake
    elif computer=='s':
        if a=='g':
            return True
        elif a=='w':
            return False
    # checks for entered charachter other s,w,g
    else:
        return -1
# using (randint) method to generate random numbers
rno=random.randint(1,3)
if rno ==1:
    computer='s'
elif rno ==2:
    computer='g'
elif rno==3:
    computer='w'
# Name of Player
name =input("What is your good name : ")
# Choice of Player
a=input("Your turn : Snake(s)  Water(w)  Gun(g) : ")
# Returns the Winner
b=winner(computer,a)
# prints choice of player and computer
print(f"Computer choose {computer}")
print(f"Computer choose {a}")
# Dispaly output according to choice
if b==None:
    print("Game is a tie!")
elif b:
    print(f"{name} ,You are the Winner !")
else:
    print(f"Sorry {name},You lose the game!")

