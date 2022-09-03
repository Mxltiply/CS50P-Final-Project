import time
import random


board: list[str] = [
    '-','-','-',
    '-','-','-',
    '-','-','-'
]


PLAYER: str = "X"
COMPUTER: str = "O"
turn: str = ""

class PlayerError(Exception):
    pass


def main():
    """This is the main play function of Tic-Tac-Toe; it hosts the game."""
    global PLAYER
    global COMPUTER
    global turn
    global board
    
    print("Welcome to Tic Tac Toe! Let's play!")
    print_board(board)
    
    choice: str = input("Please choose X or O: ").strip().upper()
    if choice == "X":
        PLAYER = "X"
        COMPUTER = "O"
    elif choice == "O":
        PLAYER = "O"
        COMPUTER = "X"
    else:
        raise PlayerError("Invalid choice!")
    
    turn = PLAYER
    # Main Game Loop
    while True:
        play_turn(turn, board)
        
        winner = validate_win(board)
        tie = validate_tie(board)
        if winner:
            print(f"{winner} is the winner!!!")
            break
        if tie:
            print("Tie game!")
            break        
          
def print_board(board):
    """Prints the board to the terminal with formatting"""
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])
    print('\n')


def change_turn():
    """Changes the player's turn"""
    global PLAYER
    global COMPUTER
    global turn
    
    if turn == PLAYER:
        turn = COMPUTER
    else:
        turn = PLAYER
    
def play_turn(turn, board):
    """Handles the player's turn and computer's turn"""
    if turn == PLAYER:
        print(f"{PLAYER}'s turn")
           
        valid: bool = False
        
        while not valid: 
            pos: str = input("Choose from 1-9: ") 
             
            if not pos.isnumeric():
                print("Invalid input")
                continue
                
            pos = int(pos) - 1
            if pos not in range(0, 9):
                print("Invalid input")
            elif board[pos] != "-":
                print("That spot already has a marker!")
            else:
                board[pos] = PLAYER
                valid = True      
    else:
        print(f"{COMPUTER}'s turn")
        time.sleep(1)     
        makeComputerMove(board)

    print_board(board)
    change_turn()

def makeComputerMove(board):
    """Attempts to find the best calculated position for the AI to go"""
    global COMPUTER
    

    # begin the minimax algorithm in the maximizing stage (the computer wants to win/draw)
    bestScore: int = -1000000
    bestMove: int = 0

    for i in range(9):
        if board[i] == "-":
            board[i] = COMPUTER
            score = minimax(board, 0, False)
            board[i] = "-"

            if score > bestScore:
                bestScore = score
                bestMove = i

    board[bestMove] = COMPUTER
    return bestMove

def minimax(board, depth, isMaximizing):
    """Implements the minimax (a type of adversarial search) algorithm"""

    global COMPUTER
    global PLAYER
    
    # represents the win, loss, and tie values
    scores = {
        COMPUTER: 1,
        PLAYER: -1,
        "tie": 0
    }

    result = validate_win(board) or validate_tie(board)
    
    # if the board state passed in matches the terminal case (a win, loss, or tie)
    # simply return that value
    if result is not None:
        return scores[result]

    # otherwise, start building the tree

    # if it's the computers turn (attempting to maximize any opportunity to win/draw the game)
    if isMaximizing:
        bestScore = -1000000

        for i in range(9):
            if board[i] == "-":
                # check for an empty space, try putting the computer's marker there; extend the recursive tree
                # to the next level (minimizing)
                board[i] = COMPUTER
                bestScore = max(bestScore, minimax(board, depth + 1, not isMaximizing))

                board[i] = "-"

        # return the highest score for that specific level within the tree        
        return bestScore
    else:
        # if it's the player's turn (attempting to minimize any loss)
        bestScore = 1000000

        for i in range(9):
            if board[i] == "-":
                # check for an empty space, try putting the player's marker there; extend the recursive tree
                # to the next level (maximizing)
                board[i] = PLAYER
                bestScore = min(bestScore, minimax(board, depth + 1, not isMaximizing))

                board[i] = "-"

        # return the lowest score for that specific level within the tree 
        return bestScore
    

def validate_win(board):
    """Validates the winner; it checks the rows, columns, and diagonals."""
    row_winner = row_checker(board)
    column_winner = column_checker(board)
    diagonal_winner = diagonal_checker(board)

    # if any of the row/column/diagonal return something (x or o) then declare the winner / else nothing
    if row_winner:
        return row_winner
    elif column_winner:
        return column_winner
    elif diagonal_winner:
        return diagonal_winner
    else:
        return None

def row_checker(board):
    """Checks the rows for a winner"""
    row1 = board[0] == board[1] == board[2] and board[0] != '-'
    row2 = board[3] == board[4] == board[5] and board[3] != '-'
    row3 = board[6] == board[7] == board[8] and board[6] != '-'
    
    if row1:
        return board[0] # X or O
    if row2:
        return board[3] # X or O
    if row3:
        return board[6] # X or O

def column_checker(board):
    """Checks the columns for a winner"""
    column1 = board[0] == board[3] == board[6] and board[0] != '-'
    column2 = board[1] == board[4] == board[7] and board[1] != '-'
    column3 = board[2] == board[5] == board[8] and board[2] != '-'

    if column1:
        return board[0] # X or O
    if column2:
        return board[1] # X or O
    if column3:
        return board[2] # X or O

def diagonal_checker(board):
    """Checks the diagonals for a winner"""
    diagonal1 = board[0] == board[4] == board[8] and board[0] != '-'
    diagonal2 = board[2] == board[4] == board[6] and board[2] != '-'

    if diagonal1:
        return board[0] # X or O
    if diagonal2:
        return board[2] # X or O

def validate_tie(board):
    """Checks if there is a tie or not"""
    if "-" not in board:
        return "tie"
    else:
        return None
    
    
if __name__ == '__main__':
    """Main script runner"""
    main()