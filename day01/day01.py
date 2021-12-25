def main():
    depth_increased_count()
    sliding_window_sum_increased_count()

# count number of times when n + 1 > n
def depth_increased_count():
    with open("input.txt") as file:
        counter = 0
        prev = int(file.readline())
        while y := file.readline():
            if int(y) > prev:
                counter += 1
            prev = int(y)

    return counter

# count number of times when sum(n + 1, n + 4) > sum(n, n + 3)
def sliding_window_sum_increased_count():
    with open('input.txt') as file:
        nums = [int(x) for x in file.readlines()]
        counter = 0
        for i, _ in enumerate(nums[:-3]):
            if sum(nums[i:i+3]) < sum(nums[i+1:i+4]):
                counter += 1

    return counter

if __name__ == "__main__":
    main()
