source, rocks, sand = (500, 0), set(), set()


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
    for y in range(max_y + 2):
        for x in range(min([x for x, _ in rocks]) - 1, max([x for x, _ in rocks]) + 2):
            if (x, y) == source:
                print("+", end="")
            elif (x, y) in rocks:
                print("#", end="")
            elif (x, y) in sand or (x, y) == current:
                print("o", end="")
            else:
                print(".", end="")
        print()


at_rest = False
current = source
while True:
    if not at_rest:
        rocks_and_sand = rocks.union(sand)
        if (current[0], current[1] + 1) not in rocks_and_sand:
            current = (current[0], current[1] + 1)
        elif (current[0] - 1, current[1] + 1) not in rocks_and_sand:
            current = (current[0] - 1, current[1] + 1)
        elif (current[0] + 1, current[1] + 1) not in rocks_and_sand:
            current = (current[0] + 1, current[1] + 1)
        else:
            at_rest = True
    else:
        sand.add(current)
        current = source
        at_rest = False

    if current[1] > max_y:
        break

print_grid(current=current)
print("\ngrains of sand: ", len(sand))
