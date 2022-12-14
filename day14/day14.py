source, rocks, sand = (500, 0), set(), set()
part1 = False

for line in open("input.txt").readlines():
    points = line.split(" -> ")
    for i in range(len(points) - 1):
        start_x, start_y, end_x, end_y = list(
            map(int, points[i].split(",") + points[i + 1].split(","))
        )
        for j in range(min(start_x, end_x), max(start_x, end_x) + 1):
            for k in range(min(start_y, end_y), max(start_y, end_y) + 1):
                rocks.add((j, k))


max_y = max([y for _, y in rocks])


def print_grid(current=None):
    for y in range(max_y + 4):
        rock_x = [x for x, _ in rocks]
        min_x, max_x = min(rock_x) - 10, max(rock_x) + 10
        for x in range(min_x, max_x):
            if (x, y) in sand or (x, y) == current:
                print("o", end="")
            elif (x, y) == source:
                print("+", end="")
            elif (x, y) in rocks:
                print("#", end="")
            else:
                print(".", end="")
        print()


at_rest = False
current = source
while True:
    if not at_rest:
        down = (current[0], current[1] + 1)
        left = (current[0] - 1, current[1] + 1)
        right = (current[0] + 1, current[1] + 1)
        if not part1 and current[1] == max_y + 1:
            at_rest = True
        elif down not in rocks and down not in sand:
            current = down
        elif left not in rocks and left not in sand:
            current = left
        elif right not in rocks and right not in sand:
            current = right
        else:
            at_rest = True
    else:
        sand.add(current)
        if not part1 and current == source:
            break
        current = source
        at_rest = False

    if part1 and current[1] > max_y:
        break

# print_grid(current=current)
print("\ngrains of sand: ", len(sand))
