# generate random integer values
from random import choice
from random import randint

import random
import time

rps=["R","P","S"]
game_choice=["Rock","Paper","Scissors"]


print("Let's play Rock Paper Scissors Game Ready....")
print("Rock")
print("Paper")
print("Scissors")
print("GO..")

while True:
    your_choice=input("Enter your choice: ") 
    computer_chioce=random.choice(game_choice)       
    if your_choice =="Rock".lower()or your_choice=="Paper".lower() or your_choice=="Scissors".lower():
        print("Player",your_choice, end="") 
        print(": Cpu",computer_chioce)
        if your_choice == computer_chioce:
            print("It is a tie")
            continue
        elif your_choice == "Rock".lower()and computer_chioce == "Scissors":
            print("You Win")
            break
        elif your_choice == "Paper".lower() and computer_chioce == "Rock":
            print("You Win")
            break
        elif your_choice == "Scissors".lower() and computer_chioce == "Paper":
            print("You Win")
            break
        elif your_choice == "Scissors".lower() and computer_chioce == "Rock":
            print("Computer Wins")
            break
        elif your_choice == "Rock".lower() and computer_chioce == "Paper":
            print("Computer Wins")
            break
        elif your_choice == "Paper".lower() and computer_chioce == "Scissors":
            print("Computer Wins")
            break
        
            

    else:
        print('Try Again!!')    




