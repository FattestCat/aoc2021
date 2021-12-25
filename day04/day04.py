MARKED = -1


def main():
    get_data()


def get_data():
    with open("input.txt") as file:
        numbers = file.readline().strip().split(",")
        string_boards = file.readlines()
        boards = []
        for i, line in enumerate(string_boards[:-4]):
            if line == "\n":
                boards.append(create_new_board(string_boards[i + 1 : i + 6]))

    won_boards = []
    last_won = None
    last_score = None

    for number in numbers:
        for board in boards:
            mark_number_on_board(number, board)

        for board in boards:
            if is_winner(board):
                if board not in won_boards:
                    last_won = board
                    last_score = calculate_score(number, last_won)
                won_boards.append(board)

    print(last_score)
    return last_score


def calculate_score(number, board):
    score = 0
    for row in board:
        for value in row:
            if value != MARKED:
                score += int(value)

    return score * int(number)


def mark_number_on_board(number, board):
    for i, row in enumerate(board):
        for j, value in enumerate(row):
            if value == number:
                board[i][j] = MARKED


def create_new_board(lines):
    return [line.strip().split() for line in lines]


def is_winner(board):
    return check_rows(board) or check_cols(board)


def check_rows(board):
    for row in board:
        if len(set(row)) == 1 and row[0] == MARKED:
            return True
    return False


def check_cols(board):
    reversed_board = [[] for _ in range(len(board))]
    for row in board:
        for j, value in enumerate(row):
            reversed_board[j].append(value)

    return check_rows(reversed_board)


if __name__ == "__main__":
    main()
