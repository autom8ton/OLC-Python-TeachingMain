import random

# 1) Returns a random integer from 1 to sides
def roll_dice(sides):
    return random.randint(1, sides)

# 2) Returns the final damage number
def calculate_damage(attack_roll):
    weapon_bonus = random.randint(1, 5)

    # Convert the roll into a simple base damage number
    damage = attack_roll + weapon_bonus

    # Critical hit rule (example): 18, 19, 20 are critical
    if attack_roll >= 18:
        damage = damage * 2

    return damage

# 3) Returns new HP after damage (minimum 0)
def apply_damage(current_hp, damage):
    new_hp = current_hp - damage
    if new_hp < 0:
        new_hp = 0
    return new_hp


# 4) Returns gold reward based on danger level
def calculate_reward(base_gold, danger_level):
    level = danger_level.lower()

    if level == "low":
        multiplier = 1.0
    elif level == "medium":
        multiplier = 1.5
    elif level == "high":
        multiplier = 2.0
    else:
        multiplier = 1.2  # fallback

    return int(base_gold * multiplier)


# 5) Returns a message string based on battle outcome
def get_battle_message(monster_name, monster_hp, gold_reward):
    if monster_hp == 0:
        print(f"{monster_name} defeated! You earned {gold_reward} gold. ")
    else:
        print(f"{monster_name} is still standing with {monster_hp} HP... keep fighting! ")


# --------------------------------
# Copy+Paste >> One-turn Boss Fight Demo
# The below code is given to you. Code the functions to make it work!
# --------------------------------

monster_name = "Cave Slime King"
monster_hp = 25
danger_level = "medium"
reward = 100

print("=== BOSS FIGHT ===")
print(f"Enemy: {monster_name}")
print(f"Monster HP (start): {monster_hp}")

# # Uncomment once function 1 roll_dice is done
# attack_roll = roll_dice(20)
# print(f"Attack roll: {attack_roll}")

# # Uncomment once function 2 calculate_damage is done
# damage = calculate_damage(attack_roll)
# print(f"Damage dealt: {damage}")

# # Uncomment once function 3 apply_damage is done
# monster_hp = apply_damage(monster_hp, damage)
# print(f"Monster HP (after): {monster_hp}")

# # Uncomment once function 4 calculate_reward is done
# gold_reward = calculate_reward(reward, danger_level)

# # Uncomment once function 5 get_battle_message is done
# get_battle_message(monster_name, monster_hp, gold_reward)
# print("=== END OF TURN ===")