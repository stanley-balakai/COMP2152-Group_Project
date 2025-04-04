from baseLevel import Level
from monsterEncounter import monster_encounter
from treasureHunt import get_random_treasure


class ForestLevel(Level):
    def __init__(self, combat_strength, m_combat_strength):
        super().__init__(
            "Forest Level",
            ["Forest Path", "Hidden Grove", "Treasure Chest", "Monster", "Puzzle Wall"],
            {"Monster", "Puzzle Wall"}  # Critical objectives for this level
        )
        self.combat_strength = combat_strength
        self.m_combat_strength = m_combat_strength

    def explore_object(self, object_name):
        print(f"\nExploring {object_name}...")
        if object_name == "Hidden Grove":
            print("You found a hidden clue about the monsters!")
        elif object_name == "Treasure Chest":
            item = get_random_treasure()
            print("The chest contains " + item + "!")
            self.hero_inventory.append(item)
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
            print("A wild monster blocks your way! Before the fight, you check your gear...")
            # Starts Monster Encounter
            monster_encounter(self.combat_strength, self.m_combat_strength)

            self.level_objects.remove(object_name)
            self.required_objects.discard(object_name)

        else:
            print("Exploring this object does not reveal anything useful.")

        # Check if the level is complete
        self.check_completion()
