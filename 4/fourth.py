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
        



# main
with open('./4/input.txt') as f:
        pairs = f.readlines()

part_one()