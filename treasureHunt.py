import random

def create_grid():
    # create a 9x9 grid with empty spaces
    grid = [[' ' for _ in range(9)] for _ in range(9)]
    
    # define possible items for the grid
    items = ['O', 'C', 'T', ' ']  # O for Open treasure, C for Closed treasure, T for Trap, ' ' for empty
    

    # randomly place items on the grid
    grid = [[random.choice(items) for _ in range(9)] for _ in range(9)]
    return grid



def display_grid(grid):
    # print column numbers
    print("    |    1  2  3  4  5  6  7  8  9")
    print("    |    -------------------------")
    


    # print rows with letters
    for i in range(9):
        row_letter = chr(65 + i)  # Convert 0-8 to A-I
        print(f"    | {row_letter} | {'  '.join(grid[i])}")



def get_valid_input():
    while True:
        choice = input("    |    Would you like to go on a treasure hunt? (Y/N): ").upper()
        if choice in ['Y', 'N']:
            return choice
        print("    |    Invalid input. Please enter Y or N.")




def get_valid_coordinates():
    while True:
        try:
            coords = input("    |    Enter coordinates (e.g., 2B): ").upper()
            if len(coords) != 2:
                print("    |    Invalid format. Please enter in the format '2B'")
                continue
            
            col = int(coords[0])
            row = ord(coords[1]) - ord('A')
            
            if 1 <= col <= 9 and 0 <= row <= 8:
                return row, col - 1
            else:
                print("    |    Coordinates out of range. Please enter valid coordinates.")
        except ValueError:
            print("    |    Invalid input. Please enter in the format '2B'")



def get_random_treasure():
    treasures = [
        "Ancient Scroll",
        "Golden Coin",
        "Magic Potion",
        "Diamond Ring",
        "Enchanted Sword",
        "Mysterious Map"
    ]
    return random.choice(treasures)



def play_treasure_hunt():
    # ask if user wants to play
    choice = get_valid_input()
    if choice == 'N':
        return


    # create and display the grid
    grid = create_grid()
    print("\n    |    Welcome to the Treasure Hunt!")
    print("    |    Find treasures but beware of traps!")
    print("    |    O = Open Treasure, C = Closed Treasure, T = Trap")
    print("    |    Enter coordinates to search (e.g., 2B)")
    print("\n")
    display_grid([['?' for _ in range(9)] for _ in range(9)])  # Show empty grid to player
    
    while True:
        row, col = get_valid_coordinates()
        cell = grid[row][col]
        
        if cell == 'O':
            treasure = get_random_treasure()
            print(f"    |    Congratulations! You found an open treasure chest!")
            print(f"    |    Inside you found: {treasure}")
        elif cell == 'C':
            print("    |    Oh no! This chest is locked. Better luck next time!")
        elif cell == 'T':
            print("    |    TRAP! You've triggered a trap!")
            print("    |    Game Over!")
            return
        else:
            print("    |    Nothing here...")
        
        # ask if player wants to continue
        while True:
            continue_choice = input("    |    Would you like to search another spot? (Y/N): ").upper()
            if continue_choice in ['Y', 'N']:
                break
            print("    |    Invalid input. Please enter Y or N.")
        
        if continue_choice == 'N':
            print("    |    Thanks for playing!")
            return
