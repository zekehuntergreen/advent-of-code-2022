import math
import re

test = False
Y = 10 if test else 2000000
input_file = "test_input.txt" if test else "input.txt"
puzzle_input = open(input_file, "r").read().splitlines()

sensor_beacons = []
beacons = set()


def calculate_manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def is_point_on_disk(sensor_coordinates, sensor_radius, point_coordinates):
    return (
        calculate_manhattan_distance(sensor_coordinates, point_coordinates)
        <= sensor_radius
    )


def point_could_be_beacon(point_coordinates):
    # is this point either a beacon or outside the range of all sensors?
    if point_coordinates in beacons:
        return True
    for sensor, _, radius in sensor_beacons:
        if is_point_on_disk(sensor, radius, point_coordinates):
            return False
    return True


min_x, max_x, max_radius = math.inf, -math.inf, -math.inf
for line in puzzle_input:
    sx, sy, bx, by = map(
        int,
        re.findall(
            r".*x=(-?\d+), y=(-?\d+).*x=(-?\d+), y=(-?\d+)",
            line,
        )[0],
    )
    s, b = (sx, sy), (bx, by)
    beacons.add(b)

    if sx < min_x:
        min_x = sx
    if sx > max_x:
        max_x = sx
    radius = calculate_manhattan_distance(s, b)
    if radius > max_radius:
        max_radius = radius

    sensor_beacons.append((s, b, radius))

# part 1
number_of_points_that_cant_be_a_beacon = 0
for x in range(min_x - max_radius, max_x + max_radius):
    result = point_could_be_beacon((x, Y))
    if not result:
        number_of_points_that_cant_be_a_beacon += 1

print(f"part 1: {number_of_points_that_cant_be_a_beacon}")

# part 2
# range_limit = 20 if test else 4000000
# for y in range(0, range_limit):
#     if y % 10 == 0:
#         print(y)
#     for x in range(0, range_limit):
#         p = (x, y)
#         if point_could_be_beacon(p) and p not in beacons:
#             print(f"part 2: {p}")
