# # # "Tuple Out" Dice Game Consolidation Project
# ------------------------------------------------
# Fuse pandas into the program

# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# To demonstrate to real players, have at 
# least 2 fictional people meet for the game.
name = "^"
person_to_name = "&"
name_characters = "a,b,c,d,e..."

# """This function is to introduce a player."""
def greet(person_to_name, name_characters):
    name_length = len(person_to_name)
    personal_name = name_characters * name_length
  
    return personal_name

    
print("Hello,", person_to_name, "\nSophia! You will roll first.", name,
    sep = "\n")


# """This function is to introduce a player."""
def greet(person_to_name, name_characters):
    name_length = len(person_to_name)
    personal_name = name_characters * name_length
  
    return personal_name

    
print("Hello,", person_to_name, "\nFatima! You will roll after each of Sophia's turns.", name,
    sep = "\n")


# Begin the game with Sophia's play first
print("Sophia's latest turn is now.")

dice_numbers = (1, 5, 2)
print(dice_numbers)
print("Keep playing. 8 points to start off.")

# Start Fatima's play next
print("Fatima's latest turn is now.")

dice_numbers = (3, 4, 1)
print(dice_numbers)
print("Keep playing. 8 points to start off.")

# Start Sophia's play next
print("Sophia's latest turn is now.") 

dice_numbers = (1, 1, 4)
print(dice_numbers)
print("Fixed dice. -2 points (6 points for this turn). Must not re-roll a 1 next turn or else Sophia loses.")

# Start Fatima's play next
print("Fatima's latest turn is now.")

dice_numbers = (2, 5, 5)
print(dice_numbers)
print("Fixed dice. -2 points (10 points for this turn). Must not re-roll a 5 next turn or else Fatima loses.")


# Start Sophia's play next
print("Sophia's latest turn is now.")

dice_numbers = (1, 1, 1)
print(dice_numbers)
print("Tupled out. 3 points for this turn have become 0 points. Sophia loses. Fatima wins.")

# Loop an end to the round with Sophia and Fatima 
# after the demo is finished one time.
# Game complete.

# Have a binary program for a coin flip to decide who goes first if you play. 
# It can be you and a friend coin tossing, you coin tossing to decide 
# if you go first or a computer game you can find. 

# A coin toss also comes in handy for other features. More on that soon.

print("That was a demo. Now, to you, the person watching...")

import random

coin_toss = "probabilistic"
coin_toss_number = [1,2, "heads", "tails"]

random.choices([1, 2], k = 4)

random.shuffle(coin_toss_number)
print(coin_toss_number)

counter = 1
counter = 2
while counter == 1:
    if coin_toss_number == 1:
        print(f"{counter}Heads. You go first.")
        continue
    print(f"{counter}Tails. The other player goes first.")
    counter += 1

while counter == 2:
    if coin_toss_number == 2:
        print(f"{counter}Tails. The other player goes first.")
        continue
    print(f"{counter}Heads. You go first.")
    counter += 2

# counter = 2
# while counter == 2:
#     if coin_toss_number == 2:
#         print(f"{counter}Tails. The other player goes first.")

#     else:
#         print("Heads. You go first.")

# Flipped order is possible depending on which player' perspective is reading.
# # Literally 2 sides of a coin ;)

# Have the user input their own names 
# everytime they run this program once 
# Sophia and Fatima have "played".

player_name = input("Greetings. Please type your name.\n")

type(player_name) 

print("Welcome: ", player_name, ". You are now in the game!", sep ="")

# Below are combinations to shuffle through later.
# Combinations of numbers were chosen over single digits
# to shorten roll process if combinations are pre-set.


# Employ a mixed list below:

game_events = ["first_roll", "five", "fixed_dice", "last_roll", 1, "tuple_defeat", 2, 3, "tuple-less_victory"]

dice_numbers = (1, 2, 3, 4, 5)

random.choices([1, 2, 3, 4, 5], k = 3)

random.shuffle(dice_numbers)
print(dice_numbers)

import time

numbers = input("How many numbers should I print out?")
print("processing")
numbers = int(numbers)

print("starting the loop now")
for num in range(numbers):
    print(f"here's the number {num}")

clock_timer = ("minutes = [1]", "seconds = [2]")

counter = clock_timer[1] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,...)

for counter in range(16, 60):
    print(f"the counter variable is now {counter}")

clock_timer[2] = (10, 20, 30, 40, 50, 60)

now = time.localtime()
type(now)
print(now)
now[0]
now[1]

time.process_time()
time.strftime()
time.strptime("December 17, 2024, 9:58:58 PM", "%B %d, %Y, %I:%M:%S %p")