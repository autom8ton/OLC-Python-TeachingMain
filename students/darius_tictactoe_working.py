
def init_board():
    board = [] # hold the entire board

    for j in range(3):
        row = [] # empty row
        for i in range(3):
            row.append(' ') # add 3  empty spaces   
        
        board.append(row) # add this row to the board

    return board

# this function prints out the board
def print_board(arg_board):
    count = 1
    
    print("-" * 13)
    for row in arg_board:
        for cell in row:
            if cell == " ":
                print(f"| {count} ", end="")
            else:
                print(f"| {cell} ", end="") # if there is value print the value

            # go to the next line 
            if count % 3 == 0:
                print("|") 
                print("-" * 13)

            count += 1

def get_player_move():
    while True:
        num_choice = input("Enter a number (1 - 9): ")

        if num_choice.isdigit():
            num_choice = int(num_choice)

            if num_choice >= 1 and num_choice <= 9:
                
                # calculate the position
                num_choice = num_choice - 1 # normalise to zero
                row = num_choice // 3 # return the row number
                col = num_choice % 3 # return the col number

                # update the board coordinates
                board[row][col] = "X"
                break
            else:
                print("Number must be between 1 to 9.")
        else:
            print("You must enter a valid number.")

#####################
# start of main code
board = init_board() # return the board to board variable

print_board(board)

# test 
while True:
    get_player_move()
    print_board(board)
