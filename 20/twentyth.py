import copy
from typing import List

# damn duplicates
# def part_one():

    # v = copy.deepcopy(numbers)
    # print(v)
    # for i in range(len(numbers)):
    #     new_number = numbers[i]
    #     index = v.index(new_number)
    #     v.remove(new_number)

    #     # if (index + numbers[i]) % len(numbers) == 0:
    #     #     v.append(numbers[i])
    #     # else:
    #     v.insert((index + numbers[i]) % len(v), numbers[i])
    #     #print(v)

    # start = v.index(0)
    # total_sum = 0
    # for i in range(1, 4):
    #     total_sum += v[(start + i*1000) % len(numbers)]
    
    # print(total_sum)


class Node:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None

class CircularList:
    def __init__(self, zero_index: int, nodes: List[Node]):
        self.nodes = nodes
        self.zero_index = zero_index
        for i in range(len(nodes)):
            self.nodes[i].left = self.nodes[i-1]
            self.nodes[i].right = self.nodes[(i + 1)% len(nodes)]

    def __str__(self):
        v = []
        head = self.nodes[0]
        for i in range(len(self.nodes)):
            v.append(head.value)
            head = head.right
        return str(v)

    def compute_sum(self):
        total_sum = 0
        node = self.nodes[self.zero_index]
        for i in range(3):
            for i in range(1000):
                node = node.right
            total_sum += node.value
        
        return total_sum
        
def mixing(c: CircularList, times: int):
    for k in range(times):
        for i in range(len(numbers)):
            if c.nodes[i].value == 0:
                continue

            # get current node
            node = c.nodes[i]
            move = node.value % (len(numbers) - 1)

            # remove neighbours ties
            (c.nodes[i].left).right = c.nodes[i].right
            (c.nodes[i].right).left = c.nodes[i].left

            if move > 0:
                # go right
                iter_node = node.right
                move -= 1

                while move > 0:
                    iter_node = iter_node.right
                    move -= 1
                
                # change node
                c.nodes[i].left = iter_node
                c.nodes[i].right = iter_node.right

                # change new neighbours
                (iter_node.right).left = c.nodes[i]
                iter_node.right = c.nodes[i]

            else:

                # go left
                iter_node = node.left
                move += 1

                while move < 0:
                    iter_node = iter_node.left
                    move += 1

                # change node
                c.nodes[i].right = iter_node
                c.nodes[i].left = iter_node.left

                # change new neighbours
                (iter_node.left).right = c.nodes[i]
                iter_node.left = c.nodes[i]

def part_one():

    l = []
    zero_index = 0
    for i in range(len(numbers)):
        l.append(Node(numbers[i]))
        if numbers[i] == 0:
            zero_index = i
    c = CircularList(zero_index, l)
    mixing(c, 1)
    print(c.compute_sum())

def part_two(): 
    l = []
    zero_index = 0
    for i in range(len(numbers)):
        l.append(Node(numbers[i] * 811589153))
        if numbers[i] == 0:
            zero_index = i
    c = CircularList(zero_index, l)
    mixing(c, 10)
    print(c.compute_sum())

# main
with open('./20/input.txt') as f:
        numbers = f.readlines()

numbers = [eval(s.strip()) for s in numbers]

#part_one()
part_two()
