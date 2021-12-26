from pprint import pprint


def main():
    data = get_data()
    # flashed_count = play_out(100, data)
    # print(flashed_count)
    rounds_till_sync = find_sync_round(data)
    print(rounds_till_sync)


def get_data():
    with open("input.txt") as file:
        lines = [[int(n) for n in line.strip()] for line in file.readlines()]
        return lines


def find_sync_round(data):
    rounds_played = 0
    while (y := len(set(n for row in data for n in row))) != 1:
        print(f'len set: {y}')
        rounds_played += 1
        play_out(1, data)
        print(rounds_played)
    return rounds_played

def play_out(rounds, data):
    flashes_count = 0
    while rounds:
        rounds -= 1
        incr_points(data)
        flashed_this_round = set()
        while charged := [
            point for point in find_charged(data) if point not in flashed_this_round
        ]:
            flashed_this_round.update(charged)
            flashes_count += len(charged)
            flash_all_charged(charged, data)
        set_flashed_to_zero(flashed_this_round, data)
    return flashes_count


def set_flashed_to_zero(points, data):
    for i, j in points:
        data[i][j] = 0

def flash_all_charged(charged, data):
    for point in charged:
        flash(point, data)


def incr_points(data):
    for i, row in enumerate(data):
        for j, value in enumerate(row):
            data[i][j] = value + 1


def find_charged(data):
    charged = []
    for i, row in enumerate(data):
        for j, _ in enumerate(row):
            if data[i][j] > 9:
                charged.append((i, j))
    return charged


def flash(point, data):
    neis = find_neis(point, data)
    for i, j in neis:
        data[i][j] += 1
    data[point[0]][point[1]] = 0


def find_neis(point, data):
    row_len = len(data[0])
    shifts = [(i, j) for i in range(-1, 2) for j in range(-1, 2)]
    nei_points = [(point[0] + i, point[1] + j) for i, j in shifts]
    nei_points = [
        point
        for point in nei_points
        if 0 <= point[0] < len(data) and 0 <= point[1] < row_len
    ]

    return nei_points


if __name__ == "__main__":
    main()
