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


def compute_possible_positions(finish):
    global drawing, positions, directions
    next_positions = set()
    for (row, col) in positions:
        for (offset_row, offset_col) in directions:
            if drawing[row + offset_row][col + offset_col] in ['.', 'F', 'S']:
                if drawing[row + offset_row][col + offset_col] == finish:
                    return True
                else:
                    next_positions.add((row + offset_row, col + offset_col))
            
    
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

    start_row = 1
    start_col = 1
    finish_row = len(drawing) - 2
    finish_col = len(drawing[0]) - 2
    clear_map(True)
    drawing[finish_row][finish_col] = "F"
    drawing[start_row][start_col] = "S"
    #print_nicely(drawing)
    empty_drawing = copy.deepcopy(drawing)


    positions.add((start_row, start_col))
    steps = 0
    for i in range(3):
        looking_for = ''
        if i % 2 == 0:
            positions = {(start_row, start_col)}
            looking_for = 'F'
        else:
            positions = {(finish_row, finish_col)}
            looking_for = 'S'


        while True:
            steps += 1
            move_blizzards()
            #print_nicely(drawing)
            if compute_possible_positions(looking_for):
                break
            clear_map()
        print(steps)
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

