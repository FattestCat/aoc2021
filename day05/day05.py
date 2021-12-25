import re


def main():
    coords = get_data()
    coords = transform_coords(coords)
    ints = find_intersections(coords)
    print(ints)


def find_intersections(coords):
    marked_points = set()
    intersected = set()
    for p1, p2 in coords:
        for point in p1.get_all_points_between(p2):
            if (point.x, point.y) in marked_points:
                intersected.add((point.x, point.y))
            marked_points.add((point.x, point.y))
    return len(intersected)


def get_data():
    pat = re.compile("[\\d]+")
    coords = []
    with open("input.txt") as file:
        while line := file.readline():
            coords.append([int(x) for x in pat.findall(line)])
    return coords


def transform_coords(coords):
    new_coords = [[Point(x1, y1), Point(x2, y2)] for x1, y1, x2, y2 in coords]
    return new_coords


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_all_points_between(self, other):
        if self.x == other.x:
            lower = min(self.y, other.y)
            upper = max(self.y, other.y)
            return [Point(self.x, y) for y in range(lower, upper + 1)]

        if self.y == other.y:
            lower = min(self.x, other.x)
            upper = max(self.x, other.x)
            return [Point(x, self.y) for x in range(lower, upper + 1)]

        if self.x < other.x and self.y < other.y:
            return [Point(self.x + i, self.y + i) for i in range(other.x - self.x + 1)]

        if self.x > other.x and self.y > other.y:
            return [Point(self.x - i, self.y - i) for i in range(self.x - other.x + 1)]

        if self.x < other.x and self.y > other.y:
            return [Point(self.x + i, self.y - i) for i in range(self.y - other.y + 1)]

        if self.x > other.x and self.y < other.y:
            return [Point(self.x - i, self.y + i) for i in range(self.x - other.x + 1)]

        return self

    def __str__(self):
        return f"(x: {self.x}, y: {self.y})"

    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return hash((self.x, self.y))


if __name__ == "__main__":
    main()
