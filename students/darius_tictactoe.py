import random
import time

# Create Board using a nested list of 3 x 3
def initboard():
    board = []
    for i in range(3):
        row = []
        for j in range(3):
            row.append(" ")
        board.append(row)
    return board
    # print(board)


#print the board onto the screen
def printboard(argboard):
    count = 1
    for row in argboard:
        for cell in row:
            if cell == " ":
                print(f"| {count} ", end = "")
            else:
                print(f"| {cell} ", end = "")

            if count % 3 ==0:
                print(f"|")
                print("-"*13)
            count +=1

def getplayermove(argboard, argplayer):
    # get the player move ->> this will go into a function later
    while True:
        move = input(f"Player {argplayer}, Enter a number from 1 - 9: ")
        if move.isdigit():
            move = int(move) 
            if move >= 1 and move <= 9:
                move = move - 1 #reset back to zero based index

                # calculate the position of the move
                row = move // 3
                col = move % 3
                
                if argboard[row][col] == " ": # check if position already filled
                    argboard[row][col] = argplayer
                    break
                else:
                    print(f"Position {move + 1 } is already taken")
            else:
                print("You must enter a number that is from 1 to 9.")
        else:
            print("Enter a number. Try again.")        
    # print(f"row: {row} col: {col}")
    # printboard(board)
    return argboard

def check_win(argboard):
    win_conditions = [
        # Horizontal
        [argboard[0][0],argboard[0][1],argboard[0][2]],
        [argboard[1][0],argboard[1][1],argboard[1][2]],
        [argboard[2][0],argboard[2][1],argboard[2][2]],
        #Vertical
        [argboard[0][0],argboard[1][0],argboard[2][0]],
        [argboard[0][1],argboard[1][1],argboard[2][1]],
        [argboard[0][2],argboard[1][2],argboard[2][2]],
        # Diagonal
        [argboard[0][0],argboard[1][1],argboard[2][2]],
        [argboard[2][0],argboard[1][1],argboard[0][2]]
    ]

    for condition in win_conditions:
        if condition[0] == condition[1] == condition[2] and condition[0] != " ":
            return True
    return False

def is_draw(argboard):
    for row in argboard:
        if " " in row:
            return False
    return True

def getcurrentplayer(player):
    if player == "X":
        player = "Q"
    else:
        player = "X"
    return player


def getaimove(argboard, argplayer):
    print(f"Computer ({argplayer}) is thinking...")
    time.sleep(1)

    # Step 1: Try to win
    for i in range(3):
        for j in range(3):
            if argboard[i][j] == " ":
                argboard[i][j] = argplayer # simulate a move
                if check_win(argboard):
                    return # check if computer is going to win.
                else:
                    argboard[i][j] = " "  # undo the move

    # Step 2: Try to block player if player is going to win
    opponent = "X"
    if argplayer == "X":
        opponent = "Q"
    for i in range(3):
        for j in range(3):
            if argboard[i][j] == " ":
                argboard[i][j] = opponent
                if check_win(argboard):
                    argboard[i][j] = argplayer
                    return
                else:
                    argboard[i][j] = " "

    # Step 3: Take center if available
    if argboard[1][1] == " ":
        argboard[1][1] = argplayer
        return

    # Step 4: Take a corner if available
    corners = [[0,0], [0,2], [2,0], [2,2]]
    random.shuffle(corners) # randomize to choose a random corner
    for i, j in corners:
        if argboard[i][j] == " ":
            argboard[i][j] = argplayer
            return

    # Step 5: Take any available move
    for i in range(3):
        for j in range(3):
            if argboard[i][j] == " ":
                argboard[i][j] = argplayer
                return


# run the code
board = initboard()
current_player = ""

while True:
    current_player = getcurrentplayer(current_player)
    printboard(board)
    print()

    #getplayermove(board, current_player)
    if current_player == "X":
        getplayermove(board, current_player)
    else:
        getaimove(board, current_player)

    if check_win(board):
        print(f"Winner is {current_player}")
        print()
        printboard(board)
        break
    elif is_draw(board):
        print("It's a draw!")
        print()
        printboard(board)
        break