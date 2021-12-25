def main():
    power_consumption()
    oxygen_co2()


def power_consumption():
    with open("input.txt") as file:
        lines = [line.strip() for line in file.readlines()]
        line_lenth = len(lines[0])
        gamma_values = [0 for _ in range(line_lenth)]
        for line in lines:
            for i, value in enumerate(line):
                update_gamma(gamma_values, value, i)
        gamma_rate = [(1 if x > 0 else 0) for x in gamma_values]
        epsilon_rate = [(1 if x == 0 else 0) for x in gamma_rate]

        return to_dec(gamma_rate) * to_dec(epsilon_rate)


def oxygen_co2():
    with open("input.txt") as file:
        lines = [line.strip() for line in file.readlines()]
        oxygen = lines[:]
        co2 = lines[:]
        bits_len = len(lines[0])
        while len(oxygen) > 1:
            for i in range(bits_len):
                oxygen = clean_oxygen_data(oxygen, i)
                if len(oxygen) == 1:
                    break

        while len(co2) > 1:
            for i in range(bits_len):
                co2 = clean_co2_data(co2, i)
                if len(co2) == 1:
                    break

        print(to_dec(oxygen) * to_dec(co2))
        return to_dec(oxygen) * to_dec(co2)


def clean_co2_data(co2, index):
    value = most_common(co2, index, co2=True)
    return [line for line in co2 if line[index] == str(value)]


def clean_oxygen_data(oxygen, index):
    value = most_common(oxygen, index, oxygen=True)
    return [line for line in oxygen if line[index] == str(value)]


def most_common(lst, index, *, oxygen=False, co2=False):
    """
    find most common number (0 or 1) on index place for all elements in lst
    for oxygen and least common number fot co2
    """
    indicator = 0
    for elem in lst:
        if elem[index] == "1":
            indicator += 1
        else:
            indicator -= 1
    if oxygen:
        return 1 if indicator >= 0 else 0
    if co2:
        return 0 if indicator >= 0 else 1


def update_gamma(gamma, value, index):
    if value == "1":
        gamma[index] += 1
    else:
        gamma[index] -= 1


def to_dec(lst):
    res = "".join(str(x) for x in lst)
    return int(res, 2)


if __name__ == "__main__":
    main()
