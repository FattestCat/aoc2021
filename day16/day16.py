from operator import mul
from functools import reduce

type_sum = 0
version_sum = 0


def main():
    data = get_data()
    data = "".join(data)
    ver, type_id, numbers, end = parse_packet(0, data)
    print(f"numbers: {numbers}")


def parse_packet(i, data):
    ver = int(data[i : i + 3], base=2)
    type_ = int(data[i + 3 : i + 6], base=2)
    update_version(ver)
    if type_ == 4:
        end = i + 6
        numbers = []
        while data[end] != "0":
            numbers.append(data[end : end + 5][1:])
            end += 5
        numbers.append(data[end : end + 5][1:])
        end += 5
        value = convert_to_int(numbers)
        return ver, type_, value, end
    else:
        if data[i + 6] == "0":
            sub_len = int(data[i + 7 : i + 22], base=2)
            end = i + 22
            sub_numbers = []
            while end < (sub_len + 22 + i):
                ver, t_, value, end = parse_packet(end, data)
                sub_numbers.append(value)
            res = get_packet_value(type_, sub_numbers)
            return ver, type_, res, end
        else:
            sub_cnt = int(data[i + 7 : i + 18], base=2)
            end = i + 18
            sub_numbers = []
            while sub_cnt:
                ver, t_, value, end = parse_packet(end, data)
                sub_numbers.append(value)
                sub_cnt -= 1
            res = get_packet_value(type_, sub_numbers)
            return ver, type_, res, end


def get_packet_value(t, numbers):
    if t == 0:
        return sum(numbers)
    if t == 1:
        return reduce(mul, numbers)
    if t == 2:
        return min(numbers)
    if t == 3:
        return max(numbers)
    if t == 5:
        return 1 if numbers[0] > numbers[1] else 0
    if t == 6:
        return 1 if numbers[0] < numbers[1] else 0
    if t == 7:
        return 1 if numbers[0] == numbers[1] else 0


def update_version(ver):
    global version_sum
    version_sum += ver


def convert_to_int(numbers):
    return int("".join(numbers), base=2)


def get_data():
    with open("input.txt") as file:
        data = [f"{int(n, base=16):04b}" for n in file.readline().strip()]
    return data


if __name__ == "__main__":
    main()
