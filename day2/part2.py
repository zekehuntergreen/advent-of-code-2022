puzzle_input = open("input.txt", "r").read()
lines = puzzle_input.splitlines()

outcome_key = {
    "X": "L",
    "Y": "D",
    "Z": "W",
}


class Move:
    beats = None
    beaten_by = None

    def __init__(self, move, play_score):
        self.move = move
        self.play_score = play_score


rock = Move("R", 1)
paper = Move("P", 2)
scissors = Move("S", 3)
rock.beats = scissors
rock.beaten_by = paper
paper.beats = rock
paper.beaten_by = scissors
scissors.beats = paper
scissors.beaten_by = rock

move_key = {
    "A": rock,
    "B": paper,
    "C": scissors,
}


def get_my_move(opponents_move, outcome):
    if outcome == "D":
        return opponents_move
    elif outcome == "W":
        return opponents_move.beaten_by
    else:
        return opponents_move.beats


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
    opponents_move_str, outcome = line.split()
    opponents_move = move_key[opponents_move_str]
    print("opponent", opponents_move.move)
    outcome = outcome_key[outcome]
    print("outcome", outcome)
    my_move = get_my_move(opponents_move, outcome)
    print("my move", my_move.move)

    score = my_move.play_score + get_score(opponents_move.move, my_move.move)
    print(score)
    total_score += score

print(f"total_score: {total_score}")
