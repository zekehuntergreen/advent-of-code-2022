import math
import re
import pprint
from typing import Dict, Set

pp = pprint.PrettyPrinter(indent=4)

test = True
Y = 10 if test else 2000000
input_file = "test_input.txt" if test else "input.txt"
puzzle_input = open(input_file, "r").read().splitlines()

disqualified_ranges: Dict[int, Set[tuple]] = {}
signals = set()
beacons = set()


def add_disqualified_range(min_x, max_x, y):
    if y in disqualified_ranges:
        disqualified_ranges[y].add((min_x, max_x))
    else:
        disqualified_ranges[y] = {(min_x, max_x)}


for line in puzzle_input:
    sx, sy, bx, by = map(
        int,
        re.findall(
            r".*x=(-?\d+), y=(-?\d+).*x=(-?\d+), y=(-?\d+)",
            line,
        )[0],
    )
    s, b = (sx, sy), (bx, by)
    signals.add(s)
    beacons.add(b)

    x_diff = abs(sx - bx)
    y_diff = abs(sy - by)
    m = x_diff + y_diff
    print(s, b, m)

    # instead of storing sets of disqualified coordinates, we could store a list
    # of tuples representing the range of disqualified coordinates
    for y in range(sy - m, sy + m + 1):
        x_range = abs(m - abs(sy - y))
        add_disqualified_range(sx - x_range, sx + x_range, y)

    # x_range = abs(m - abs(sy - Y))
    # add_disqualified_range(sx - x_range, sx + x_range, Y)

    # for y in range(sy - m, sy + m + 1):
    #     x_range = abs(m - abs(sy - y))
    #     for x in range(sx - x_range, sx + x_range + 1):
    #         if (x, y) not in beacons:
    #             add_disqualified_coordinate(x, y)


if test:
    pp.pprint(disqualified_ranges)


def coordinate_in_disqualified_range(x, y):
    if not y in disqualified_ranges:
        return False
    for r in disqualified_ranges[y]:
        if r[0] <= x <= r[1]:
            return True
    return False


def print_grid():
    min_x, max_x, min_y, max_y = -10, 30, -10, 30
    # print(min_x, max_x, min_y, max_y)
    print("\t ", end="")
    for x in range(min_x, max_x):
        print(x % 10, end="")
    print()

    for y in range(min_y, max_y):
        print(f"{y}\t", end=" ")
        for x in range(min_x, max_x):
            if (x, y) in signals:
                print("S", end="")
            elif (x, y) in beacons:
                print("B", end="")
            # elif y in disqualified_coordinates and x in disqualified_coordinates[y]:
            #     print("#", end="")
            elif coordinate_in_disqualified_range(x, y):
                print("#", end="")
            else:
                print(".", end="")
        print()


disqualified_at_Y = set()
for r in disqualified_ranges[Y]:
    for x in range(r[0], r[1] + 1):
        if (x, Y) not in beacons and (x, Y) not in signals:
            disqualified_at_Y.add((x))


# pp.pprint(disqualified_at_Y)
# # print()
if test:
    print_grid()
print("\npart 1", len(disqualified_at_Y))
