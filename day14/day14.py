def main():
    template, rules = get_data()
    rounds = 40
    elems = extract_elements(rules)
    elems = dict(zip(elems, [0 for _ in range(len(elems))]))
    pairs = extract_pairs(template)
    get_starting_elem_count(template, elems)
    play_game(elems, pairs, rules, rounds)


def play_game(elems, pairs, rules, rounds):
    if rounds == 0:
        print(max(elems.values()) - min(elems.values()))
        return max(elems.values()) - min(elems.values())
    play_game(elems, play_round(elems, pairs, rules), rules, rounds - 1)


def play_round(elems, pairs, rules):
    new_pairs = {}
    for pair in pairs:
        new_elem = rules[pair]
        p1, p2 = create_new_pairs(pair, new_elem)
        new_pairs[p1] = new_pairs.get(p1, 0) + pairs[pair]
        new_pairs[p2] = new_pairs.get(p2, 0) + pairs[pair]
        elems[new_elem] = elems.get(new_elem, 0) + pairs[pair]
    return new_pairs


def create_new_pairs(pair, new_elem):
    return pair[0] + new_elem, new_elem + pair[1]


def get_starting_elem_count(template, elems):
    for v in template:
        elems[v] = elems.get(v, 0) + 1


def extract_pairs(template):
    pairs = {}
    for i, _ in enumerate(template[:-1]):
        pair = "".join((template[i], template[i + 1]))
        pairs[pair] = pairs.get(pair, 0) + 1
    return pairs


def extract_elements(rules):
    return set([elem for pair in rules for elem in pair])


def get_data():
    with open("input.txt") as file:
        template = list(file.readline().strip())
        file.readline()
        rules = {}

        # rules = {
        # pair: new
        # for line in file.readlines()
        # for pair, new in line.strip().replace(" ", "").split("->")
        # }

        for line in file.readlines():
            rule = line.strip().replace(" ", "").split("->")
            rules[rule[0]] = rule[1]

        return template, rules


if __name__ == "__main__":
    main()
