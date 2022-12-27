

def print_screen():
    for row in screen:
        print("".join(row))
    print()


def make_boundry():
    width = len(screen[0])
    for i in range(len(screen)):
        for j in range(width):
            if j == 0 or j == width-1 or i == len(screen)-1:
                screen[i][j] = '#'


def is_valid_position(i: int, j: int, offsets):
    for (off_i, off_j) in offsets:
        if screen[off_i + i][off_j + j] == '#':
            return False
    return True


def put_on_screen(i: int, j: int, offsets):
    for (off_i, off_j) in offsets:
        screen[off_i + i][off_j + j] = '#'


def get_new_lvl(lowest: int):
    start = 1
    end = 8
    isLowest = True
    while isLowest:
        isLowest = False
        for j in range(start, end):
            if screen[lowest][j] == '#':
                lowest -= 1
                isLowest = True
    return lowest



def part_one():

    make_boundry()
    #print_screen()
    lowest_lvl = len(screen) - 2
    left_start = 3
    jet_count = 0

    for k in range(2022):
        # general starting position
        i = lowest_lvl - 3
        j = left_start
        
        shape = shapes_list[k % 5]
        
        while True:
            direction = jets[jet_count]
            if direction == '>' and is_valid_position(i, j+1, shape):
                j += 1
            elif direction == '<' and is_valid_position(i, j-1, shape):
                j -= 1

            jet_count = (jet_count + 1) % len(jets)    
            
            if is_valid_position(i+1, j, shape):
                i += 1
            else:
                break
        

        put_on_screen(i, j, shape)
        # adjust lowest_level
        lowest_lvl = get_new_lvl(lowest_lvl)
        #print(lowest_lvl)
        #print_screen()
    print(len(screen) - lowest_lvl - 2)



# main
with open('./17/input.txt') as f:
        jets = f.readlines()

jets = jets[0].strip()
screen = [['.' for i in range(9)]
# TODO change back to 5260
                    for j in range(5260)]

minus = [(0,0), (0,1), (0,2), (0,3)]
plus = [(0,1), (-1,0), (-1,1), (-2,1), (-1, 2)]
L = [(0,0), (0,1), (0,2), (-1,2), (-2,2)]
I = [(0,0), (-1,0), (-2,0), (-3,0)]
square = [(0,0), (0,1), (-1,0), (-1,1)]

shapes_list = [minus, plus, L, I, square]
part_one()