from pprint import pprint
from collections import Counter
from copy import copy

start = "start"
end = "end"

paths = []

# islower() in validation is the slowest part
# might be improved using look up on set() of lower key points
def main():
    data = get_data()
    edges = extract_edges(data)
    find_paths(start, start, end, [], edges)
    pprint(len(paths))


def get_data():
    with open("input.txt") as file:
        lines = [line.strip() for line in file.readlines()]
        return lines


def find_paths(point, start, end, base, edges):
    next_points = find_all_next(point, start, edges)
    for next_point in next_points:
        new_base = copy(base)
        new_base.append(next_point)
        # if not is_valid(new_base):
        if not is_valid_part_two(new_base):
            continue
        if next_point == end:
            paths.append(new_base)
        else:
            find_paths(next_point, start, end, new_base, edges)


def is_valid(path):
    small = [node for node in path if node.islower()]
    if len(small) == 0 or max(Counter(small).values()) < 2:
        return True
    return False


def is_valid_part_two(path):
    small = [node for node in path if node.islower()]
    counter = Counter(small)
    if len(small) == 0:
        return True
    if max(counter.values()) > 2:
        return False
    if len([v for v in counter.values() if v == 2]) > 1:
        return False
    return True


def extract_edges(data):
    return set(tuple([*e.split("-")]) for e in data)


def find_all_next(point, start, edges):
    paths = [edge for edge in edges if point in edge]
    return [p for path in paths for p in path if p != point and p != start]


if __name__ == "__main__":
    main()
