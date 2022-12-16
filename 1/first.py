# Greedy comparison
import sys

def part_one():
    biggest_num = 0
    partial_sum = 0

    #just iterate and compare biggest_num with partial sum when newline
    for i in range(len(calories)):

        if (calories[i] == '\n'):
            if (partial_sum > biggest_num):
                biggest_num = partial_sum
            partial_sum = 0

        else:
            value = int(calories[i])
            partial_sum += value

    # compare with the latest partial sum
    if (partial_sum > biggest_num):
        biggest_num = partial_sum

    print(biggest_num)

# same as part one but this time keep a list and compare the minimum
def part_two():
    
    biggest_3 = [0, 1, 2]
    partial_sum = 0

    #just iterate and compare biggest_num with partial sum when newline
    for i in range(len(calories)):

        if (calories[i] == '\n'):
            min_value = min(biggest_3)
            if (partial_sum > min_value):
                biggest_3.remove(min_value)
                biggest_3.append(partial_sum)
            partial_sum = 0

        else:
            value = int(calories[i])
            partial_sum += value

    # compare with the latest partial sum
    min_value = min(biggest_3)
    if (partial_sum > min_value):
        biggest_3.remove(min_value)
        biggest_3.append(partial_sum)

    print(biggest_3)
    print(sum(biggest_3))
    pass

with open('./1/input.txt') as f:
        calories = f.readlines()

#part_one()
part_two()