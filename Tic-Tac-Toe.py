import random


board = [[' ' for _ in range(3)] for _ in range(3)]


def player():
    while True:
        try:
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
        except ValueError:
            print("Invalid input. Please enter two numbers separated by a space.")
    
def ai(board):
    bestScore = float('-inf')
    bestMove = None

    # Checks for Winning Move
    for row, col in get_empty_spots(board):
        board[row][col] = 'O'
        score = aiLogic(board, 0, False, maxDepth=4)
        board[row][col] = ' '

        if score > bestScore:
            bestScore = score
            bestMove = (row, col)

    if bestMove:
        row, col = bestMove
        board[row][col] = 'O'


def eval_board(board):
    if check_winner(board, 'O'):
        return 10
    if check_winner(board, 'X'):
        return -10
    else:
        return 0


def aiLogic(board, depth, maximizing, maxDepth):
    if check_winner(board, 'O'):
        return 10 - depth
    if check_winner(board, 'X'):
        return -10 + depth
    if not get_empty_spots(board):
        return 1
    if depth >= maxDepth:
        return eval_board(board)

    if maximizing:
        bestScore = float('-inf')
        for row, col in get_empty_spots(board):
            board[row][col] = 'O'
            score = aiLogic(board, depth + 1, False, maxDepth)
            board[row][col] = ' '
            bestScore = max(bestScore, score)
        return bestScore
    else:
        bestScore = float('inf')
        for row, col in get_empty_spots(board):
            board[row][col] = 'X'
            score = aiLogic(board, depth + 1, True, maxDepth)
            board[row][col] = ' '
            bestScore = min(bestScore, score)
        return bestScore

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
    coinFlip = random.randint(0, 1)
    if coinFlip == 1:
        currentPlayer = 'Player'
    else:
        currentPlayer = 'AI'
    
    while has_open_spaces(board) and not check_winner(board, 'X') and not check_winner(board, 'O'):
        if currentPlayer == 'Player':
            for row in board:
                print(row)
            player()
            currentPlayer = 'AI'
            if not has_open_spaces(board):
                break
        else:
            ai(board)
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
