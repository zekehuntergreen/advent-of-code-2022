lines = open("input.txt", "r").read().splitlines()

num_fully_contained, num_overlap = 0, 0
for line in lines:
    print(line)
    elf1, elf2 = line.split(",")
    elf1_lower, elf1_upper, elf2_lower, elf2_upper = map(
        int, elf1.split("-") + elf2.split("-")
    )
    if (elf1_lower <= elf2_lower and elf1_upper >= elf2_upper) or (
        elf2_lower <= elf1_lower and elf2_upper >= elf1_upper
    ):
        num_fully_contained += 1
    if (elf1_lower <= elf2_lower and elf1_upper >= elf2_lower) or (
        elf1_lower >= elf2_lower and elf2_upper >= elf1_lower
    ):
        num_overlap += 1

print(f"{num_fully_contained} assignments fully contained by the other")
print(f"{num_overlap} overlap")
