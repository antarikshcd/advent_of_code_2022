"""
This script counts the input spearated by blanks and identifies the elf carrying the most.

"""

file = 'input.txt'
cal_dict = {}
cal = 0
# prev_cal = 0
elf_cnt = 0
# max_cal = 0
#
with open(file, 'r') as f:
    # f is iterable
    for i, line in enumerate(f):
        txt = line.strip() # strip removes the new line character
        # if a whitespace then we bump to the next elf
        if len(txt) == 0:
            # we finished counting the elf, bump the counter
            elf_cnt += 1
            #
            # max_cal = max(max_cal, prev_cal)
            # store the total calories in the dict
            cal_dict[elf_cnt] = cal
            #
            # prev_cal = cal
            # reset the calorie counter
            cal = 0
            #
        else:
            # calorie counter
            cal = cal + int(txt)

   
# verification
print(f'Max calories = {max(cal_dict.values())}')

# --------part 2 -------------
cal_list = list(cal_dict.values())
cal_list.sort() 
#
Ncal = len(cal_list)
tot_cal = sum(cal_list[Ncal-3:])
print(f'Calories carried by top three elves = {tot_cal}')