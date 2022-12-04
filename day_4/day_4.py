"""
Solutions to problems of day 4
"""
elf1_in_elf2 = []
elf2_in_elf1 = []
disjoint_pairs = []
with open('./input.txt', 'r') as file:
    #
    for line in file:
        txt = line.strip()
        # we split the file around the commas
        txt_elves = txt.split(',')
        # print(txt_elves)
        # get range of numbers for each elf
        elf_1 = txt_elves[0].split('-')
        elf_2 = txt_elves[1].split('-')
        #print(elf_1)
        # get range
        elf1_lower = int(elf_1[0])
        elf1_upper = int(elf_1[1])
        #
        elf2_lower = int(elf_2[0])
        elf2_upper = int(elf_2[1])
        #print(elf2_uppe
        elf1_range = set(range(elf1_lower, elf1_upper + 1))
        elf2_range = set(range(elf2_lower, elf2_upper + 1))
        #
        # test for membership
        # need toa void the case where the sets are aequal, to be counted once
        elf1_in_elf2.append(elf1_range <= elf2_range)
        elf2_in_elf1.append(elf2_range < elf1_range)
        # part 2
        disjoint_pairs.append(elf1_range.isdisjoint(elf2_range))    

# count         
count_1 = elf1_in_elf2.count(True)
count_2 = elf2_in_elf1.count(True)
total_count = count_1 + count_2
# part 2
count_overlap = disjoint_pairs.count(False)
#
print(f'Number of pairs with one range in other = {total_count}')
# part 2
print(f'Number of pairs with overlap = {count_overlap}')