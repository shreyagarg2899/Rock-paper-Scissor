#use of random library
from random import randint
print("Welcome to Rock, Paper, Scissors Bot")
print("select from below items")

t = ["Rock", "Paper", "Scissors"]


computer = t[randint(0,2)]

player = input("Rock, Paper, Scissors?: ")
print("your choice is ",player)
print("Computer's choice is ",computer)
if player == computer:
    print("Tie!")
elif player == "Rock":
    if computer == "Paper":
        print("You lose!", computer, "covers", player)
    else:
        print("You win!", player, "smashes", computer)
elif player == "Paper":
    if computer == "Scissors":
        print("You lose!", computer, "cut", player)
    else:
        print("You win!", player, "covers", computer)
elif player == "Scissors":
    if computer == "Rock":
        print("You lose...", computer, "smashes", player)
    else:
        print("You win!", player, "cut", computer)
else:
    print("That's not a valid play. Check your spelling!")
