import string

rucksacks = open("input.txt", "r").read().splitlines()


def get_priority(common_item: str):
    return (string.ascii_lowercase + string.ascii_uppercase).index(common_item) + 1


# part 1
priority_sum = 0
for rucksack in rucksacks:
    compartment1, compartment2 = set(rucksack[: int(len(rucksack) / 2)]), set(
        rucksack[int(len(rucksack) / 2) :]
    )
    common_item = compartment1.intersection(compartment2).pop()
    priority_sum += get_priority(common_item)

print(f"part 1: {priority_sum}")

# part 2
priority_sum = 0
for i in range(0, len(rucksacks), 3):
    rucksack1, rucksack2, rucksack3 = (
        set(rucksacks[i]),
        set(rucksacks[i + 1]),
        set(rucksacks[i + 2]),
    )
    common_item = rucksack1.intersection(rucksack2).intersection(rucksack3).pop()
    priority_sum += get_priority(common_item)

print(f"part 2: {priority_sum}")
