import copy

def print_nicely(drawing):
    for data in drawing:
        print(''.join(data))

def clear_map(first_time = False):
    global drawing, empty_drawing
    if first_time:
        for i in range(len(drawing)):
            for j in range(len(drawing[0])):
                if drawing[i][j] != '#':
                    drawing[i][j] = '.'
    else:
        drawing = copy.deepcopy(empty_drawing)

def move_blizzards():
    global going_up, going_right, going_down, going_left, drawing
    aux = []
    new_row = 0
    new_col = 0
    for (row, col) in going_down:
        if drawing[row + 1][col] == '#':
            new_row = 2
        else:
            new_row = row + 1
        aux.append((new_row, col))
        drawing[new_row][col] = 'v'
        
    going_down = copy.deepcopy(aux)
    aux.clear()
    
    
    for (row, col) in going_up:
        if drawing[row - 1][col] == '#':
            new_row = len(drawing) - 3
        else:
            new_row = row - 1
        aux.append((new_row, col))
        drawing[new_row][col] = '^'
    
    going_up = copy.deepcopy(aux)
    aux.clear()

    for (row, col) in going_left:
        if drawing[row][col - 1] == '#':
            new_col = len(drawing[0]) - 2
        else:
            new_col = col - 1
        aux.append((row, new_col))
        drawing[row][new_col] = '<'
    
    going_left = copy.deepcopy(aux)
    aux.clear()

    for (row, col) in going_right:
        if drawing[row][col + 1] == '#':
            new_col = 1
        else:
            new_col = col + 1
        aux.append((row, new_col))
        drawing[row][new_col] = '>'
    
    going_right = copy.deepcopy(aux)
    aux.clear()


def compute_possible_positions():
    global drawing, positions, directions
    next_positions = set()
    for (row, col) in positions:
        for (offset_row, offset_col) in directions:
            if drawing[row + offset_row][col + offset_col] == '.':
                next_positions.add((row + offset_row, col + offset_col))
            elif drawing[row + offset_row][col + offset_col] == 'F':
                return True
    
    positions = next_positions
    return False

def part_one():
    global drawing, empty_drawing, positions
    protection = '#' * len(drawing[0])
    drawing.append(protection)
    drawing.insert(0, protection)
    
    for i in range(len(drawing)):
        drawing[i] = [*drawing[i]]
    
    # save torndaos and clean map
    for i in range(len(drawing)):
        for j in range(len(drawing[0])):
            if drawing[i][j] != '#' and drawing[i][j] != '.':
                
                if drawing[i][j] == '>':
                    going_right.append((i,j))
                elif drawing[i][j] == '<':
                    going_left.append((i,j))
                elif drawing[i][j] == '^':
                    going_up.append((i,j))
                elif drawing[i][j] == 'v':
                    going_down.append((i,j))
                
    clear_map(True)
    drawing[len(drawing) - 2][len(drawing[0]) - 2] = "F"
    empty_drawing = copy.deepcopy(drawing)
    start_row = 2
    start_col = 1

    positions.add((start_row, start_col))
    steps = 0
    while True:
        steps += 1
        move_blizzards()
        #print_nicely(drawing)
        if compute_possible_positions():
            break
        clear_map()

    print(steps)
        

# main
with open('./24/input.txt') as f:
        drawing = f.readlines()

drawing = [s.strip() for s in drawing]
going_up = []
going_down = []
going_left = []
going_right = []
empty_drawing = []
positions = set()
directions = [(0, 0), (0, 1), (0, -1), (-1, 0), (1, 0)]
part_one()

