
def print_maze():
    for row in maze:
        print("".join(row))
    print()

# misunderstood the text and thaught the order of the 
# direction you check is specific for an elf but it is not
# the classs is now quite rendundant but I am in too deep
class Elf:
    def __init__(self, i: int, j: int):
        self.i = i
        self.j = j
        #self.look_idx = look_idx
        
    def check_alone(self):

        for k in range(8):
            new_i = self.i + around_i[k]
            new_j = self.j + around_j[k]
            
            if (new_i < 0 or new_j < 0 or new_i >= H or new_j >= W):
                continue

            if maze[new_i][new_j] == '#':
                return False
        
        return True

    def change_index(self, i: int, j: int):
        self.i = i
        self.j = j

    
    def add_proposal(self):
        global look_index
        new_i = -1
        new_j = -1

        for k in range(4):
            check_index = (look_index + k) % 4
            
            # check north
            if (check_index == 0):
                if (self.i == 0):
                    continue
                
                if maze[self.i - 1][self.j] == '#':
                    continue
                
                if self.j != 0 and maze[self.i - 1][self.j - 1] == '#':
                    continue

                if self.j != H-1 and maze[self.i - 1][self.j + 1] == '#':
                    continue
                
                new_i = self.i - 1
                new_j = self.j
                break
                

            # check south
            if (check_index == 1):
                if (self.i == H-1):
                    continue
                
                if maze[self.i + 1][self.j] == '#':
                    continue
                
                if self.j != 0 and maze[self.i + 1][self.j - 1] == '#':
                    continue

                if self.j != H-1 and maze[self.i + 1][self.j + 1] == '#':
                    continue

                new_i = self.i + 1
                new_j = self.j
                break

            # check west
            if (check_index == 2):
                if (self.j == 0):
                    continue
                
                if maze[self.i][self.j - 1] == '#':
                    continue
                
                if self.i != 0 and maze[self.i - 1][self.j - 1] == '#':
                    continue

                if self.i != W-1 and maze[self.i + 1][self.j - 1] == '#':
                    continue
                
                new_j = self.j - 1
                new_i = self.i
                break

            # check east
            if (check_index == 3):
                if (self.j == W-1):
                    continue
                
                if maze[self.i][self.j + 1] == '#':
                    continue
                
                if self.i != 0 and maze[self.i - 1][self.j + 1] == '#':
                    continue

                if self.i != W-1 and maze[self.i + 1][self.j + 1] == '#':
                    continue
                
                new_j = self.j + 1
                new_i = self.i
                break

        # add proposal
        if (new_i != -1 and new_j != -1):
            if (new_i, new_j) in proposals:
                old_list = proposals[(new_i, new_j)]
                old_list.append((self.i, self.j))
                proposals[(new_i, new_j)] = old_list

            else:
                proposals[(new_i, new_j)] = [(self.i, self.j)]


def part_one():
    global look_index
    #print_maze()
    for i in range(len(initial_maze)):
        for j in range(len(initial_maze[0])):
            if initial_maze[i][j] == '#':
                elves.append(Elf(i +  H //2, j + W//2))
                maze[i +  H //2][j + W//2] = '#'
            else:
                maze[i][j] = '.'


    for _ in range(10):
        #print_maze()
        for x in elves:
            if not x.check_alone():
                x.add_proposal()
        
        for (to_i, to_j), pos_list in proposals.items():
            if len(pos_list) == 1:
                (from_i, from_j) = pos_list[0]
                for elf in elves:
                    if elf.i == from_i and elf.j == from_j:
                        elf.change_index(to_i, to_j)
                        maze[from_i][from_j] = '.'
                        maze[to_i][to_j] = '#'
                        break
        proposals.clear()
        look_index += 1
    
    #print_maze()
    min_i = min(node.i for node in elves)
    max_i = max(node.i for node in elves)
    min_j = min(node.j for node in elves)
    max_j = max(node.j for node in elves)
    print(min_i, min_j, max_i, max_j)

    total_sum = 0
    for i in range(min_i, max_i + 1):
        for j in range(min_j, max_j + 1):
            if maze[i][j] == '.':
                total_sum += 1
    
    print(total_sum)


def part_two():
    global look_index
    #print_maze()
    for i in range(len(initial_maze)):
        for j in range(len(initial_maze[0])):
            if initial_maze[i][j] == '#':
                elves.append(Elf(i +  H //2, j + W//2))
                maze[i +  H //2][j + W//2] = '#'
            else:
                maze[i][j] = '.'

    round = 1
    while True:
        for x in elves:
            if not x.check_alone():
                x.add_proposal()
        
        if len(proposals) == 0:
            print(round)
            break
        
        for (to_i, to_j), pos_list in proposals.items():
            if len(pos_list) == 1:
                (from_i, from_j) = pos_list[0]
                for elf in elves:
                    if elf.i == from_i and elf.j == from_j:
                        elf.change_index(to_i, to_j)
                        maze[from_i][from_j] = '.'
                        maze[to_i][to_j] = '#'
                        break
        proposals.clear()
        look_index += 1
        round += 1
    
    print(round)

# main
with open('./23/input.txt') as f:
        initial_maze = f.readlines()

initial_maze = [s.strip() for s in initial_maze]

H = len(initial_maze) * 100
W = len(initial_maze[0]) * 100

maze = [['.' for i in range(W)]
                    for j in range(H)]

around_i = [-1, -1, -1, 0, 1, 1, 1, 0]
around_j = [-1, 0, 1, 1, 1, 0, -1, -1]

look_index = 0
proposals = {}
elves = []

#part_one()
part_two()