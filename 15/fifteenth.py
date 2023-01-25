import sys

def part_one():
    #search_y = 10
    search_y = 2000000

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



        
def part_two():

    min_val = 0
    max_val = 4000000
    lines_intervals = {}
    for i in range(max_val + 1):
        lines_intervals[i] = []

    for data in details:
        sensor, beacon = data.split(':')

        sensor_x, sensor_y = sensor.split(',')
        beacon_x, beacon_y = beacon.split(',')
        
        sensor_x = eval(sensor_x.strip("Sensor at x="))
        sensor_y = eval(sensor_y.strip(" y="))

        beacon_x = eval(beacon_x.strip(" closest beacon is at x="))
        beacon_y = eval(beacon_y.strip(" y="))

        if sensor_y >= min_val and sensor_y <= max_val and sensor_x >= min_val and sensor_x <= max_val:
            if not (sensor_x, sensor_x) in lines_intervals[sensor_y]:
                lines_intervals[sensor_y].append((sensor_x, sensor_x))

        if beacon_y >= min_val and beacon_y <= max_val and beacon_x >= min_val and beacon_x <= max_val:
            if not (beacon_x, beacon_x) in lines_intervals[beacon_y]:
                lines_intervals[beacon_y].append((beacon_x, beacon_x))
        
        distance = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
        for i in range(distance):
            if (sensor_y + i <= max_val and sensor_y + i >= min_val) or (sensor_y - i <= max_val and sensor_y - i >= min_val):
                lowest_value = sensor_x - (distance - i)
                biggest_value = sensor_x + (distance - i)
                
                # not reaching the important interval
                if lowest_value > max_val or biggest_value < min_val:
                    continue
                
                if lowest_value < min_val:
                    lowest_value = min_val
                
                if biggest_value > max_val:
                    biggest_value = max_val
                
                if i == 0:
                    lines_intervals[sensor_y].append((lowest_value, biggest_value))
                else:
                    if sensor_y - i >= min_val and sensor_y - i <= max_val:
                        lines_intervals[sensor_y - i].append((lowest_value, biggest_value))
                    if sensor_y + i >= min_val and sensor_y + i <= max_val:
                        lines_intervals[sensor_y + i].append((lowest_value, biggest_value))

    for i in range(len(lines_intervals)):
        lines_intervals[i] = sorted(lines_intervals[i])

    for i in range(len(lines_intervals)):
        new_intervals = []
        (local_min, local_max) = (lines_intervals[i])[0]
        for j in range(len(lines_intervals[i])):
            (low, high) = lines_intervals[i][j]
            if low - 1 <= local_max:
                local_max = max(high, local_max)
            else:
                new_intervals.append((local_min, local_max))
                local_min = low
                local_max = high
            
        if not (local_min, local_max) in new_intervals:
            new_intervals.append((local_min, local_max))
        
        lines_intervals[i] = new_intervals

    result_y = 0    
    result_x = 0
    for i in range(len(lines_intervals)):
        if len(lines_intervals[i]) != 1:
            (_, result_x) = lines_intervals[i][0]
            result_x += 1
            result_y = i

    answer = result_y + result_x * 4000000
    print(answer)
    # print(lines_intervals)

    
        
    
# main
with open('./15/input.txt') as f:
        details = f.readlines()

details = [s.strip() for s in details]
occupied_positions = set(())

part_two()
