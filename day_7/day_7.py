"""
Solutions to day 7
"""
size_limit = 100000
data = []
with open('./input.txt', 'r') as file:
    #
    for line in file:
        line_strip = line.strip()
        data.append(line_strip.split(" "))
#
# store the directory files
# directory:dict
#
change_dir = False
size_dict = {}
# every directory is being cd'd once
for line in data:
    # issue a cmd
    if line[0] == '$' and line[1] == 'cd':
        if line[2] == '/':
            cwd = "/"
            pwd = []
        elif line[2] == '..':
            cwd = pwd.pop()
            # print(prev_dir)
        else:
            #pwd.append(line[2])
            pwd.append(cwd)
            cwd = cwd + "/" + line[2]
            # cwd = line[2]
            #size_dict[line[2]] = 0 
    elif line[0] == '$' and line[1] == 'ls':
        pass
    elif line[0] == 'dir':
        pass
    elif line[0].isdigit():
        # size_dict[cwd] = int(line[0])
        #
        if cwd in size_dict:
            size_dict[cwd] += int(line[0])
        else:
            size_dict[cwd] = int(line[0])     
        #
        for dir in pwd:
          if dir in size_dict.keys():      
              size_dict[dir] += int(line[0])
          else:
              size_dict[dir] = int(line[0])     


# print(size_dict)
sum = 0
for key,value in size_dict.items():
    # print(key, value)
    if value <= size_limit:
        sum = sum + value

print(sum)       
# part 2
required_size = 30000000 - (70000000 - size_dict['/'])
#print(required_size)
sufficient_space = []
for size in size_dict.values():
    if size >= required_size:
        sufficient_space.append(size)
#
print(min(sufficient_space))        
 