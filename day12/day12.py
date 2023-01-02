import string
import math

test = False
input_file = "test_input.txt" if test else "input.txt"
puzzle_input = open(input_file).read().splitlines()
grid_height, grid_width = len(puzzle_input), len(puzzle_input[0])
fewest_moves_from_start = [
    [math.inf for _ in range(grid_width)] for _ in range(grid_height)
]


def find_letter(letter):
    for i in range(grid_height):
        for j in range(grid_width):
            if puzzle_input[i][j] == letter:
                return (i, j)


def can_move(from_height, to_height):
    from_height = from_height.replace("E", "z").replace("S", "a")
    to_height = to_height.replace("E", "z").replace("S", "a")
    return (
        string.ascii_lowercase.index(to_height)
        - string.ascii_lowercase.index(from_height)
        <= 1
    )


start_position, end_position = find_letter("S"), find_letter("E")
fewest_moves_from_start[start_position[0]][start_position[1]] = 0

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
                ):
                    # print(y, x, py, px)
                    if (
                        can_move(puzzle_input[y][x], puzzle_input[py][px])
                        and fewest_moves_from_start[y][x] + 1
                        < fewest_moves_from_start[py][px]
                    ):
                        # print(f"can move from {y},{x} to {py},{px}")
                        updating = True
                        fewest_moves_from_start[py][px] = (
                            fewest_moves_from_start[y][x] + 1
                        )

# print(fewest_moves_from_start)
print(fewest_moves_from_start[end_position[0]][end_position[1]])
