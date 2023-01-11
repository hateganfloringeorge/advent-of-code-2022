def get_common_sides(x: int, y: int, z: int):
    side_1 = (0, 0, 0)
    side_2 = (0, 0, 0)
    common_sides = 0
    for i in range(3):
        if (i == 0):
            side_1 = tuple([x + 1, y, z])
            side_2 = tuple([x - 1, y, z])
        elif (i == 1):
            side_1 = tuple([x, y + 1, z])
            side_2 = tuple([x, y - 1, z])
        elif (i == 2):
            side_1 = tuple([x, y, z + 1])
            side_2 = tuple([x, y, z - 1])
        
        if side_1 in cubes:
            common_sides += 1
        if side_2 in cubes:
            common_sides += 1

    return common_sides


def part_one():

    for data in cores:
        core_position = tuple([eval(i) for i in data.split(',')])
        cubes.add(core_position)
    print(cubes)

    common_sides = 0
    for (x, y, z) in cubes:
        common_sides += get_common_sides(x, y, z)
    print(common_sides)
    print(len(cubes) * 6 - common_sides)



# main
with open('./18/input.txt') as f:
        cores = f.readlines()

cores = [s.strip('\n') for s in cores]
cubes = set()

part_one()