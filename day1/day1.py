puzzle_input = open("input/input.txt", "r").read()

elves_calories = []
current_calories = 0
for line in puzzle_input.splitlines():
    if line == "":
        elves_calories.append(current_calories)
        current_calories = 0
    else:
        current_calories += int(line)

sorted = sorted(elves_calories, reverse=True)
top_3 = sorted[:3]
print(top_3)
print(sum(top_3))
