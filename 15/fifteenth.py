import sys

def part_one():
    #search_y = 10
    search_y = 2000000
    min_x = sys.maxsize
    max_x = 0
    min_y = sys.maxsize
    max_y = 0

    for data in details:
        sensor, beacon = data.split(':')

        sensor_x, sensor_y = sensor.split(',')
        beacon_x, beacon_y = beacon.split(',')
        
        sensor_x = eval(sensor_x.strip("Sensor at x="))
        sensor_y = eval(sensor_y.strip(" y="))
        #sensors.append((sensor_x, sensor_y))

        beacon_x = eval(beacon_x.strip(" closest beacon is at x="))
        beacon_y = eval(beacon_y.strip(" y="))
        #beacons.append((beacon_x, beacon_y))

        if sensor_y == search_y:
            occupied_positions.add(sensor_x)
        if beacon_y == search_y:
            beacons.append(beacon_x)
        
        distance = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
        if distance >= abs(search_y - sensor_y):
            distance -= abs(search_y - sensor_y)
            occupied_positions.add(sensor_x)
            for i in range(1, distance + 1):
                occupied_positions.add(sensor_x + i)
                occupied_positions.add(sensor_x - i)
                
    for x in beacons:
        if x in occupied_positions:
            occupied_positions.remove(x)
    print(len(occupied_positions))
        

    # more troublesome maybe will use at part two
    # elements = sensors + beacons
    # max_x, _ = max(elements, key=lambda x:x[0])
    # min_x, _ = min(elements, key=lambda x:x[0])
    # print(min_x, max_x)

    # _, max_y = max(elements, key=lambda x:x[1])
    # _, min_y = min(elements, key=lambda x:x[1])
    # print(min_y, max_y)


    
        
    
# main
with open('./15/input.txt') as f:
        details = f.readlines()

details = [s.strip() for s in details]
sensors = []
beacons = []
occupied_positions = set(())

part_one()
