#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random

print("Welcome to Dice Battle!")
print("You will roll 3 dice against a virtual oponent.")
print("Roll a higher total than your opponent to win!")

def display_results(rolls, total, prev_rolls, scores): #used a funtion to prevent lengthy coding
    print("your rolls: " ,rolls)
    print("your Total: ", total)
    print("Previous Roll: ", prev_rolls)
    prev_rolls.pop(0) # takes away the value for previous rolls 
    prev_rolls.append(rolls) #adds the current rolls to a value for previous rolls 
    print("Previous Scores: ",  scores)
    scores.append(total) #adds the value for total to scores 
    if scores == ["NA", total]:
        scores.pop(0) #removes the value for scores when it has "NA"

def dice_roll():
    return random.randint(1,6)

user_scores = ["NA"]
cpu_scores = ["NA"]
user_prev_roll = ["NA"]
cpu_prev_roll = ["NA"]
wins = 0
losses = 0
ties = 0

while True:
    user_roll = [dice_roll(), dice_roll(), dice_roll()]
    cpu_roll = [dice_roll(), dice_roll(), dice_roll()]
    user_total = sum(user_roll)
    cpu_total = sum(cpu_roll)
    
    input("\nPress Enter to Roll...")
    display_results( user_roll, user_total, user_prev_roll, user_scores) # makes for a cleaner body

    print("\nOpponent's Rolls:", cpu_roll)
    print("Opponent's Total:", cpu_total)
    display_results( cpu_roll, cpu_total, cpu_prev_roll, cpu_scores)

    if user_total > cpu_total:
        print("\nYou Win!")
        wins += 1
    elif user_total < cpu_total:
        print("\nYou Lost! Better Luck Next Time :(")
        losses += 1
    else:
        print("\nIt's A Draw!")
        ties += 1
    
    play_again = input("\nPlay Again? (yes/no): ")
    if play_again != "yes":
        print("\nThanks for playing!")
        break
    
print("Wins:", wins, "Losses:", losses, "Ties:", ties)
print("Your Scores:", user_scores)
print("Oponnent scores:", cpu_scores)


# In[ ]:




