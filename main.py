# Import the random library to use for the dice later
import random

# Put all the functions into another file and import them
import functions
import treasureHunt
from caveLevel import CaveLevel
from forestLevel import ForestLevel

# Define two Dice
small_dice_options = list(range(1, 7))
big_dice_options = list(range(1, 21))

# Define the Weapons
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear Bomb"]

# Define the Loot
loot_options = ["Health Potion", "Poison Potion", "Secret Note", "Leather Boots", "Flimsy Gloves"]
belt = []

# Define the Monster's Powers
monster_powers = {
    "Fire Magic": 2,
    "Freeze Time": 4,
    "Super Hearing": 6
}

# Define the number of stars to award the player
num_stars = 0

# Loop to get valid input for Hero and Monster's Combat Strength
i = 0
input_invalid = True

while input_invalid and i in range(5):
    print("    ------------------------------------------------------------------")
    print("    |", end="    ")
    combat_strength = input("Enter your combat Strength (1-6): ")
    print("    |", end="    ")
    m_combat_strength = input("Enter the monster's combat Strength (1-6): ")

    # Validate input: Check if the string inputted is numeric
    if (not combat_strength.isnumeric()) or (not m_combat_strength.isnumeric()):
        # If one of the inputs are invalid, print error message and halt
        print("    |    One or more invalid inputs. Player needs to enter integer numbers for Combat Strength    |")
        i = i + 1
        continue

    # Note: Now safe to cast combat_strength to integer
    # Validate input: Check if the string inputted
    elif (int(combat_strength) not in range(1, 7)) or (int(m_combat_strength)) not in range(1, 7):
        print("    |    Enter a valid integer between 1 and 6 only")
        i = i + 1
        continue

    else:
        input_invalid = False
# Converts the user input from string to int
        combat_strength = int(combat_strength)
        m_combat_strength = int(m_combat_strength)
        break

# Allow the player to interact
# Choose a level to play
current_level_name = input("Choose your level: Forest or Cave? ").strip().lower()


if current_level_name == "forest":
    # Pass the base combat strength and monster strength into the level
    # so the monster encounter has access to them when triggered.
    level = ForestLevel(combat_strength, m_combat_strength)
elif current_level_name == "cave":
    level = CaveLevel(combat_strength, m_combat_strength)
else:
    print("Invalid level. Starting in the Forest by default.")
    level = ForestLevel(combat_strength, m_combat_strength)

# Start navigating the level
level.display_paths(int(combat_strength))  # Dynamically display paths based on hero stats

quit = False
while not level.completed:
    object_to_explore = input("\nWhat would you like to do? (Type 'exit' to leave the level): ")
    if object_to_explore.lower() == "exit":
        print(f"You have chosen to exit {level.name}.")
        quit = True
        break  # Exit the loop and return to the main menu or a preparation phase
    else:
        level.explore_object(object_to_explore)
        level.display_paths(int(combat_strength))  # Update paths after interactions

if quit == False:
    print("\nYou have successfully navigated the level and completed it!")


if not input_invalid:
    input_invalid = False

    # Collect Loot
    print("    ------------------------------------------------------------------")
    print("    |    !!You find a loot bag!! You look inside to find 2 items:")
    print("    |", end="    ")
    input("Roll for first item (enter)")

    # Collect Loot First time
    loot_options, belt = functions.collect_loot(loot_options, belt)
    print("    ------------------------------------------------------------------")
    print("    |", end="    ")
    input("Roll for second item (Press enter)")

    # Collect Loot Second time
    loot_options, belt = functions.collect_loot(loot_options, belt)

    print("    |    You're super neat, so you organize your belt alphabetically:")
    belt.sort()
    print("    |    Your belt: ", belt)

    treasureHunt.play_treasure_hunt()



