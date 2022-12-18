
def part_one():
    
    signals_sum = 0
    important_cycles = [20, 60, 100, 140, 180, 220]
    i = 1 
    j = 0
    x = 1

    while i <= 220:
        
        if "noop" == instructions[j]:
            i += 1
        
        else:
            i += 1
            if (i % 20 == 0) and (i in important_cycles):
                signals_sum += i * x
            x += int(instructions[j][5:])
            i += 1

        if (i % 20 == 0) and (i in important_cycles):
            signals_sum += i * x

        j += 1

    print(signals_sum)

def part_two():

    important_cycles = [20, 60, 100, 140, 180, 220]
    i = 0
    j = 0
    x = 1
    image = ""

    while i < 240:
        
        if "noop" == instructions[j]:
            if abs(x - i % 40) < 2:
                image += "#"
            else:
                image += "."
            i += 1
            
        else:
            if abs(x - i % 40) < 2:
                image += "#"
            else:
                image += "."
            i += 1

            if (i % 40 == 0):
                image += '\n'
            
            if i >= 240:
                break

            if abs(x - i % 40) < 2:
                image += "#"
            else:
                image += "."

            x += int(instructions[j][5:])
            i += 1

        if (i % 40 == 0):
            image += '\n'

        j += 1

    print(image)

# main
with open('./10/input.txt') as f:
        instructions = f.readlines()

instructions = [s.strip() for s in instructions]

part_two()