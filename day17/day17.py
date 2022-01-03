from collections import namedtuple
from collections import Counter

Range = namedtuple("Range", ["min", "max"])
Position = namedtuple("Position", ["x", "y"])

# 2079
# 2709

def main():
    x_range, y_range = [Range(x1, x2) for x1, x2 in get_data()]
    max_y_speed = abs(y_range.max - y_range.min)
    max_x_speed = abs(x_range.max - x_range.min)
    initial_pos = Position(0, 0)
    test_x_range, test_y_range = Range(20, 30), Range(-10, -5)
    print(x_range, y_range)
    print(max_y_speed, max_x_speed)
    possible_speed = [
        (x, y) for x in range(max_x_speed + 1) for y in range(max_y_speed + 1)
    ]
    possible_speed = [(x, y) for x in range(400) for y in range(400)]
    # ths = [
    # find_highest_point(initial_pos, x, y, x_range, y_range)
    # for x, y in possible_speed
    # ]
    good_speed = [
        (x, y)
        for x in range(-400, 400)
        for y in range(-400, 400)
        if find_highest_point(initial_pos, x, y, x_range, y_range)
    ]
    print(len(good_speed))


def get_next_step(pos, x_speed, y_speed):
    return (
        Position(pos.x + x_speed, pos.y + y_speed),
        x_speed - 1 if x_speed > 0 else 0 if x_speed == 0 else x_speed + 1,
        y_speed - 1,
    )


def find_highest_point(pos, x_speed, y_speed, x_range, y_range):
    crossed = False
    while pos.x <= x_range.max and pos.y >= y_range.min:
        pos, x_speed, y_speed = get_next_step(pos, x_speed, y_speed)
        if x_range.min <= pos.x <= x_range.max and y_range.min <= pos.y <= y_range.max:
            crossed = True
    return crossed


def get_data():
    with open("input.txt") as file:
        data = file.readline().strip().split(" ")
        x_range = [int(n) for n in data[2].strip(",x=").split("..")]
        y_range = [int(n) for n in data[3].strip(",y=").split("..")]
    return x_range, y_range


if __name__ == "__main__":
    main()
