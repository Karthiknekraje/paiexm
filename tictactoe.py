import random

def print_board(board):
    for row in board: print(" | ".join(row)); print("-" * 5)

def check_winner(board, player):
    return any(all(s == player for s in row) for row in board) or \
           any(all(row[i] == player for row in board) for i in range(3)) or \
           all(board[i][i] == player for i in range(3)) or \
           all(board[i][2 - i] == player for i in range(3))

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def main():
    board = [[" "]*3 for _ in range(3)]
    player, computer = "X", "O"

    while True:
        print_board(board)
        r, c = map(int, input("Enter row and column (0-2): ").split())
        if board[r][c] != " ": print("Taken, try again."); continue

        board[r][c] = player
        if check_winner(board, player): print_board(board); print("Player wins!"); break
        if is_full(board): print_board(board); print("Draw!"); break

        r, c = random.choice([(r, c) for r in range(3) for c in range(3) if board[r][c] == " "])
        board[r][c] = computer
        if check_winner(board, computer): print_board(board); print("Computer wins!"); break
        if is_full(board): print_board(board); print("Draw!"); break

if __name__ == "__main__":
    main()
