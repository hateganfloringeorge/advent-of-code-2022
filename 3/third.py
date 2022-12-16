
def get_priority(char):
    number = ord(char)
    if (number > 90):
        return number - 96
    else:
        return number - 64 + 26

def part_one():

    priority_sum = 0

    for i in range(len(bags)):
        current_bags = bags[i]
        firstpart, secondpart = current_bags[:len(current_bags)//2], current_bags[len(current_bags)//2:]

        charDict = {}
        for j in range(len(firstpart)):
            charDict[firstpart[j]] = 1
        
        k = 0
        while True:
            if secondpart[k] in charDict:
                priority_sum += get_priority(secondpart[k])
                break
            k += 1

    print(priority_sum)


def part_two():

    priority_sum = 0
    for i in range(len(bags)//3):

        first_bag = bags[i*3]
        second_bag = bags[i*3 + 1]
        third_bag = bags[i*3 + 2]

        charDict = {}

        # add only one (could have ignored it if duplicate) 
        for j in range(len(first_bag)):
            charDict[first_bag[j]] = 1
        
        # set to two only for already present chars
        for j in range(len(second_bag)):
            if second_bag[j] in charDict:
                charDict[second_bag[j]] = 2
        
        j = 0
        while True:
            if third_bag[j] in charDict and charDict[third_bag[j]] == 2:
                priority_sum += get_priority(third_bag[j])
                break
            j += 1
        
        charDict.clear()

    print(priority_sum)

# main
with open('./3/input.txt') as f:
        bags = f.readlines()

#part_one()
part_two()