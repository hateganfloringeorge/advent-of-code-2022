import ast

def is_correct_order(left, right):

    # both integers
    if isinstance(left, int) and isinstance(right, int):
        if left == right:
            return 0
        elif left < right:
            return 1
        else:
            return -1
    
    # adjust to list if needed
    if isinstance(left, list) and isinstance(right, int):
        right = [right]
    elif isinstance(left, int) and isinstance(right, list):
        left = [left]
    
    # compare lists

    # edge cases
    if not left and not right:
        return 0

    if not left and right:
        return 1

    if left and not right:
        return -1

    left_len = len(left)
    right_len = len(right)
    for i in range(min(left_len, right_len)):
        result = is_correct_order(left[i], right[i])
        if result != 0:
            return result
        
    
    if left_len == right_len:
        return 0

    if left_len > right_len:
        return -1
    return 1

def part_one():
    
    total_sum = 0
    for i in range(0, len(pairs), 3):
        print(i)
        left = ast.literal_eval(pairs[i])
        right = ast.literal_eval(pairs[i+1])
        if is_correct_order(left, right) != -1:
            total_sum += i // 3 + 1
        print(is_correct_order(left, right))

    print(total_sum)


# main
with open('./13/input.txt') as f:
        pairs = f.readlines()

pairs = [s.strip() for s in pairs]
right_order_pairs = [False for j in range((len(pairs) + 1)//3)]

part_one()