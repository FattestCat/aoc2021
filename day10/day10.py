open_br = set(("(", "{", "[", "<"))
close_br = set((")", "]", "}", ">"))
brackets = {")": "(", "]": "[", "}": "{", ">": "<"}
points = {")": 3, "]": 57, "}": 1197, ">": 25137}
completion_point = {"(": 1, "[": 2, "{": 3, "<": 4}


def main():
    data = get_data()
    corrupted = []
    incomplete = []
    for line in data:
        if br := find_first_corrupted(line):
            corrupted.append(br)
        if queue := find_incomplete_sequence(line):
            incomplete.append(queue)
    print(f"corrupted score: {sum(points[br] for br in corrupted)}")

    final_score = get_final_score([count_completion_points(q) for q in incomplete])
    print(f"final score: {final_score}")


def count_completion_points(queue):
    pts = 0
    for br in reversed(queue):
        pts = pts * 5 + completion_point[br]
    return pts


def get_final_score(scores):
    return sorted(scores)[len(scores) // 2]


def get_data():
    with open("input.txt") as file:
        lines = [line.strip() for line in file.readlines()]
        return lines


def find_first_corrupted(line):
    queue = []
    for br in line:
        if br in open_br:
            queue.append(br)
        elif len(queue) == 0:
            return br
        elif queue[-1] == brackets[br]:
            queue.pop()
        else:
            return br


def find_incomplete_sequence(line):
    queue = []
    for br in line:
        if br in open_br:
            queue.append(br)
        elif len(queue) == 0:
            return None
        elif queue[-1] == brackets[br]:
            queue.pop()
        else:
            return None
    return queue


if __name__ == "__main__":
    main()
