# Greedy comparison
import sys

with open('./1/input.txt') as f:
        calories = f.readlines()

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