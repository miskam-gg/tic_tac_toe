def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board, player):
    # проверка по горизонтали, вертикали и диагоналям
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True
        if all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


def is_full(board):
    return all(cell != ' ' for row in board for cell in row)


def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)
        row, col = map(int, input(f'ход игрока {current_player}. введите строку и столбец (например, 1 2): ').split())

        if row < 1 or row > 3 or col < 1 or col > 3 or board[row - 1][col - 1] != ' ':
            print('неверный ход. попробуйте снова.')
            continue

        board[row - 1][col - 1] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f'игрок {current_player} победил!')
            break
        elif is_full(board):
            print_board(board)
            print('ничья!')
            break

        current_player = 'X' if current_player == 'O' else 'O'


if __name__ == "__main__":
    main()
