from functools import reduce
from operator import mul
from collections import deque

inf = float("inf")

# 120 to low
# 5265 to low

# 39086565 to high


def main():
    data = get_data()
    add_borders(data)
    lp, lc = count_low_points(data)
    areas = find_areas(data, lc)
    print(f'first part: {sum(lp) + len(lp)}')
    print(f'second part: {reduce(mul, sorted(areas)[-3:])}')


def find_areas(data, lowest_coords):
    areas = []
    for i, j in lowest_coords:
        areas.append(find_area(data, i, j))
    return areas


def find_area(data, i, j):
    queue = deque()
    queue.append((i, j))
    area = 0
    visited = set()
    while queue:
        x, y = queue.popleft()
        if (x, y) in visited:
            continue
        area += 1
        visited.add((x, y))
        if data[x + 1][y] < 9:
            queue.append((x + 1, y))
        if data[x - 1][y] < 9:
            queue.append((x - 1, y))
        if data[x][y + 1] < 9:
            queue.append((x, y + 1))
        if data[x][y - 1] < 9:
            queue.append((x, y - 1))
    return area


def get_data():
    with open("input.txt") as file:
        lines = file.readlines()
    return [[int(n) for n in line.strip()] for line in lines]


def add_borders(data):
    line_len = len(data[0])
    [wrap_line(line) for line in data]
    data.insert(0, get_line(inf, line_len + 2))
    data.append(get_line(inf, line_len + 2))
    return data


def wrap_line(line):
    line.insert(0, inf)
    line.append(inf)
    return line


def get_line(symbol, lenth):
    return [symbol for _ in range(lenth)]


def count_low_points(data):
    lowest_points = []
    lowest_coords = []
    for i, line in enumerate(data[1:-1], 1):
        for j, number in enumerate(line[1:-1], 1):
            if is_lowest(i, j, data):
                lowest_points.append(number)
                lowest_coords.append((i, j))
    return lowest_points, lowest_coords


def is_lowest(i, j, data):
    point = data[i][j]
    if (
        point < data[i + 1][j]
        and point < data[i - 1][j]
        and point < data[i][j + 1]
        and point < data[i][j - 1]
    ):
        return True
    return False


if __name__ == "__main__":
    main()
