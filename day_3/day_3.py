"""
Solutions to problems of day 3.

"""
common_elements = []
#
all_lines = []
#
badges = []

with open('./input.txt', 'r') as file:
    #
    for line in file:
        txt = line.strip()
        all_lines.append(txt) #part 2
        Ntxt = len(txt)
        # check
        if (Ntxt%2 != 0):
            raise RuntimeError("Number of characters are not divisible by 2!")
        #
        Nhalf = int(Ntxt/2)
        first_part = txt[0:Nhalf]
        second_part = txt[Nhalf:]
        # note: pop() gives an arbitrary element which is fine for us 
        el = set(first_part).intersection(second_part).pop()
        common_elements.append(el)
        
# part 2
for i in range(0,len(all_lines),3):
    #
    first_elf = all_lines[i + 0]
    second_elf = all_lines[i + 1]
    third_elf = all_lines[i + 2]
    #
    el = set(first_elf) & set(second_elf) & set(third_elf)
    badges.append(el.pop())

# order the letters and assign value
letters_dict = {}
#
for i in range(0,26):
    letters_dict[chr(97 + i)] = i+1
    letters_dict[chr(65 + i)] = i+27

# count the total of common lements in each rucksack
# part 1
common_values = [letters_dict[key]  for key in common_elements]
total = sum(common_values)
# value of badges, part 2
common_values = [letters_dict[key]  for key in badges]
total_badge = sum(common_values)
# count the total of badges
print(f'Total = {total}')
print(f'Total of badge = {total_badge}')



    

