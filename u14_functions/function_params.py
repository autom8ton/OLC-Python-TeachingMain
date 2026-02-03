
def print_quest_header(quest_name, reward):
    # 2 parameters
    print("***** QUEST BOARD NOTICE *****")
    print(f"Quest: {quest_name}")
    print(f"Reward: {reward}")
    print("="*50)  # separator (or use a function)


def print_quest_details(location, danger_level):
    print(f"Location: {location}")
    print(f"Danger Level: {danger_level}")

    # define danger level advice
    if danger_level.lower() == "low":
        print("Advice: Beginner-friendly. Bring snacks and confidence. ")
    elif danger_level.lower() == "medium":
        print("Advice: Stay alert. Travel in pairs. ")
    elif danger_level.lower() == "high":
        print("Advice: Risky mission. Prepare well and plan an escape route. ")
    else:
        print("Advice: Unknown danger. Ask the Guild Master for info. ")

    print("*-"*25)  # separator (or use a function)
    print()  # separator (or use a function)


def show_quest_board(quest_name, reward, location, danger_level):
    print_quest_header(quest_name, reward)# Call first function
    print_quest_details(location, danger_level) # Call second function

# --- Demo calls (students can change these) ---
show_quest_board("Rescue the Lost Owlbear", "120 gold", "Whispering Forest", "medium")
show_quest_board("Defeat the Cave Slime King", "Rare Gem", "Dark Caverns", "high")