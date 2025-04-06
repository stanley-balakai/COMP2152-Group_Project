import random

class Chest:
    def __init__(self, chest_type, loot=None, trap=None):
        self.chest_type = chest_type  # chest types being normal, trapped, or mimic
        self.loot = loot              # loot for normal or trapped chests
        self.trap = trap              # trap only for the trapped chests
        self.opened = False

    def open(self, player_stats):
        if self.opened:
            print("This chest has already been opened.")
            return
        self.opened = True

        print(f"Opening a {self.chest_type} chest...")

        if self.chest_type == "trapped":
            if self.trap:
                if self.trap == "poison":
                    print("    |    It's a trap! Poison gas leaks out. -2 HP")
                    player_stats['health'] -= 2
                elif self.trap == "bomb":
                    print("    |    BOOM! A bomb explodes! -5 HP")
                    player_stats['health'] -= 5
                elif self.trap == "cursed":
                    print("    |    A dark curse weakens you. -3 HP")
                    player_stats['health'] -= 3
                else:
                    print("    |    You triggered something... but nothing happened?")
            else:
                print("    |    You hear a click... but nothing went off.")

            if self.loot == "gold":
                gold_found = random.randint(10, 100)
                print(f"    |    You still find {gold_found} gold!")
                player_stats['gold'] += gold_found
            elif self.loot == "health potion":
                print("    |    You find a Health Potion! Use it or keep it?")
                choice = input("Use now (U) or Keep (K)? ").upper()
                if choice == "U":
                    print("    |    You use the potion. +5 HP")
                    player_stats['health'] += 5
                else:
                    print("    |    You store the potion.")
                    player_stats['inventory'].append("Health Potion")
            elif self.loot == "enchanted sword":
                print("    |    You found an Enchanted Sword! +2 damage")
                player_stats['strength'] += 2
            else:
                print("    |    The chest is otherwise empty.")

        elif self.chest_type == "normal":
            if self.loot == "gold":
                gold_found = random.randint(10, 100)
                print(f"    |    You found {gold_found} gold!")
                player_stats['gold'] += gold_found
            elif self.loot == "health potion":
                print("    |    You found a Health Potion! Use it or keep it?")
                choice = input("Use now (U) or Keep (K)? ").upper()
                if choice == "U":
                    print("    |    You use the potion. +5 HP")
                    player_stats['health'] += 5
                else:
                    print("    |    You store the potion.")
                    player_stats['inventory'].append("Health Potion")
            elif self.loot == "enchanted sword":
                print("    |    You found an Enchanted Sword! +2 damage")
                player_stats['strength'] += 2
            else:
                print("    |    You open the chest... but it's empty.")

        else:
            print("    |    OH NO! It's a Mimic! You must fight it!")
            mimic_hp = 10
            while mimic_hp > 0 and player_stats['health'] > 0:
                input("    |    Press Enter to attack the Mimic...")
                hit = random.randint(2, player_stats['strength'])
                mimic_hp -= hit
                print(f"    |    You attack the mimic for {hit} damage. Mimic HP: {max(mimic_hp, 0)}")
                if mimic_hp <= 0:
                    print("    |    You defeated the Mimic!")
                    break

                input("    |    Press Enter for the Mimic's turn...")
                mimic_hit = random.randint(1, 4)
                player_stats['health'] -= mimic_hit
                print(f"    |    Mimic bites you for {mimic_hit} damage. Your HP: {max(player_stats['health'], 0)}")

            if player_stats['health'] <= 0:
                print("    |    You were defeated by the Mimic...")

def generate_chests(num_chests=5):
    chest_types = ["normal", "trapped", "mimic"]
    loots = ["gold", "health potion", "enchanted sword"]
    traps = ["poison", "bomb", "cursed"]

    chests = [
        Chest(
            chest_type=random.choice(chest_types),
            loot=random.choice(loots) if random.choice(chest_types) != "mimic" else None,
            trap=random.choice(traps) if random.choice(chest_types) == "trapped" else None
        )
        for _ in range(num_chests)
    ]
    return chests