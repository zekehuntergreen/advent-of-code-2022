import functools


puzzle_input = open("input.txt", "r").read().splitlines()


def compare(left, right):
    if type(left) == int and type(right) == int:
        if left == right:
            return None
        return left < right
    elif type(left) == int:
        return compare([left], right)
    elif type(right) == int:
        return compare(left, [right])

    for i in range(min([len(left), len(right)])):
        result = compare(left[i], right[i])
        if result is None:
            continue
        else:
            return result

    if len(left) == len(right):
        return None
    return len(left) < len(right)


packet_pairs = []
packets = []
for i in range(0, len(puzzle_input), 3):
    left, right = eval(puzzle_input[i]), eval(puzzle_input[i + 1])
    packet_pairs.append((left, right))
    packets.append(left)
    packets.append(right)

in_correct_order = []
for i, p in enumerate(packet_pairs):
    left, right = p
    if compare(left, right):
        in_correct_order.append(i + 1)

print("part 1:", sum(in_correct_order))

divider1, divider2 = [[2]], [[6]]
packets.append(divider1)
packets.append(divider2)


def cmp(x, y):
    result = compare(x, y)
    if result == True:
        return -1
    elif result == False:
        return 1
    else:
        return 0


packets = sorted(packets, key=functools.cmp_to_key(cmp))

print("part 2:", (packets.index(divider1) + 1) * (packets.index(divider2) + 1))
