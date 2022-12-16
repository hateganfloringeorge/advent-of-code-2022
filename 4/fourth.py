def part_one():
    
    total_pairs = 0
    for i in range(len(pairs)):

        #extract numbers
        pair = pairs[i]
        first, second = pair.split(',')
        first_min, first_max = list(map(int,first.split('-')))
        second_min, second_max = list(map(int, second.split('-')))

        if (first_min == second_min or first_max == second_max):
            total_pairs += 1
            continue

        if (first_min < second_min and second_max < first_max):
            total_pairs += 1
            continue

        if (second_min < first_min and first_max < second_max):
            total_pairs += 1
            continue
    
    print(total_pairs)
        

def part_two():
    
    total_pairs = 0
    for i in range(len(pairs)):

        #extract numbers
        pair = pairs[i]
        first, second = pair.split(',')
        first_min, first_max = list(map(int,first.split('-')))
        second_min, second_max = list(map(int, second.split('-')))

        # skip all pairs with at least one common number
        if (first_min == second_min or first_max == second_max or 
            first_min == second_max or second_min == first_max):
            continue

        if (first_max < second_min or first_min > second_max):
            total_pairs += 1
            continue
    
    print(len(pairs) - total_pairs)


# main
with open('./4/input.txt') as f:
        pairs = f.readlines()

#part_one()
part_two()