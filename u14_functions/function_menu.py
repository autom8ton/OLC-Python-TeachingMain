# =========================================
# GAME / PROGRAM WELCOME PAGE (FUNCTIONS)
# =========================================

def print_title():
    # Students can copy/paste this ASCII art.
    print("""
  ██████╗  ██████╗ ██████╗ ███████╗ ██████╗ ██╗   ██╗███████╗███████╗████████╗
 ██╔════╝ ██╔═══██╗██╔══██╗██╔════╝██╔═══██╗██║   ██║██╔════╝██╔════╝╚══██╔══╝
 ██║      ██║   ██║██║  ██║█████╗  ██║   ██║██║   ██║█████╗  ███████╗   ██║   
 ██║      ██║   ██║██║  ██║██╔══╝  ██║▄▄ ██║██║   ██║██╔══╝  ╚════██║   ██║   
 ╚██████╗ ╚██████╔╝██████╔╝███████╗╚██████╔╝╚██████╔╝███████╗███████║   ██║   
  ╚═════╝  ╚═════╝ ╚═════╝ ╚══════╝ ╚══▀▀═╝  ╚═════╝ ╚══════╝╚══════╝   ╚═╝   
    """)
    print("Welcome, adventurer!")
    print("This is a mini text game where you choose what to do next.")

def draw_separator():
    print("=" * 45)   

def print_rules():
    print("Rules:")
    print("1) Type the number of your choice and press Enter.")
    print("2) Read carefully — some choices may end the game.")
    print("3) Have fun and don't panic if you make a mistake!")

def show_menu():
    print("Menu:")
    print("1) Start Game")
    print("2) Instructions")
    print("3) Quit")

def game_intro():
    print_title()
    draw_separator()
    print_rules()
    draw_separator()
    show_menu()
    draw_separator()

# Run the welcome page
game_intro()
