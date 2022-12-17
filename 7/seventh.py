class TreeNode:
    def __init__(self, name, parent):
        self.size = 0
        self.subdirs = []
        self.files = []
        self.parent = parent
        self.name = name
        self.hasDataFilled = False

def compute_sizes(node: TreeNode):
    total_size = 0
    if len(node.subdirs) != 0:
        for directory in node.subdirs:
            total_size += compute_sizes(directory)
    
    for (_, file_size) in node.files:
        total_size += file_size
    
    node.size = total_size
    return total_size

def part_one():

    # parsing (the hard part)
    i = 0
    dir_entries = [TreeNode('/', None)]
    current_node = dir_entries[0]

    while i < len(terminal):

        # guard against errors
        if '$' in terminal[i]:
            
            if ' ls' in terminal[i]:
                # move to next line and iterate until next command
                i += 1
                current_files = []
                current_directoryList = []
                while i < len(terminal) and '$' not in terminal[i]:

                    if terminal[i].startswith('dir'):
                        dir_name = terminal[i][4:]
                        new_node = TreeNode(dir_name, current_node)
                        dir_entries.append(new_node)
                        current_directoryList.append(new_node)
                    
                    else:
                        size, name = terminal[i].split(' ')
                        size = int(size)
                        current_files.append((name, size))
                    
                    i += 1
                i -= 1

                if (current_node.hasDataFilled == False):
                    current_node.files = current_files
                    current_node.subdirs = current_directoryList
                    current_node.hasDataFilled = True    

            else:
                # cd new_directory
                new_directory = terminal[i][5:len(terminal[i])]

                if new_directory == '..':
                    if (current_node.name != '/'):
                        current_node = current_node.parent
                else:
                    for j in range(len(current_node.subdirs)):
                        if current_node.subdirs[j].name == new_directory:
                            current_node = current_node.subdirs[j]
                            break
                    

        else:
            print("ERROR")
        
        i += 1
        
    # everything is parsed now time for the tasks
    compute_sizes(dir_entries[0])

    total_sum = 0
    for node in dir_entries:
        if node.size <= 100000:
            total_sum += node.size
    
    print(total_sum)

    # part two
    unused_memory = 70000000 - dir_entries[0].size
    memory_required = 30000000 - unused_memory
    plausible_files = []

    for i in range(len(dir_entries)):
        if dir_entries[i].size >= memory_required:
            plausible_files.append(dir_entries[i].size)

    
    print(min(plausible_files))


# main
with open('./7/input.txt') as f:
        terminal = f.readlines()

terminal = [s.strip() for s in terminal]

part_one()