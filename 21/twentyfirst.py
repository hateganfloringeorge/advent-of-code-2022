
class Node:
    def __init__(self, name: str, isNumber: bool, number: int, operation: str, first_operand:str, second_operand:str):
        self.name = name
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
    
    def check_humn(self):
        if self.isNumber:
            if self.name == "humn":
                return True
            return False
        
        return node_dict[self.first].check_humn() or node_dict[self.second].check_humn()



def part_one():
    for i in range(len(shouting)):
        name, values = shouting[i].split(':')
        tokens = values[1:].split(' ')
        if (len(tokens) <= 2):
            number = eval(tokens[0])
            node_dict[name] = Node(name, True, number, None, None, None)
        else:
            node_dict[name] = Node(name, False, None, tokens[1], tokens[0], tokens[2])

    # part one
    # root_value = node_dict['root'].get_value()
    # print(root_value)

    # part two
    node = node_dict['root']
    result = 0

    print(node_dict[node.second].check_humn())
    #compute the result and then reverse operations just as in any ecuation
    if node_dict[node.first].check_humn():
        result = node_dict[node.second].get_value()
        node = node_dict[node.first]
    else:
        result = node_dict[node.first].get_value()
        node = node_dict[node.second]
    
    while node.name != 'humn':
        other_value = 0
        if node_dict[node.first].check_humn():
            other_value = node_dict[node.second].get_value()
            aux_node = node_dict[node.first]
        else:
            other_value = node_dict[node.first].get_value()
            aux_node = node_dict[node.second]

        if node.operation == '+':
            result -= other_value
        elif node.operation == '*':
            result /= other_value
        elif node.operation == '-':
            if aux_node.name == node_dict[node.second].name:
                result = other_value - result
            else:
                result += other_value
        else:
            if aux_node.name == node_dict[node.second].name:
                result = other_value / result
            else:
                result *= other_value
        
        node = aux_node
    
    print(result)


# main
with open('./21/input.txt') as f:
        shouting = f.readlines()

shouting = [s.strip() for s in shouting]
node_dict = {}

part_one()