# # # "Tuple Out" Dice Game Consolidation Project
# ------------------------------------------------
# To make the game a little more real, place a timer
# on things starting in a few lines...

# To demonstrate to real players, have at 
# least 2 fictional people meet for the game.
name = "^"
person_to_name = "&"
name_characters = "a,b,c,d,e..."

# # Test previews of the demo naming function detailed below:
# greet("Hello, ... ) # error should not occur
# greet(Hello, ...[insert name] You will roll...[insert custom statements]") 
# greet("Hello,...", "^")
# greet("Hello,...", "&")


# """This function is to introduce a player."""
def greet(person_to_name, name_characters):
    name_length = len(person_to_name)
    personal_name = name_characters * name_length
  
    return personal_name


print("Hello,", person_to_name, "\nSophia! You will roll first.", name,
    sep = "\n")

print("Hello,", person_to_name, "\nFatima! You will roll after each of Sophia's turns.", name,
    sep = "\n")
# # """This function is to introduce a player."""
# def greet(person_to_name, name_characters):
#     name_length = len(person_to_name)
#     personal_name = name_characters * name_length
  
#     return personal_name

    


import time

t = 3 # 3 seconds
time.sleep(3)

# Begin the game with Sophia's play first
print("Sophia's latest turn is now.")

t = 3 # 3 seconds
time.sleep(3)

dice_numbers = (1, 5, 2)
print(dice_numbers)
print("Keep playing. 8 points to start off.")

t = 3 # 3 seconds
time.sleep(3)

# Start Fatima's play next
print("Fatima's latest turn is now.")

t = 3 # 3 seconds
time.sleep(3)

dice_numbers = (3, 4, 1)
print(dice_numbers)
print("Keep playing. 8 points to start off.")

t = 3 # 3 seconds
time.sleep(3)

# Start Sophia's play next
print("Sophia's latest turn is now.") 

t = 3 # 3 seconds
time.sleep(3)

dice_numbers = (1, 1, 4)
print(dice_numbers)
print("Fixed dice. -2 points (6 points for this turn)." 
      " Must not re-roll a 1 next turn or else Sophia loses.")

t = 3 # 3 seconds
time.sleep(3)

# Start Fatima's play next
print("Fatima's latest turn is now.")

t = 3 # 3 seconds
time.sleep(3)

dice_numbers = (2, 5, 5)
print(dice_numbers)
print("Fixed dice. -2 points (10 points for this turn)." 
      " Must not re-roll a 5 next turn or else Fatima loses.")


# Start Sophia's play next
print("Sophia's latest turn is now.")

t = 3 # 3 seconds
time.sleep(3)

dice_numbers = (1, 1, 1)
print(dice_numbers)
print("Tupled out. 3 points for this turn have become 0 points. Sophia loses. Fatima wins.")


# Loop an end to the round with Sophia and Fatima 
# after the demo is finished one time.
# Game complete.

# To demonstrate the scores as a data visual for your eyes, let's:

import pandas as pd  # type: ignore

df = pd.read_csv('Demo_Sophia_and_Fatima_Data.csv')
print(df)

demo_results = pd.read_csv("Demo_Sophia_and_Fatima_Data.csv")

type(demo_results)
demo_results.head()

demo_results.columns

demo_results = demo_results.rename(columns =
                        {'Demo player' : "demo player",
                         'Dice Game Players' : "players",
                         'Turn Order' : "turn order",
                         'Score Per Turn' : "score per turn",
                         'Number of Fixed Dice' : "fixed dice",
                         'Number of Tuples' : "tuples",
                         'Number of Safe Rolls' : "safe rolls",})


demo_results.head()
# Further breakdown of the example you saw 
# Future versions will do these for your scores too. Get excited.
max_score_per_turn = max(demo_results["avg score"])
min_score_per_turn = min(demo_results["avg score"])
demo_results["demo player"][demo_results["avg score"] == max_score_per_turn]
demo_results["demo player"][demo_results["avg score"] == min_score_per_turn]



# Okay. You get to try your turn now. Have a program for a coin flip 
# to decide who goes first if you play. 
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

# Flipped order is possible depending on which player' perspective is reading.
# # Literally 2 sides of a coin ;)

# Have the user input their own names 
# everytime they run this program once 
# Sophia and Fatima have "played".

player_name = input("Greetings. Please type your name.\n")

type(player_name) 

print("Welcome: ", player_name, ". You are now in the game! Just to let you know what" 
      " could happen...", sep ="")

# Below are combinations to shuffle through later.
# Combinations of numbers were chosen over single digits
# to shorten roll process if combinations are pre-set.


# Employ a mixed list below:

game_events = ["first_roll", "five", "fixed_dice", "last_roll", 1, "tuple_defeat", 2, 3, "tuple-less_victory"]
print(game_events)


dice_numbers = (1, 2, 3, 4, 5)

random.choices([1, 2, 3, 4, 5], k = 3)

random.shuffle(dice_numbers)
print(dice_numbers)

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

# Time to count the sand in the hourglass. It's been a long game!

clock_timer[2] = (10, 20, 30, 40, 50, 60)

import time

now = time.localtime()
type(now)
print(now)
now[0]
now[1]

time.process_time()

#Strftime first:
time.strftime("%m/%d/%y", now)
time.strftime("%B %d, %Y", now)
time.strftime("%b %d, %Y", now)
time.strftime("%Y-%m-%d %H:%M:%S", now)

# Strptime as part of the dice roll game to keep track
# Almost like a live semi 'countdown' in a chess (ahem,) dice match
time.strptime("December 17, 2024, 9:58 PM", "%B %d, %Y, %I:%M:%S %p")
time = input("Type the time you are playing in here to confirm the previous line.")
time.strptime("December 20, 2024, 6:23 PM", "%B %d, %Y, %I:%M:%S %p")
time = input("Type the time you are playing in here to confirm the previous line.")

my_playtime = time.strptime()