#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random

print("Welcome to Dice Battle!")
print("You will roll 3 dice against a virtual oponent.")
print("Roll a higher total than your opponent to win!")

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
    print("\nYour Rolls:", user_roll) 
    print("Your total:", user_total)
    print("Previous Roll:", user_prev_roll)
    user_prev_roll.pop(0)
    user_prev_roll.append(user_roll)
    print("Previous scores:", user_scores)
    user_scores.append(user_total)
    if user_scores == ["NA", user_total]:
        user_scores.pop(0)

    print("\nOpponent's Rolls:", cpu_roll)
    print("Opponent's Total:", cpu_total)
    print("Previous Roll:", cpu_prev_roll)
    cpu_prev_roll.pop(0)
    cpu_prev_roll.append(cpu_roll)
    print("Previous scores:", cpu_scores)
    cpu_scores.append(cpu_total)
    if cpu_scores == ["NA", cpu_total]:
        cpu_scores.pop(0)

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




