
import random
print(" WELCOME TO ROCK, PAPER SCISSORS GAME")
print("R for rock")
print("P for paper")
print("S for scissors")

choices = ["R", "P", "S"]
player = input("What is your choice?  R, P or S?: ")

while True:   

        if player  not in choices:
            print("Not a valid choice TRY AGAIN")
            player = input("What is your choice?  R, P or S?: ")
            continue

        CPU = random.choice(choices)
        print("Player: ", player)
        print("CPU: ", CPU)

        if player == CPU:
            print("It is a tie! PLAY AGAIN")
            player = input("What is your choice? R,  P or S?: ")
            continue


        elif player == "R":
            if CPU == "S":
                print("Player: rock  CPU: scissors")
                print("Rock beats Scissors! You are the winner! GAME OVER")
            else:
                print("Player: rock  CPU: scissors")
                print("Paper beats Rock! CPU is the winner! GAME OVER")
        elif player == "P":
            if CPU == "R":
                print("Player: paper  CPU: rock")
                print("Paper best Rock! You are the winner! GAME OVER")
            else:
                print("Player: paper  CPU: rock")
                print("Scissors beats Paper! CPU is the winner! GAME OVER")
        elif player == "S":
            if CPU == "P":
                print("Player: scissors  CPU: paper")
                print("Scissors beats Paper! You are the winner! GAME OVER")
            else:
                print("Player: scissors  CPU: paper")
                print("Rock beats Scissors! CPU is the winner! GAME OVER")
            
        if player in choices:
            break

        
