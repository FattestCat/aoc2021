from collections import Counter


def main():
    fishes = get_data()
    counter = Counter(fishes)

    for _ in range(256):
        counter = update_fishes(counter)

    print(sum(counter.values()))


def get_data():
    with open("input.txt") as file:
        fishes = [int(fish) for fish in file.readline().strip().split(",")]
    return fishes


def update_fishes(counter):
    res = {k: 0 for k in range(9)}
    for k, v in counter.items():
        if k == 0:
            res[6] += v
            res[8] = v
        elif k == 7:
            res[6] += v
        else:
            res[k - 1] = counter[k]

    return res


def new_fishes(fishes):
    for fish in fishes:
        if fish == 0:
            yield 6
            yield 8
        else:
            yield fish - 1


if __name__ == "__main__":
    main()
