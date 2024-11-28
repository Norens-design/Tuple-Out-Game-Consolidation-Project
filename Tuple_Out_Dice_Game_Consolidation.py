# # # "Tuple Out" Dice Game Consolidation Project
 # # List of items to remember to incorporate in different lines
# ------------------------------------------------

# Create at least 2 fictional people. Have them meet for the game.
def greet(name):
  """This function is to introduce a player."""
  print("Hello, " + name + "Sophia! You will roll first.")

# Defining function is in a hiccup right now, 
# So this is another non-concatenated way to say "Hi" below...

print("Hello, Sophia! You will roll first.")

# Output: "Hello, Sophia! You will roll first."


def greet(name):
  """This function is to introduce a player."""
  print("Hello, " + name + "Fatima! You will roll after each of Sophia's turns.")

# Output: "Hello, Fatima! You will roll after each of Sophia's turns."

print("Hello, Fatima! You will roll after each of Sophia's turns.")

# Begin the game with Sophia's play first
print("Sophia's latest turn is now.")

dice_numbers = (1, 5, 2)
print(dice_numbers)
print("Keep playing. 8 points to start off.")

# Output: (1, 5, 2) 
# 
# Start Fatima's play next
print("Fatima's latest turn is now.")

dice_numbers = (3, 4, 1)
print(dice_numbers)
print("Keep playing. 8 points to start off.")

# Output: (3, 4, 1) 
#
# Start Sophia's play next
print("Sophia's latest turn is now.") 

dice_numbers = (1, 1, 4)
print(dice_numbers)
print("Fixed dice. -2 points (6 points for this turn). Must not re-roll a 1 next turn or else Sophia loses.")

# Output: (1, 1, 4)
#
# Start Fatima's play next
print("Fatima's latest turn is now.")

dice_numbers = (2, 5, 5)
print(dice_numbers)
print("Fixed dice. -2 points (10 points for this turn). Must not re-roll a 5 next turn or else Fatima loses.")

# Output: (2, 5, 5) 
#
# Start Sophia's play next
print("Sophia's latest turn is now.")

dice_numbers = (1, 1, 1)
print(dice_numbers)
print("Tupled out. 3 points for this turn have become 0 points. Sophia loses. Fatima wins.")

# Output: (1, 1, 1)
#
# Game complete.