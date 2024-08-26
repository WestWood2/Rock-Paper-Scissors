import random
import time

# Game Loop 
def LoopGame():
    time.sleep(0.5)
    print("===============================================")
    print("So this how you start.")
    print("-The other player will display it rock:paper:scissors")
    print(" ")
    print("-you enter rock:paper:scissors to counter the game hand")
    print(" ")
    print("-There will be tree turn. To win the game you need to win all 3 game or more than the other player.")
    print(" ")
    print("-If both palyer have matching pair it will contnue until one side win")
    print("===============================================")
    time.sleep(3)
    print("How to counter")
    print("-rock beat scissors / scissors beat paper / paper beat rock")
    print(" ")
    time.sleep(2)
    win = 0
    lose = 0
    tie = 0
    Turn = 0
    while Turn != 3:
        #list of str and choice random str from the list
        RPS_list = ['rock','paper','scissors']
        R_RPS = random.choice(RPS_list)
        
        time.sleep(1.5)
        print("-------------------------------")
        print("please enter (rock, paper, scissors):")
        User_RPS = input()
        print("-------------------------------")
        
        time.sleep(0.5)
        print(f"You chose {User_RPS}, computer chose {R_RPS}.")
        print(" ")
        
        if User_RPS == R_RPS:
            time.sleep(2)
            print(f"Both players selected {User_RPS}. It's a tie!")
            tie += 1
        elif User_RPS == "rock":
            if R_RPS == "scissors":
                time.sleep(2)
                print("Rock smashes scissors! You win!")
                win += 1
                Turn += 1
            else:
                time.sleep(2)
                print("Paper covers rock! You lose.")
                lose += 1
                Turn += 1
        elif User_RPS == "paper":
            if R_RPS == "rock":
                time.sleep(2)
                print("Paper covers rock! You win!")
                win += 1
                Turn += 1
            else:
                time.sleep(2)
                print("scissors cuts paper! You lose.")
                lose += 1
                Turn += 1
        elif User_RPS == "scissors":
            if R_RPS == "paper":
                time.sleep(2)
                print("scissors cuts paper! You win!")
                win += 1
                Turn += 1
            else:
                time.sleep(2)
                print("Rock smashes scissors! You lose.")
                lose += 1
                Turn += 1
        else:
            print("You can only enter (rock, paper, scissors):")

    print("==============================")            
    print(f"< Win = {win} > < Lost = {lose} > < Tie = {tie} >")
    if win > lose:
        print(" ")
        print("your a Winner")
    else:
        print(" ")
        print("You have Lost")


Game_Start = " "
print("This is a Rock/Paper/Scissors")
print("To Start enter 's' to start")
while Game_Start != 's':
    Game_Start = input()
    if Game_Start == 's':
        LoopGame()
    else:
       print("please enter 's' to start")
       
