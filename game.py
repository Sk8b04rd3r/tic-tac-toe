def display_board(board):
    print("   1   2   3")
    for i in range(3):
        print(i + 1, end=" ")
        for j in range(3):
            print(f" {board[i][j]} ", end="")
            if j < 2:
                print("|", end="")
        print()
        if i < 2:
            print("  ---|---|---")

def is_game_over(board, symbol):
    for i in range(3):
        if board[i][0] == symbol and board[i][1] == symbol and board[i][2] == symbol:
            return 1
        if board[0][i] == symbol and board[1][i] == symbol and board[2][i] == symbol:
            return 1
    if board[0][0] == symbol and board[1][1] == symbol and board[2][2] == symbol:
        return 1
    if board[0][2] == symbol and board[1][1] == symbol and board[2][0] == symbol:
        return 1
    tie = 1
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                tie = 0
                break
    if tie:
        return 2
    return 0

def main():
    board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    player = 'X'
    result = 0

    print("Welcome to Tic-Tac-Toe!")

    while result == 0:
        display_board(board)
        row, col = map(int, input(f"Player {player}, enter row (1-3) and column (1-3): ").split())
        row -= 1
        col -= 1
        if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' ':
            board[row][col] = player
            result = is_game_over(board, player)
            if result == 1:
                display_board(board)
                print(f"Player {player} wins!")
            elif result == 2:
                display_board(board)
                print("It's a tie!")
            player = 'O' if player == 'X' else 'X'
        else:
            print("Invalid move. Try again.")

if __name__ == "__main__":
    main()
