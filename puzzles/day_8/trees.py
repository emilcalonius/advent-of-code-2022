#-------------------------------------- PART 1. ------------------------------------------------
def is_visible(trees_list, row_idx, tree_idx):
    if row_idx == 0 or row_idx == len(trees_list) - 1:
        return True

    if tree_idx == 0 or tree_idx == len(trees_list[row_idx])-1:
        return True

    if (max(trees_list[row_idx][:tree_idx]) < trees_list[row_idx][tree_idx] 
    or max(trees_list[row_idx][tree_idx+1:]) < trees_list[row_idx][tree_idx]):
        return True

    column = []
    for row in trees_list:
        column.append(row[tree_idx])
    
    if max(column[:row_idx]) < column[row_idx] or max(column[row_idx+1:]) < column[row_idx]:
        return True
    
    return False

#------------------------------------- PART 2. ---------------------------------------------------
def calculate_scenic_score(trees_list, row_idx, tree_idx):
    left = 0
    if tree_idx > 0:
        for tree in reversed(trees_list[row_idx][:tree_idx]):
            if tree >= trees_list[row_idx][tree_idx]:
                left += 1
                break
            left += 1

    right = 0
    if tree_idx < len(trees_list[row_idx]) - 1:
        for tree in trees_list[row_idx][tree_idx+1:]:
            if tree >= trees_list[row_idx][tree_idx]:
                right += 1
                break
            right += 1

    column = []
    for row in trees_list:
        column.append(row[tree_idx])

    up = 0
    if row_idx > 0:
        for tree in reversed(column[:row_idx]):
            if tree >= trees_list[row_idx][tree_idx]:
                up += 1
                break
            up += 1

    down = 0
    if row_idx < len(trees_list) - 1:
        for tree in column[row_idx+1:]:
            if tree >= trees_list[row_idx][tree_idx]:
                down += 1
                break
            down += 1

    return left * right * up * down
        

with open("map.txt", "r") as file:
    trees = []
    for line in file:
        line = line.rstrip("\n")
        trees.append([*line])

    num_visible = 0
    max_scenic_score = 0
    height = len(trees)
    width = len(trees[0])
    for i in range(len(trees)):
        for j in range(len(trees[i])):
            if is_visible(trees, i, j):
                num_visible += 1

            scenic_score = calculate_scenic_score(trees, i, j)
            if scenic_score > max_scenic_score:
                max_scenic_score = scenic_score

    print("Visible trees from outside:")
    print(num_visible)
    print("Max scenic score for all trees:")
    print(max_scenic_score)