def main():
    numbers = get_data()
    # constant_consumption(numbers)
    inc_consumption(numbers)


def inc_consumption(numbers):
    smallest_sm = float("inf")
    for position in range(min(numbers), max(numbers) + 1):
        if (sm := sum(fuel_cost(position, n) for n in numbers)) < smallest_sm:
            smallest_sm = sm
    print(f"smallest cons: {smallest_sm}")


def fuel_cost(number, position):
    n = abs(number - position)
    return n * (n + 1) / 2


def constant_consumption(numbers):
    smallest_sm = float("inf")
    for position in range(min(numbers), max(numbers) + 1):
        if (sm := sum([abs(n - position) for n in numbers])) < smallest_sm:
            smallest_sm = sm

    print(f"smallest sum: {smallest_sm}")


def get_data():
    with open("input.txt") as file:
        numbers = [int(n) for n in file.readline().strip().split(",")]
    return numbers


if __name__ == "__main__":
    main()
