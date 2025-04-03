from baseLevel import Level


class CaveLevel(Level):
    def __init__(self):
        super().__init__(
            "Cave Level",
            ["Dark Tunnel", "Puzzle Wall", "Monster", "Hidden Passage", "Treasure Chest"],
            {"Puzzle Wall", "Monster", "Hidden Passage"}  # Critical objectives for this level
        )

    def explore_object(self, object_name):
        print(f"\nExploring {object_name}...")
        if object_name == "Dark Tunnel":
            print("You navigate the tunnel and find faint markings that hint at a puzzle solution of images water fire earth.")
            # Optional exploration
        elif object_name == "Treasure Chest":
            print("You found a Rusty Key in the chest!")
            self.hero_inventory.append("Rusty Key")
            self.level_objects.remove(object_name)  # Optional object
        elif object_name == "Hidden Passage":
            if "Puzzle Key" in self.hero_inventory:
                print("You clear the rubble with the Puzzle Key and access the Hidden Passage!")
                self.level_objects.remove(object_name)  # Remove the Hidden Passage once accessed
                self.required_objects.discard(object_name)  # Mark as completed if it's critical
            else:
                print("The passage is blocked by rubble. You need a Puzzle Key to clear it.")
        elif object_name == "Puzzle Wall":
            puzzle_input = input("Solve the puzzle (Enter the sequence 'water-fire-earth'): ")
            if puzzle_input == "water-fire-earth":
                print("The wall crumbles, clearing the passage!")
                self.level_objects.remove(object_name)
                self.required_objects.discard(object_name)  # Mark the puzzle as completed
            else:
                print("The sequence is wrong. The wall remains intact.")
        elif object_name == "Monster":
            print("A cave-dwelling monster awaits! Engage in combat to move forward.")
            #Start Monster Combat

            self.level_objects.remove(object_name)
            self.required_objects.discard(object_name)  # Mark the monster as completed
        else:
            print("Nothing interesting happens here.")

        # Check if the level is complete
        self.check_completion()
