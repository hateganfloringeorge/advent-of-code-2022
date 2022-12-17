def check_down_up():
    print("^")
    for j in range(N):
        local_highest = '-'
        for i in range(N):
            if (local_highest < forest[N-1-i][j]):
                visible_positions.add((N-1-i,j))
                #skip the rest if 9
                if (forest[N-1-i][j] == '9'):
                    break
                local_highest = forest[N-1-i][j]
            

def check_up_down():
    print("\/")
    for j in range(N):
        local_highest = '-'
        for i in range(N):
            if (local_highest < forest[i][j]):
                visible_positions.add((i,j))
                #skip the rest if 9
                if (forest[i][j] == '9'):
                    break
                local_highest = forest[i][j]

def check_right_left():
    print("<=")
    for i in range(N):
        local_highest = '-'
        for j in range(N):
            if (local_highest < forest[i][N-1-j]):
                visible_positions.add((i,N-1-j))
                #skip the rest if 9
                if (forest[i][N-1-j] == '9'):
                    break
                local_highest = forest[i][N-1-j]

def check_left_right():
    print("=>")
    for i in range(N):
        local_highest = '-'
        for j in range(N):
            if (local_highest < forest[i][j]):
                visible_positions.add((i,j))
                #skip the rest if 9
                if (forest[i][j] == '9'):
                    break
                local_highest = forest[i][j]


def part_one():
    
    check_left_right()
    check_right_left()
    check_up_down()
    check_down_up()
    print(len(visible_positions))


# part two
def count_up(i,j):
    height = forest[i][j]
    score = 0
    i -= 1

    while i >= 0 and height > forest[i][j]:
        score += 1
        i -= 1
    
    if (i < 0):
        return score
    return score + 1

def count_down(i,j):
    height = forest[i][j]
    score = 0
    i += 1

    while i <= N-1 and height > forest[i][j]:
        score += 1
        i += 1
    
    if (i > N-1):
        return score
    return score + 1


def count_left(i,j):
    height = forest[i][j]
    score = 0
    j -= 1

    while j >= 0 and height > forest[i][j]:
        score += 1
        j -= 1
    
    if (j < 0):
        return score
    return score + 1

def count_right(i,j):
    height = forest[i][j]
    score = 0
    j += 1

    while j <= N-1 and height > forest[i][j]:
        score += 1
        j += 1
    
    if (j > N-1):
        return score
    return score + 1


def compute_score(i, j):
    if (i == 0 or j == 0 or i == N-1 or j == N-1):
        return 0

    score = count_up(i,j) * count_down(i,j) * count_left(i,j) * count_right(i,j)
    return score

    
def part_two():

    max_score = 0
    for i in range(N):
        for j in range(N):
            aux = compute_score(i,j)
            if (aux > max_score):
                max_score = aux
    
    print(max_score)

# main
with open('./8/input.txt') as f:
        forest = f.readlines()

forest = [s.strip() for s in forest]
N = len(forest)

visible_positions = {(0,0)}

#part_one()
part_two()