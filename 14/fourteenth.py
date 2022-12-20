
def get_reverse_sign(x :int):
    if x >= 0:
        return -1
    else:
        return 1

def keepMoving(row: int, col: int):
    return not occupied[row + 1][col] or not occupied[row + 1][col + 1] or not occupied[row + 1][col - 1]

def part_one():

    # parse everythings
       
    for i in range(len(obstacles)):
        points = obstacles[i].replace('->', ',').split(',')
        
        row = 0
        col = 0
        new_row = 0
        new_col = 0

        for j in range(0, len(points), 2):
            if j == 0:
                row = int(points[j + 1])
                col = int(points[j])
            else:
                new_row = int(points[j + 1])
                new_col = int(points[j])

                # same column build vertically
                if (col == new_col):
                    offset = row - new_row
                    sign = get_reverse_sign(offset)
                    offset = abs(offset)

                    # iterate cells and mark them
                    for k in range(offset + 1):
                        occupied[row + sign * k][col] = True

                    # add ground
                    last_ground[col] = max(last_ground[col], max(row, new_row)) 

                # same row build horizontally
                else:
                    offset = col - new_col
                    sign = get_reverse_sign(offset)
                    offset = abs(offset)

                    # iterate cells and mark them
                    for k in range(offset + 1):
                        occupied[row][col + sign * k] = True
                        last_ground[col + sign * k] = max(last_ground[col + sign * k], row)
            
                # prepare for next line
                row = new_row
                col = new_col

    # start pouring the sand
    total_sand = 0
    keepCounting = True

    while keepCounting:

        # new sand dropping
        sand_row = 0
        sand_col = 500

        while keepMoving(sand_row, sand_col):

            if sand_row > last_ground[sand_col]:
                keepCounting = False
                break

            # go down
            while not occupied[sand_row + 1][sand_col]:
                sand_row += 1
            
            # try to move diagonally
            if not occupied[sand_row + 1][sand_col - 1]:
                sand_row += 1
                sand_col -= 1
            elif not occupied[sand_row + 1][sand_col + 1]:
                sand_row += 1
                sand_col += 1
        
        if keepCounting:
            occupied[sand_row][sand_col] = True
            total_sand += 1
    
    print(total_sand)
            
            

        
    print(last_ground)
        
    
    

# main
with open('./14/input.txt') as f:
        obstacles = f.readlines()

obstacles = [s.strip() for s in obstacles]
big_number = 1000
last_ground = [-1] * big_number

occupied = [[False for i in range(big_number)]
                        for j in range(big_number)]

part_one()