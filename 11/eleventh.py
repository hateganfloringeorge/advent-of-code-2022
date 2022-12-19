class Monkey:
    def __init__(self, index, items, todo, todo_nr, div_by, good, bad):
        self.index = index
        self.items = items
        self.todo = todo
        self.todo_nr = todo_nr
        self.div_by = div_by
        self.good = good
        self.bad = bad


def part_one():

    # parsing
    monkeys = []    
    i = 0
    while i < len(notes):

        if "Monkey" in notes[i]:
            # index
            index = int(notes[i].strip("Monkey :"))
            i += 1

            # starting items
            items = notes[i].strip("Starting items: ").split(',')
            items = [eval(i) for i in items]
            i += 1

            # operations
            # parsing is the hardest part
            elements = notes[i].strip("Operation: new = old ").split(" ")
            
            op_number = ""
            operation = elements[0]
            if (len(elements) == 2):
                 op_number = int(elements[1])
            
            i += 1

            # division
            div_number = int(notes[i].strip("Test: divisible by "))
            i += 1

            # if true
            true_index = int(notes[i].strip("If true: throw to monkey "))
            i += 1

            # if false
            false_index = int(notes[i].strip("If false: throw to monkey "))
            
            new_monkey = Monkey(index, items, operation, op_number, 
                                div_number, true_index, false_index)

            monkeys.append(new_monkey)
        
        i += 1

    # compute result
    rounds_count = 20
    inspections = [0] * len(monkeys)

    for i in range(rounds_count):
        for j in range(len(monkeys)):
            monkey = monkeys[j]
            inspections[j] += len(monkey.items)

            while len(monkey.items) > 0:
                # take item
                item = monkey.items.pop(0)

                # do operation
                op_number = 0
                if monkey.todo_nr == "":
                    op_number = item
                else:
                    op_number = monkey.todo_nr

                if monkey.todo == "*":
                    item *= op_number
                else:
                    item += op_number

                # divide by 3
                item //= 3

                # check division
                div_result = (item % monkey.div_by) == 0

                # send it to next monkey
                if div_result:
                    monkeys[monkey.good].items.append(item)
                else:
                    monkeys[monkey.bad].items.append(item)
             

    print(inspections)
    first_max = max(inspections)
    inspections.remove(first_max)
    second_max = max(inspections)
    #print(str(first_max) + " " + str(second_max))
    print(first_max * second_max)

# main
with open('./11/input.txt') as f:
        notes = f.readlines()

notes = [s.strip() for s in notes]

part_one()