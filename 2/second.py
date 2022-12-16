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
    

def part_one():
    total_points = 0
    for i in range(len(cheatsheet)):
        opponent_pick = cheatsheet[i][0]
        my_pick = cheatsheet[i][2]

        # get the picks to the same values 0-2
        opponent_pick = ord(opponent_pick) - ORD_A
        my_pick = ord(my_pick) - ORD_X

        total_points += (my_pick + 1) + result_points(opponent_pick, my_pick)

    print(total_points)

# main
with open('./2/input.txt') as f:
        cheatsheet = f.readlines()

part_one()