import string
import math

test = False
input_file = "test_input.txt" if test else "input.txt"
puzzle_input = open(input_file).read().splitlines()


def can_move(from_height, to_height):
    # print(from_height, to_height)
    if to_height == "E":
        to_height = "z"
    if from_height == "E":
        from_height = "z"
    if from_height == "S":
        from_height = "a"
    if to_height == "S":
        to_height = "a"
    if from_height == to_height:
        return True
    return (
        string.ascii_lowercase.index(to_height)
        - string.ascii_lowercase.index(from_height)
        == 1
    )


grid_height = len(puzzle_input)
grid_width = len(puzzle_input[0])


# find starting position
starting_position = (-1, -1)
for i in range(grid_height):
    for j in range(grid_width):
        if puzzle_input[i][j] == "S":
            starting_position = (j, i)
            break


def find_high_ground(y, x, visited):
    # print(x, y, visited)
    current_height = puzzle_input[y][x]
    if current_height == "E":
        return len(visited)

    visited.add((y, x))
    possible_moves = ((y - 1, x), (y, x + 1), (y + 1, x), (y, x - 1))
    possible_move_heights = [math.inf]

    for py, px in possible_moves:
        if (
            py >= 0
            and py <= grid_height - 1
            and px <= grid_width - 1
            and px >= 0
            and can_move(current_height, puzzle_input[py][px])
            and (py, px) not in visited
        ):
            possible_move_heights.append(
                find_high_ground(py, px, set([v for v in visited]))
            )
    return min(possible_move_heights)


print(find_high_ground(*starting_position, set()))
