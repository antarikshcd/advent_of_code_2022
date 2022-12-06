"""
Solutions to day 6
"""
def get_slice(char, limit, lst = []):
    """
    """
    # lst = []
    if len(lst) < limit:
        lst.append(char)
    else:
        lst.pop(0)
        lst.append(char)

    return lst        

def get_count(lst):
    """
    """
    cnt_lst = []
    for char in lst:
        cnt = lst.count(char)
        cnt_lst.append(cnt)

    return cnt_lst

def get_pos(lst, limit, global_cnt):
    """
    """
    if lst.count(1) == limit and global_cnt >= limit:
        return global_cnt, False
    else:
        return 0, True    

code_lst = []
msg_lst = []
cnt = 0
flag = 1
flag_part1 = True
flag_part2 = True
with open('./input.txt', 'r') as file:
    
    while flag:
        letter = file.read(1)          
        if not letter or letter=='\n':
            break
        else:
            cnt += 1
            #
            code_lst = get_slice(letter, 4, code_lst)
            msg_lst = get_slice(letter, 14, msg_lst)
            # #
            cnt_charlst = get_count(code_lst)
            # part 1
            if flag_part1:
                pos_part1, flag_part1 = get_pos(cnt_charlst, 4, cnt)

            # part 2
            cnt_msglst = get_count(msg_lst)
            # part 2
            if flag_part2:
                pos_part2, flag_part2 = get_pos(cnt_msglst, 14, cnt)


print(f'Part 1 position = {pos_part1}')
print(f'Part 2 position = {pos_part2}')
