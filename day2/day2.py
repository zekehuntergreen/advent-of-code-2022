puzzle_input = open("input.txt", "r").read()
lines = puzzle_input.splitlines()

move_key = {
    "A": "R",
    "B": "P",
    "C": "S",
    "X": "R",
    "Y": "P",
    "Z": "S",
}

play_scores = {
    "R": 1,
    "P": 2,
    "S": 3,
}


def get_score(opponents_move, my_move):
    if (
        my_move == "R"
        and opponents_move == "S"
        or my_move == "P"
        and opponents_move == "R"
        or my_move == "S"
        and opponents_move == "P"
    ):
        return 6
    elif opponents_move == my_move:
        return 3
    else:
        return 0


total_score = 0
for line in lines:
    opponents_move, my_move = line.split()
    opponents_move = move_key[opponents_move]
    my_move = move_key[my_move]
    win_score = get_score(opponents_move, my_move)
    score = win_score + play_scores[my_move]
    print("*" * 8)
    print(opponents_move, my_move)
    print(score)
    total_score += score

print(f"total_score: {total_score}")
