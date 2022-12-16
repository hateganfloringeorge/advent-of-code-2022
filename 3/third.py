
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

# main
with open('./3/input.txt') as f:
        bags = f.readlines()

part_one()