"""
Solutions to problems of day 5
"""
import copy

lines = []
lines_crates = []
lines_cmds = []
flag_cmds = 0
with open('./input.txt', 'r') as file:
    #
    for line in file:
        txt = line.splitlines()
        if txt[0] == '':
            flag_cmds = 1
            continue
        #    
        if flag_cmds == 0:
            lines_crates.append(txt)
        else:    
            lines_cmds.append(txt)
#
crates_lst = [[],[],[],[],[],[],[],[],[]]
for i in range(len(lines_crates) - 1):
    line = lines_crates[i]
    # split at space: four empty strings equals one crate
    split_line = line[0].split(" ")
    # 
    count = 0
    count_gl = 0
    row_lst = []
    row_dict = {}
    for char in split_line:
        if char == '':
            count = count + 1
        else:
            # index
            ind = int(count/4) + 1
            count_gl += ind
            count = 0
            #
            crates_lst[count_gl-1].append(char)
            row_lst.append(char)        
#
crates_qty = []
from_crate = []
to_crate = []
for line in lines_cmds:
    split_line = line[0].split(" ")
    crates_qty.append(int(split_line[1]))
    from_crate.append(int(split_line[3]))
    to_crate.append(int(split_line[5]))  
#
#
crates_lst2 = copy.deepcopy(crates_lst)
N_ops = len(crates_qty)
for i in range(N_ops):
    qty = crates_qty[i]
    from_ind = from_crate[i] - 1
    to_ind = to_crate[i] - 1
    #
    remove_lst = []
    for j in range(qty):
        # store the element being removed
        remove = crates_lst[from_ind][0]
        # delete the old element
        crates_lst[from_ind].pop(0)
        # insert it at the start of the new list
        crates_lst[to_ind].insert(0, remove)
        # part 2
        remove = crates_lst2[from_ind][0]
        crates_lst2[from_ind].pop(0) 
        crates_lst2[to_ind].insert(j, remove)
#print(crates_lst)
print('part 1: \n')
for lst in crates_lst:
    print(lst[0], end="")
print("\n")
print('part 2: \n')
for lst in crates_lst2:
    print(lst[0], end="")
print("\n")    