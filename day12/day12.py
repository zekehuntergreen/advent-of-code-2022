import string
import math

test = False
input_file = "test_input.txt" if test else "input.txt"
puzzle_input = open(input_file).read().splitlines()
grid_height, grid_width = len(puzzle_input), len(puzzle_input[0])
fewest_moves_from_end = [
    [math.inf for _ in range(grid_width)] for _ in range(grid_height)
]


def find_letter(letter):
    for i in range(grid_height):
        for j in range(grid_width):
            if puzzle_input[i][j] == letter:
                return (i, j)


def get_height_of_letter(letter):
    return string.ascii_lowercase.index(letter.replace("E", "z").replace("S", "a"))


def can_move(from_height, to_height):
    return get_height_of_letter(to_height) - get_height_of_letter(from_height) <= 1


start_position, end_position = find_letter("S"), find_letter("E")
fewest_moves_from_end[end_position[0]][end_position[1]] = 0

updating = True
while updating:
    updating = False
    for y in range(grid_height):
        for x in range(grid_width):
            possible_moves = ((y - 1, x), (y, x + 1), (y + 1, x), (y, x - 1))
            for py, px in possible_moves:
                if (
                    py >= 0
                    and py <= grid_height - 1
                    and px <= grid_width - 1
                    and px >= 0
                    and can_move(puzzle_input[py][px], puzzle_input[y][x])
                    and fewest_moves_from_end[y][x] + 1 < fewest_moves_from_end[py][px]
                ):
                    updating = True
                    fewest_moves_from_end[py][px] = fewest_moves_from_end[y][x] + 1

print(f"part 1: {fewest_moves_from_end[start_position[0]][start_position[1]]}")

shortest_path = math.inf
for i in range(grid_height):
    for j in range(grid_width):
        if (
            get_height_of_letter(puzzle_input[i][j]) == 0
            and fewest_moves_from_end[i][j] < shortest_path
        ):
            shortest_path = fewest_moves_from_end[i][j]
print(f"part 2: {shortest_path}")
