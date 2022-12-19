from collections import deque
 
# A data structure for queue used in BFS
class QueueNode:
    def __init__(self,x: int, y: int, dist: int):
        self.x = x
        self.y = y
        self.dist = dist  # Cell's distance from the source

# Check whether given cell(row,col)
# is a valid cell or not
def isValid(row: int, col: int):
    return (row >= 0) and (row < H) and (col >= 0) and (col < W)


def checkMovement(old_x, old_y, new_x, new_y):
    if maze[old_x][old_y] == 'S':
        return True
        # if maze[new_x][new_y] == 'a':
        #     return True
        # else:
        #     return False
    
    # I don't get it... the expected result seems wrong... b
    if (ord(maze[new_x][new_y]) - ord(maze[old_x][old_y])) <= 1:
        # if maze[new_x][new_y] == 'E' and maze[old_x][old_y] != 'z':
        #     return False
        # return True
        return True
    return False

rowNum = [-1, 0, 0, 1]
colNum = [0, -1, 1, 0]

def part_one():
    start_x = 0
    start_y = 0
    distance = 0
    for i in range(H):
        for j in range(W):
            if (maze[i][j] == 'S'):
                start_x = i
                start_y = j
                break
    
    visited = [[False for i in range(W)]
                        for j in range(H)]
    
    visited[start_x][start_y] = True

    counter = 0
    
    q = deque()
    s = QueueNode(start_x, start_y, 0)
    q.append(s)

    # trying to BSF
    while q:
        node = q.popleft()

        # check if reached finish
        if maze[node.x][node.y] == 'E':
            distance = node.dist
            break
        
        for i in range(4):
            row = node.x + rowNum[i]
            col = node.y + colNum[i]

            if (isValid(row, col) and not visited[row][col]
                and checkMovement(node.x, node.y, row, col)):
                counter += 1
                
                visited[row][col] = True
                q.append(QueueNode(row, col, node.dist + 1))


    print(counter)
    print(distance)

# main
with open('./12/input.txt') as f:
        maze = f.readlines()

maze = [s.strip() for s in maze]

H = len(maze)
W = len(maze[0])
part_one()