
class Node:
    def __init__(self, name: str, isNumber: bool, number: int, operation: str, first_operand:str, second_operand:str):
        self.str = name
        self.isNumber = isNumber
        self.number = number
        self.operation = operation
        self.first = first_operand
        self.second = second_operand
    
    def get_value(self):
        if self.isNumber:
            return self.number
        
        value1 = node_dict[self.first].get_value()
        value2 = node_dict[self.second].get_value()
        
        if self.operation == '+':
            return value1 + value2
        elif self.operation == '*':
            return value1 * value2
        elif self.operation == '-':
            return value1 - value2
        else:
            return value1 / value2



def part_one():
    for i in range(len(shouting)):
        name, values = shouting[i].split(':')
        tokens = values[1:].split(' ')
        if (len(tokens) <= 2):
            number = eval(tokens[0])
            node_dict[name] = Node(name, True, number, None, None, None)
        else:
            node_dict[name] = Node(name, False, None, tokens[1], tokens[0], tokens[2])

    root_value = node_dict['root'].get_value()
    print(root_value)

# main
with open('./21/input.txt') as f:
        shouting = f.readlines()

shouting = [s.strip() for s in shouting]
node_dict = {}

part_one()