from collections import Counter


def main():
    first_part()
    second_part()


def first_part():
    with open("input01.txt") as file:
        x = 0
        y = 0
        lines = (line.strip().split(" ") for line in file.readlines())
        for line in lines:
            if line[0] == "forward":
                x += int(line[1])
            elif line[0] == "down":
                y += int(line[1])
            elif line[0] == "up":
                y -= int(line[1])

        print(f"x: {x}, y: {y}, prod: {x * y}")
        return x * y


def second_part():
    with open("input01.txt") as file:
        x = 0
        y = 0
        aim = 0
        lines = (line.strip().split(" ") for line in file.readlines())
        for line in lines:
            if line[0] == "forward":
                x += int(line[1])
                y += aim * int(line[1])
            elif line[0] == "down":
                aim += int(line[1])
            elif line[0] == "up":
                aim -= int(line[1])

        print(f"x: {x}, y: {y}, prod: {x * y}")
        return x * y


if __name__ == "__main__":
    main()
