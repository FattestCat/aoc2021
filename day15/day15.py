import heapq


SIZE = 5


def main():
    grid = get_data()
    paths = [
        (0, 0, 0),
    ]
    heapq.heapify(paths)
    visited = {
        (0, 0),
    }

    while paths:
        path = heapq.heappop(paths)
        found = False

        for nei in get_neis(path, grid):
            if (nei[1], nei[2]) in visited:
                continue
            if nei[1] == len(grid) * SIZE - 1 and nei[2] == len(grid[0]) * SIZE - 1:
                found = True
                print(f"found: {nei[0]}")
                break
            visited.add((nei[1], nei[2]))
            heapq.heappush(paths, nei)
        if found:
            break


def get_value(y, x, grid):
    y_shift = y // len(grid)
    x_shift = x // len(grid[0])
    y_in = y % len(grid)
    x_in = x % len(grid)
    value = grid[y_in][x_in] + y_shift + x_shift
    if value > 9:
        return value % 10 + 1
    return value


def get_neis(path, grid):
    neis = []
    for y, x in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        new_x = path[2] + x
        new_y = path[1] + y
        if 0 <= new_x < len(grid[0]) * SIZE and 0 <= new_y < len(grid) * SIZE:
            new_d = path[0] + get_value(new_y, new_x, grid)
            neis.append((new_d, new_y, new_x))
    return neis


def get_data():
    with open("input.txt") as file:
        grid = [[int(v) for v in line.strip()] for line in file.readlines()]
    return grid


if __name__ == "__main__":
    main()
