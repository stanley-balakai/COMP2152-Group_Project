from baseLevel import Level


class ForestLevel(Level):
    def __init__(self):
        super().__init__(
            "Forest Level",
            ["Forest Path", "Hidden Grove", "Treasure Chest", "Monster", "Puzzle Wall"],
            {"Monster", "Puzzle Wall"}  # Critical objectives for this level
        )

    def explore_object(self, object_name):
        print(f"\nExploring {object_name}...")
        if object_name == "Hidden Grove":
            print("You found a hidden clue about the monsters!")
        elif object_name == "Treasure Chest":
            print("The chest contains a Healing Potion!")
            self.hero_inventory.append("Healing Potion")
            self.level_objects.remove(object_name)  # Optional object, no impact on required_objects
        elif object_name == "Puzzle Wall":
            puzzle_input = input("Solve the puzzle (Enter the sequence 'fire-water-earth'): ")
            if puzzle_input == "fire-water-earth":
                print("The wall slides open, revealing a hidden path!")
                self.level_objects.remove(object_name)
                self.required_objects.discard(object_name)  # Mark the puzzle as completed
            else:
                print("Incorrect sequence. Try again.")
        elif object_name == "Monster":
            print("A wild monster blocks your way! You defeated it.")
            # Start Monster Combat

            self.level_objects.remove(object_name)
            self.required_objects.discard(object_name)  # Mark the monster as completed
        else:
            print("Exploring this object does not reveal anything useful.")

        # Check if the level is complete
        self.check_completion()
