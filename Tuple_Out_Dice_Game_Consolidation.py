# # # "Tuple Out" Dice Game Consolidation Project
# ------------------------------------------------

# PATT 6.1: used a "switch"-type `while:` loop to loop until a condition happens
# PATT 6.2: used `for:` loop over an iterable like a list, tuple, or dictionary
# PATT 6.3: changed or added results inside a loop (e.g., incrementing/updating a value, appending to a list)
# PATT 7.1: used a list where a list is appropriate & useful
# PATT 7.2: used indexing (by index or key) with a list, tuple, or dictionary
# ------------------------------------------------
# Fuse pandas into the program
import pandas as pd

# To demonstrate to real players, create at least 2 fictional people first. 
# Have them meet for the game.

name = "anything"
name_characters = "a,b,c,d,e..."
person_to_name = "examples"

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

# while less than five turns
#    continue prompting roll
# else: end_game

# Loop an end to the round with Sophia and Fatima 
# after the demo is finished one time.
# Game complete.

# Have a binary program for a coin flip to decide who goes first if you play. 
# It can be you and a friend coin tossing, you coin tossing to decide 
# if you go first or a computer game you can find. 

# A coin toss also comes in handy for other features. More on that soon.

coin_toss = "probabilistic"
coin_toss_number = (1,2)

if coin_toss_number is 1:
    print("You go first.")

else: 
    print("The other player goes first.")

# Flipped order is possible depending on which player' perspective is reading.
# Literally 2 sides of a coin ;)

if coin_toss_number is 2:
    print("The other player goes first.")

else: 
    print("You go first.")

# Have the user input their own names 
# everytime they run this program once 
# Sophia and Fatima have "played".

import random

player_name = input("Greetings. Please type your name.")
print("Welcome", name(player_name), sep = "")

play_time = input("Tell me the time zone and exact time you are playing in.")
print()

# Below are combinations to shuffle through later.
# Combinations of numbers were chosen over single digits
# to shorten roll process if combinations are pre-set.

dice_numbers[1] = (1-1-1, 2-2-2, 3-3-3, 4-4-4, 5-5-5)
dice_numbers[2] = (1-2-3, 1-2-4, 1-2-5, 1-3-4, 1-3-5)
dice_numbers[3] = (1-1-2, 1-1-3, 1-1-4, 1-1-5)
dice_numbers[4] = (2-2-1, 2-2-3, 2-2-4, 2-2-5)
dice_numbers[5] = (2-3-4, 2-3-5, 2-4-5, 3-4-5)
dice_numbers[6] = (3-3-1, 3-3-2, 3-3-4, 3-3-5)
dice_numbers[7] = (4-4-1, 4-4-2, 4-4-3, 4-4-5)
dice_numbers[8] = (5-5-1, 5-5-2, 5-5-3, 5-5-4)


random.shuffle(dice_numbers)
print(dice_numbers)

clock_timer = "minutes = [1]", "seconds = [2]"

counter = clock_timer[1] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)
clock_timer[2] = (10, 20, 30, 40, 50, 60)

for counter in range(16, 60):
    print(f"the counter variable is now {counter}")


# count_forward: 
# every_minute:

# while clock_timer[1] > 16: 
#     count_forward

# else: 
#     print()

import time

time.sleep() 
time.process_time()
time.localtime()
time.strftime()
time.strptime()