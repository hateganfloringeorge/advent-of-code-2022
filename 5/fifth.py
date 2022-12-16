def part_one():

    #separate the picture and the instructions
    x = 0
    while (instructions[x] != '\n'):
        x += 1

    picture = instructions[:x]
    steps = instructions[x+1:]
    
    N = 9
    stacks = []

    # get all the current positions and put them in stacks going bottom up
    # parse the image by getting indexes of numbers then going up
    for i in range(N+1):
        stack = []
        index = picture[len(picture) - 1].find(str(i))
        if index != -1:
            for j in range(len(picture) - 2, -1, -1):
                if (picture[j][index] != ' '):
                    stack.append(picture[j][index])
        stacks.append(stack)
    

    # parse all of the movments and update the stacks
    for i in range(len(steps)):
        repetitions, from_stack, to_stack = [int(s) for s in steps[i].split() if s.isdigit()]
        
        # part one 
        # for j in range(repetitions):
        #     aux = stacks[from_stack].pop()
        #     stacks[to_stack].append(aux)

        # part two (probably easier with slicing in python but I am a .NET dev ^^ )
        aux_stack = []
        for j in range(repetitions):
            aux = stacks[from_stack].pop()
            aux_stack.append(aux)

        for j in range(repetitions):
            aux = aux_stack.pop()
            stacks[to_stack].append(aux)    

    print(stacks)
    # get the tops from all of the stacks
    final_word = ''
    for i in range(1, N+1):
        final_word += stacks[i].pop()
    print(final_word)

    pass

# main
with open('./5/input.txt') as f:
        instructions = f.readlines()

part_one()