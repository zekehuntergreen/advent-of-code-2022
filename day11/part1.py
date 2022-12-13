import math
import re


puzzle_input = open("input.txt", "r").read().split("\n\n")


class Monkey:
    def __init__(self, items, op, test, test_true, test_false):
        self.items = items
        self.op = op
        self.test = test
        self.test_true = test_true
        self.test_false = test_false
        self.items_inspected = 0

    def operation(self, old):
        return self.op(old)


monkeys = []

for line in puzzle_input:
    starting_items_str, op, test, test_true, test_false = re.findall(
        r"""Monkey \d+:\s+Starting items: (.*)\s+Operation: new = (.*)\s+Test: divisible by (.*)\s+If true: throw to monkey (.*)\s+If false: throw to monkey (.*)""",
        line,
    )[0]
    starting_items = list(map(lambda s: int(s), starting_items_str.split(", ")))
    test = int(test)
    test_true = int(test_true)
    test_false = int(test_false)
    monkeys.append(
        Monkey(
            starting_items,
            eval("lambda old: " + op),
            test,
            test_true,
            test_false,
        )
    )

# print([m.__dict__ for m in monkeys])

lcm = math.prod([m.test for m in monkeys])

for round in range(1, 10001):
    for i, m in enumerate(monkeys):
        while len(m.items) > 0:
            worry_level = m.items.pop(0)
            m.items_inspected += 1
            worry_level = m.operation(worry_level)
            # worry_level = worry_level // 3
            if worry_level % m.test == 0:
                next_monkey = m.test_true
            else:
                next_monkey = m.test_false
            monkeys[next_monkey].items.append(worry_level % lcm)

    if round % 1000 == 0:
        print(f"\nround {round} ")
        for i, m in enumerate(monkeys):
            print(f"monkey {i} {m.items_inspected}")


monkeys.sort(key=lambda m: m.items_inspected, reverse=True)
print(monkeys[0].items_inspected * monkeys[1].items_inspected)
