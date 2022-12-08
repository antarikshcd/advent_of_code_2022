"""
Solutions to day 8
"""
import copy
data = []
with open('./input.txt', 'r') as file:
    #
    for line in file:
        line_strip = line.strip()
        #
        r = [int(x) for x in line_strip]
        #
        data.append(r)

#
# store in column major
Nrows = len(data)
Ncols = len(data[0])
#
def is_tree_visible(row, col):
    """
    The tree in consideration is visible if and only if
    the chosen tree is the tallest between it and the edge
    (including the dge).
    - When it is visible from all sides, it is visible.
    - If it is on the edge then it is visible as well.
    - the trees have to be counted from the tree and outwards
      otherwise we may count a smaller tree at the dge that is visible
      when in reality it isnt
    """
    tree = data[row][col]
    # check left of tree
    for i in range(col-1,-1,-1):
        if data[row][i] >= tree:
            break
    else:
        return 1    
    # check right of tree
    for i in range(col+1, Ncols):
        if data[row][i] >= tree:
            break
    else:
        return 1    
    # check top of tree
    for i in range(row-1,-1,-1):
        if data[i][col] >= tree:
            break
    else:
        return 1    
    # check bottom of tree
    for i in range(row+1, Nrows):
        if data[i][col] >= tree:
            break
    else:
        return 1    

    return 0        

def scenic_tree_score(row, col):
    """

    """
    tree = data[row][col]
    # check left of tree
    total_score = 1
    count = 0
    for i in range(col-1,-1,-1):
        if data[row][i] >= tree:
            count += 1
            break
        else:
            count += 1
    total_score *= count
    # reset
    count = 0
    # right of tree
    for i in range(col+1, Ncols):
        if data[row][i] >= tree:
            count += 1 
            break
        else:
            count += 1    
    total_score *= count
    # reset
    count = 0            
    # check top of tree
    for i in range(row-1,-1,-1):
        if data[i][col] >= tree:
            count += 1 
            break
        else:
            count += 1
    total_score *= count
    # reset
    count = 0                   
    # check bottom of tree
    for i in range(row+1, Nrows):
        if data[i][col] >= tree:
            count += 1 
            break
        else:
            count += 1     
    total_score *= count

    return total_score  
  
# how many trees on the edge
visible_trees = Ncols * 2 + (Nrows - 2) * 2
#
score = 0
for row in range(1, Nrows-1):
    for col in range(1, Ncols-1):
        if is_tree_visible(row, col):
            visible_trees += 1
        #
        score = max(score, scenic_tree_score(row, col))     


#   
print(visible_trees)
print(score)