import math
import re
from typing import List

puzzle_input = open("test_input.txt", "r").read()
stacks_str, operations = puzzle_input.split("\n\n")

stacks_str_lines = stacks_str.splitlines()

stacks: List[List[str]] = [
    [] for _ in range(math.floor((len(stacks_str_lines[-1]) + 1) / 4))
]

for row in reversed(stacks_str_lines[:-1]):
    row_crates = [row[i : i + 3].strip() for i in range(0, len(row), 4)]
    for i, crate in enumerate(row_crates):
        if crate:
            stacks[i].append(crate)

for op in operations.splitlines():
    num, from_stack, to_stack = map(
        int, re.findall(r"move (\d+) from (\d+) to (\d+)", op)[0]
    )
    to_stack -= 1
    from_stack -= 1
    to_move = stacks[from_stack][len(stacks[from_stack]) - num :]
    stacks[to_stack] += to_move
    stacks[from_stack] = stacks[from_stack][: -1 * num]

result = "".join([s[-1][1:-1] for s in stacks])
print(result)
