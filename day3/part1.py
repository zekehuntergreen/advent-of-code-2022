import string

rucksacks = open("input.txt", "r").read().splitlines()


def get_priority(common_item: str):
    return (string.ascii_lowercase + string.ascii_uppercase).index(common_item) + 1


priority_sum = 0
for rucksack in rucksacks:
    compartment1 = rucksack[: int(len(rucksack) / 2)]
    compartment2 = rucksack[int(len(rucksack) / 2) :]
    common_item = set(compartment1).intersection(set(compartment2)).pop()
    priority_sum += get_priority(common_item)

print(priority_sum)
