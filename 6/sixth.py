
def part_two():
    index = 13
    while index < len(sequence):
        new_set = set(sequence[index-13:index+1])
        if len(new_set) == 14:
            break
        index += 1

    print(index + 1)

def part_one():
    index = 3
    while index < len(sequence):
        new_set = set(sequence[index-3:index+1])
        if len(new_set) == 4:
            break
        index += 1
    
    print(index + 1)


# main
with open('./6/input.txt') as f:
        sequence = f.readlines()[0]

#part_one()
part_two()