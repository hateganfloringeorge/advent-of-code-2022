
def part_one():

    x = 0
    y = 0
    offset_x = 0
    offset_y = 0
    positions = {(0,0)}

    for i in range(len(moves)):
        direction, steps = moves[i].split(" ")
        steps = int(steps)

        for j in range(steps):
            if direction == 'R':
                x += 1
                offset_x -= 1

            if direction == 'L':
                x -= 1
                offset_x += 1

            if direction == 'D':
                y -= 1
                offset_y += 1

            if direction == 'U':
                y += 1
                offset_y -= 1

            if abs(offset_y) > 1 or abs(offset_x) > 1:
                # I cheat by dividing by two in order not to care about sign
                # is the same as moving one square in that direction

                if offset_x == 0 or offset_y == 0:
                    # move horizontally
                    if offset_x != 0:
                        offset_x //= 2
                    
                    if offset_y != 0:
                        offset_y //= 2
                
                else:
                    # move diagonally
                    if abs(offset_x) == 1:
                        offset_x = 0
                        offset_y //= 2
                    
                    else:
                        offset_y = 0
                        offset_x //= 2
                
                # add position to dictionary
                positions.add((x + offset_x, y + offset_y))
                

    print(len(positions))

def part_two():

    N = 10
    x_pos = [0] * N
    y_pos = [0] * N
    positions = {(0,0)}

    for i in range(len(moves)):
        direction, steps = moves[i].split(" ")
        steps = int(steps)

        for j in range(steps):
            if direction == 'R':
                x_pos[0] += 1

            if direction == 'L':
                x_pos[0] -= 1

            if direction == 'D':
                y_pos[0] -= 1

            if direction == 'U':
                y_pos[0] += 1

            # iterate through all positions to see the ripple effect
            k = 0
            while k < N - 1 and (abs(x_pos[k] - x_pos[k+1]) > 1 
                                    or abs(y_pos[k] - y_pos[k+1]) > 1):

                offset_x = x_pos[k + 1] - x_pos[k]
                offset_y = y_pos[k + 1] - y_pos[k]
                                
                if offset_x == 0 or offset_y == 0:
                    # move horizontally
                    if offset_x != 0:
                        offset_x //= 2
                    
                    if offset_y != 0:
                        offset_y //= 2

                #add the case when moving diagonally twice
                elif abs(offset_x) == 2 and abs(offset_y) == 2:
                    offset_y //= 2
                    offset_x //= 2

                else:
                    # move diagonally
                    if abs(offset_x) == 1:
                        offset_x = 0
                        offset_y //= 2
                    
                    else:
                        offset_y = 0
                        offset_x //= 2
                
                # change position in list
                x_pos[k + 1] = x_pos[k] + offset_x
                y_pos[k + 1] = y_pos[k] + offset_y
                
                # add position to dictionary
                if (k == N - 2):
                    positions.add((x_pos[N-1], y_pos[N-1]))

                k += 1
                

    print(len(positions))




# main
with open('./9/input.txt') as f:
        moves = f.readlines()

moves = [s.strip() for s in moves]

#part_one()
part_two()