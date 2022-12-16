#constants
ORD_A = ord('A')
ORD_X = ord('X')

def result_points(opponent, player):
    
    # check tie
    if (opponent == player):
        return 3

    # check corner cases
    if (opponent == 0 and player == 2):
            return 0

    if (player == 0 and opponent == 2):
            return 6

    #check win or lose
    if (player > opponent):
        return 6
    else:
        return 0

def compute_shape(opponent, result):
    if (result == 1):
        return opponent

    if (result == 0 and opponent == 0):
        return 2
    
    if (result == 2 and opponent == 2):
        return 0

    if (result == 0):
        return opponent - 1
    else:
        return opponent + 1

        

def part_one():
    total_points = 0
    for i in range(len(cheatsheet)):
        opponent_pick = cheatsheet[i][0]
        my_pick = cheatsheet[i][2]

        # get the picks to the same values 0-2
        opponent_pick = ord(opponent_pick) - ORD_A
        my_pick = ord(my_pick) - ORD_X

        # shapes are 0 indexed in normalization so add 1
        
        # part 1
        #total_points += (my_pick + 1) + result_points(opponent_pick, my_pick)

        # part 2 
        desired_result = my_pick
        total_points += desired_result * 3 + (compute_shape(opponent_pick, desired_result) + 1)

    print(total_points)

# main
with open('./2/input.txt') as f:
        cheatsheet = f.readlines()

part_one()