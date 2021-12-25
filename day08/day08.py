def main():
    data = get_data()
    sum = 0
    for row in data:
        numbers = decode(row[0])
        number = ""
        for displayed_number in row[1]:
            number += str(numbers.index(set(displayed_number)))
        sum += int(number)
    print(sum)


def get_simple_digits(data):
    return [
        x
        for _, d in data
        for x in d
        if len(x) == 2 or len(x) == 4 or len(x) == 7 or len(x) == 3
    ]


def get_data():
    with open("input.txt") as file:
        lines = file.readlines()
        lines = [line.split("|") for line in lines]
        lines = [
            (digits.strip().split(), output.strip().split()) for digits, output in lines
        ]

    return lines


def decode(numbers):
    for d in numbers:
        if len(d) == 2:
            one = set(d)
        if len(d) == 4:
            four = set(d)
        if len(d) == 3:
            seven = set(d)
        if len(d) == 7:
            eight = set(d)

    six = [
        x for x in numbers if eight.difference(seven).issubset(set(x)) and len(x) == 6
    ]
    six = set(*six)
    nine = [x for x in numbers if seven.union(four).issubset(set(x)) and len(x) == 6]
    nine = set(*nine)
    five = [
        x for x in numbers if nine.difference(seven).issubset(set(x)) and len(x) == 5
    ]
    five = set(*five)
    three = [x for x in numbers if len(x) == 5 and one.issubset(set(x))]
    three = set(*three)
    two = [x for x in numbers if len(x) == 5 and set(x) != five and set(x) != three]
    two = set(*two)
    zero = [x for x in numbers if len(x) == 6 and set(x) != nine and set(x) != six]
    zero = set(*zero)

    found = [zero, one, two, three, four, five, six, seven, eight, nine]  # type: ignore
    return found


if __name__ == "__main__":
    main()
