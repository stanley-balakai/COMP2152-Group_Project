import random

final_hero_health = 20 # Need this for the chest encounter code

def hero_attacks(combat_strength, monster_health, weapon_name):
    attack = random.randint(1, max(2, combat_strength))
    monster_health -= attack
    print(f"    |    Player's {weapon_name} ( {attack} ) ---> Monster (HP left: {max(monster_health, 0)} )")
    return max(monster_health, 0)

def monster_attacks(m_combat_strength, hero_health, attack_name):
    attack = random.randint(1, max(2, m_combat_strength))
    hero_health -= attack
    print(f"    |    {attack_name} ( {attack} ) ---> Player (HP left: {max(hero_health, 0)} )")
    return max(hero_health, 0)

def monster_encounter(base_strength, base_monster_strength):
    small_dice_options = list(range(1, 7))
    big_dice_options = list(range(1, 21))
    weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear Bomb"]
    loot_options = ["Health Potion", "Poison Potion", "Secret Note", "Leather Boots", "Flimsy Gloves"]
    belt = []

    input("    |    Roll the dice for your weapon (Press Enter)")
    weapon_roll = random.choice(small_dice_options)
    combat_strength = base_strength + weapon_roll
    weapon_name = weapons[weapon_roll - 1]
    print("    |    Your weapon is:", weapon_name)

    if weapon_roll <= 2:
        print("    |    --- You rolled a weak weapon, friend")
    elif weapon_roll <= 4:
        print("    |    --- Your weapon is meh")
    else:
        print("    |    --- Nice weapon, friend!")

    input("    |    Roll the dice for your health points (Press Enter)")
    hero_health = 15 + random.choice(big_dice_options)
    print("    |    You have", hero_health, "health points")
    print("    |    Combat strength:", combat_strength)
    print("    ------------------------------------------------------------------")

    print("    |    You find a loot bag! Rolling for items...")
    input("    |    Roll for first item (Press Enter)")
    belt.append(random.choice(loot_options))
    input("    |    Roll for second item (Press Enter)")
    belt.append(random.choice(loot_options))
    belt.sort()
    print("    |    Your belt: ", belt)

    for item in belt:
        if item == "Health Potion":
            hero_health += 5
            print("    |    You use a Health Potion! +5 HP")
        elif item == "Poison Potion":
            hero_health -= 2
            print("    |    Uh oh, Poison Potion! -2 HP")
        elif item == "Leather Boots":
            hero_health += 3
            print("    |    Your Leather Boots fit nicely. +3 HP")
        elif item == "Flimsy Gloves":
            hero_health += 1
            print("    |    You feel slightly protected by your Flimsy Gloves. +1 HP")
        elif item == "Secret Note":
            print("    |    You read a cryptic Secret Note... it does nothing.")

    hero_health = max(hero_health, 1)
    print("    |    Your final health after using loot: ", hero_health)

    monster_pool = ["Goblin", "Ogre", "Troll", "Drake Hatchling"]
    monsters = [random.choice(monster_pool) for _ in range(random.randint(1, 3))]
    print("    ------------------------------------------------------------------")
    print("    |    You meet the monster(s). FIGHT!!")
    print("Monsters encountered:", monsters)

    for monster in monsters:
        initial_health = random.randint(10, 20)
        monster_health = initial_health
        m_combat_strength = base_monster_strength + random.choice([0, 1, 2])
        ogre_rage = False
        dragon_recharging = False
        goblin_called_for_help = False
        hatchling_last_blast = False

        if monster == "Goblin":
            attack_name = "Goblin’s dagger swipe"
        elif monster == "Ogre":
            attack_name = "Ogre’s club smash"
        elif monster == "Troll":
            attack_name = "Troll’s crushing punch"
        elif monster == "Drake Hatchling":
            attack_name = "Hatchling’s bite"
        else:
            attack_name = "Monster's Claw"

        print(f"\nA {monster} appears with {monster_health} HP!")

        while monster_health > 0 and hero_health > 0:
            input("    |    Roll to see who strikes first (Press Enter)")
            attack_roll = random.randint(1, 6)

            if dragon_recharging:
                print("The Dragon is recharging and skips its turn!")
                dragon_recharging = False
            elif attack_roll % 2 != 0:
                input("    |    You strike (Press Enter)")
                monster_health = hero_attacks(combat_strength, monster_health, weapon_name)
                if monster_health <= 0:
                    break
                input(f"    |    The {monster} strikes back! (Press Enter)")
                hero_health = monster_attacks(m_combat_strength, hero_health, attack_name)
            else:
                input("    |    The monster strikes first! (Press Enter)")
                hero_health = monster_attacks(m_combat_strength, hero_health, attack_name)
                if hero_health <= 0:
                    break
                input("    |    Now you strike! (Press Enter)")
                monster_health = hero_attacks(combat_strength, monster_health, weapon_name)

            health_percentage = (monster_health / initial_health) * 100

            if monster == "Ogre" and health_percentage <= 50 and not ogre_rage:
                print("The Ogre enters a rage mode and permanently increases its attack power!")
                m_combat_strength += 2
                ogre_rage = True

            if monster == "Goblin" and not goblin_called_for_help and health_percentage <= 30:
                print("The Goblin is desperate! It calls for help...")
                goblin_called_for_help = True
                if random.random() < 0.3:
                    print("Another Goblin joins the fight!")
                    monsters.append("Goblin")
                else:
                    print("The Goblin's cries go unanswered...")

            if monster == "Drake Hatchling" and health_percentage <= 25 and not hatchling_last_blast:
                print("The Hatchling is enraged and musters all its strength into a Fire Blast!")
                if random.random() < 0.3:
                    print("The Drake Hatchling unleashes its Fire Blast, dealing massive damage!")
                    hero_health -= 10
                    print(f"You take 10 damage! Your HP: {max(hero_health, 0)}")
                else:
                    print("The Drake Hatchling charges up its Fire Blast but misses! It needs a turn to recover.")
                    dragon_recharging = True
                hatchling_last_blast = True
            elif monster == "Drake Hatchling":
                hatchling_last_blast = False

            if monster == "Troll" and health_percentage <= 50 and health_percentage > 30:
                print("The Troll regenerates its wounds, restoring some health!")
                monster_health += 3
                print(f"The Troll heals itself! Its HP is now {max(monster_health, 0)}")

            if monster == "Ogre" and ogre_rage:
                if random.random() < 0.3:
                    print("The Ogre, blinded by its rage, swings recklessly and misses!")
                else:
                    print("The enraged Ogre swings with all its might and hits you!")
                    hero_health = monster_attacks(m_combat_strength, hero_health, attack_name)
            else:
                print(f"The {monster} attacks normally.")

        if hero_health <= 0:
            print("You have been defeated...")
            return "hero_dead", combat_strength, hero_health, belt

        if monster == "Troll" and random.random() < 0.3 and (monster_health / initial_health) > 0.3:
            print("The Troll regenerates even more and recovers additional health!")
            monster_health += 2
        else:
            print(f"The {monster} has been defeated!")

    print("You have survived the monster encounters!")
    global final_hero_health
    final_hero_health = hero_health
    return "victory", combat_strength, hero_health, belt
