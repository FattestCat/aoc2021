from pprint import pprint
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
Fold = namedtuple("Fold", ["axis", "pos"])


def main():
    coords, folds = get_data()
    coords = clean_coords(coords)
    folds = clean_folds(folds)
    grid = construct_grid(coords)
    fold_grid(grid, folds)
    replace_with_dots(grid)
    for line in grid:
        print(line)



def replace_with_dots(grid):
    for i, line in enumerate(grid):
        for j, value in enumerate(line):
            if value == 0:
                grid[i][j] = '.'
            if value == 1:
                grid[i][j] = '#'

def count_dots(grid):
    return len([x for p in grid for x in p if x == 1])

def fold_grid(grid, folds):
    for fold in folds:
        if fold.axis == 'y':
            fold_grid_up(grid, fold.pos)
        if fold.axis == 'x':
            fold_grid_left(grid, fold.pos)


def fold_grid_up(grid, i):
    for n in range(i):
        grid[n] = merge_lines(grid[n], grid[-n-1])
    while i + 1:
        grid.pop()
        i -= 1

def fold_grid_left(grid, i):
    for n, line in enumerate(grid):
        grid[n] = fold_line(line, i)

def fold_line(l, i):
    new_line = l[:i]
    tail = l[i+1:]
    for i, v in enumerate(reversed(tail)):
        if v:
            new_line[i] = v
    return new_line

def merge_lines(l1, l2):
    new_line = l1
    for i, v in enumerate(l2):
        if v:
            new_line[i] = v
    return new_line


def construct_grid(coords):
    max_x, max_y = find_dimentions(coords)
    grid = [[0 for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    for x, y in coords:
        grid[y][x] = 1
    return grid


def find_dimentions(coords):
    max_x = max(p.x for p in coords)
    max_y = max(p.y for p in coords)
    return max_x, max_y


def get_data():
    with open("input.txt") as file:
        coords = []

        while (line := file.readline()) != "\n":
            coords.append(line.strip())

        folds = [line.strip() for line in file.readlines()]

    return coords, folds


def clean_coords(coords):
    res = []
    for coord in coords:
        res.append(Point(*tuple(map(int, coord.split(",")))))
    return res


def clean_folds(folds):
    res = []
    for fold in folds:
        _, _, f = fold.split(" ")
        axis, pos = f.split("=")
        res.append(Fold(axis, int(pos)))
    return res


if __name__ == "__main__":
    main()
