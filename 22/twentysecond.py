import re
from typing import List

def get_opposite(maze: List[List[str]], pos_i: int, pos_j: int, move_idx:int):
    x = 0
    y = 0
    if go_x[move_idx] == 0:
        # go on y
        
        if go_y[move_idx] > 0:
            # start from top of img
            y = 0
            while maze[y][pos_j] == ' ':
                y += 1

        else:
            #start from bottom of img
            y = len(maze) - 1
            while maze[y][pos_j] == ' ':
                y -= 1
        return (y, pos_j)
            

    else:
        # go on x
        if go_x[move_idx] > 0:
            # start from left
            x = 0
            while maze[pos_i][x] == ' ':
                x += 1
        else:
            #start from right
            x = len(maze[0]) - 1
            while maze[pos_i][x] == ' ':
                x -= 1
            pass

        return (pos_i, x)

def part_one():
    H = len(instructions[:-2])
    W = max([len(s) for s in instructions[:-2]])
    commands = instructions[-1]

    # added 1 to cover everything with spaces not to worry about edges
    maze = [[' ' for i in range(W + 2)]
                        for j in range(H + 2)]
    # put everything starting with 1, 1 to be surrounded
    for i in range(H):
        for j in range(len(instructions[i])):
            maze[i+1][j+1] = instructions[i][j]

    # find starting position
    pos_i = 1
    pos_j = -1
    j = 0
    while pos_j == -1:
        if maze[pos_i][j] == '.':
            pos_j = j
        j += 1

    # get moves
    moves = list(filter(None, re.split('(\d+|\D+)', commands)))
    move_idx = 0
    
    # do motions
    for i in range(len(moves)):

        # go in a direction
        if moves[i].isnumeric():
            for j in range(eval(moves[i])):
                
                # stop for wall
                if (maze[pos_i + go_y[move_idx]][pos_j + go_x[move_idx]] == '#'):
                    break

                # continue if clear
                if (maze[pos_i + go_y[move_idx]][pos_j + go_x[move_idx]] == '.'):
                    pos_i += go_y[move_idx]
                    pos_j += go_x[move_idx]
                elif (maze[pos_i + go_y[move_idx]][pos_j + go_x[move_idx]] == ' '):
                    opp_i, opp_j =  get_opposite(maze, pos_i, pos_j, move_idx)
                    if maze[opp_i][opp_j] == '#':
                        break
                    else:
                        pos_i = opp_i
                        pos_j = opp_j            
        else:
            # change direction
            if moves[i] == 'R':
                move_idx = (move_idx + 1) % 4
            elif moves[i] == 'L':
                move_idx -= 1
                if move_idx == -1:
                    move_idx = 3
            else:
                print("Something went wrong")
    print(pos_i, pos_j, move_idx)
    print(pos_i * 1000 + 4 * pos_j + move_idx)
    #print(moves)

# main
with open('./22/input.txt') as f:
        instructions = f.readlines()

instructions = [s.strip('\n') for s in instructions]
go_x = [1, 0, -1, 0]
go_y = [0, 1, 0, -1]

part_one()