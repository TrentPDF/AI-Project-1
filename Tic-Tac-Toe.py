import random


board = [[' ' for _ in range(3)] for _ in range(3)]

for row in board:
    print(row)

def player():
    while True:
        print("Rows: 1, 2, 3\nColumns: 1, 2, 3")
        row, col = map(int, input("Enter row and column (1-3): ").split())
        cell_value = board[row - 1][col - 1]

        if cell_value == 'X' or cell_value == 'O':
            print("Spot already filled. Pick again.")
            print("Rows: 1, 2, 3\nColumns: 1, 2, 3")
            row, col = map(int, input("Enter row and column (1-3): ").split())
            cell_value = board[row][col]
        else:
            board[row - 1][col - 1] = 'X'
            break
    
def ai():
    # Checks for Winning Move
    for row, col in get_empty_spots(board):
        board[row][col] = 'O'
        if check_winner(board, 'O'):
            return
        board[row][col] = ' '

    # Checks for Block
    for row, col in get_empty_spots(board):
        board[row][col] = 'X'
        if check_winner(board, 'X'):
            board[row][col] = 'O'
            return
        board[row][col] = ' '

    # Take Center if available
    if board[1][1] == ' ':
        board[1][1] = 'O'
        return
    
    # Take Side if nothing else possible
    for row, col in [(0,1), (1,0), (1,2), (2,1)]:
        if board[row][col] == ' ':
            board[row][col] = 'O'
            return

def has_open_spaces(board):
    for row in board:
        if ' ' in row:
            return True
    return False

def get_empty_spots(board):
    empty_spots = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                empty_spots.append((row, col))
    return empty_spots

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
        
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
        
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    
    return False

def game():
    currentPlayer = 'Player'
    while has_open_spaces(board) and not check_winner(board, 'X') and not check_winner(board, 'O'):
        if currentPlayer == 'Player':
            for row in board:
                print(row)
            player()
            currentPlayer = 'AI'
            if not has_open_spaces(board):
                break
        else:
            ai()
            currentPlayer = 'Player'
    if check_winner(board, 'X'):
        print("Player has won!")
        for row in board:
            print(row)
    elif check_winner(board, 'O'):
        print("AI has won!")
        for row in board:
            print(row)
    else:
        print("It's a tie.")

game()
