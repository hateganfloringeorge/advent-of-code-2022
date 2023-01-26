from typing import List
import copy

class Valve:

    def __init__(self, name: str, pressure: int, neighbours: List[str]):
        self.name = name
        self.pressure = pressure
        self.neighbours = neighbours
        self.distances = {}
    
    def compute_distance(self):
        # A simple BFS to compute distances to nodes
        start_point = self.name
        visited = []
        distances = {}
        queue = []

        visited.append(start_point)
        distances[start_point] = 0
        queue.append(start_point)

        while queue:
            node = queue.pop(0)
            valve = all_valves[node]

            for neighbour in valve.neighbours:
                if neighbour not in visited:
                    distances[neighbour] = distances[node] + 1
                    visited.append(neighbour)
                    queue.append(neighbour)
        
        self.distances = distances


def check_recursively(valve_name: str, minutes: int, visited: List[str], total: int):    
    valve = all_valves[valve_name]
    possible_places = []
    for node in relevant_valves:
        if node not in visited and valve.distances[node] <= (minutes - 1):
            possible_places.append(node)
    
    if not possible_places:
        return total

    all_totals = []
    for node in possible_places:
        new_minutes = minutes - valve.distances[node] - 1
        new_total = total + new_minutes * all_valves[node].pressure
        new_visited = visited.copy()
        new_visited.append(node)
        all_totals.append(check_recursively(node, new_minutes, new_visited, new_total))
    
    return max(all_totals)


def compute_bits_mask(visited: List[str]):
    total = 0
    for node in visited:
        total += 2 ** relevant_valves.index(node)
    return total

def check_recursively_elephant(valve_name: str, minutes: int, visited: List[str], total: int):    
    
    valve = all_valves[valve_name]
    possible_places = []
    for node in relevant_valves:
        if node not in visited and valve.distances[node] <= (minutes - 1):
            possible_places.append(node)
    
    if not possible_places:
        mask = compute_bits_mask(visited)
        if mask in already_checked:
            if total >= already_checked[mask]:
                already_checked[mask] = total
        else:
            already_checked[mask] = total
        # if first_time == True:
        #     if (valve_name, minutes) in already_checked:
        #         if already_checked[(valve_name, minutes)] > total:
        #             return 0
        #         else:
        #             already_checked[(valve_name, minutes)] = total
        #     else:
        #         already_checked[(valve_name, minutes)] = total

        #     check_recursively_elephant(start_point, 26, visited, total, False)

        print(visited, total)
        return total

    all_totals = []
    for node in possible_places:
        new_minutes = minutes - valve.distances[node] - 1
        new_total = total + new_minutes * all_valves[node].pressure
        new_visited = copy.deepcopy(visited)
        new_visited.append(node)
        all_totals.append(check_recursively_elephant(node, new_minutes, new_visited, new_total))
    
    return max(all_totals)

# def check_with_elephant(valve_names, minutes, visited: List[str], total: int):
#     global local_max
#     (valve_name1, valve_name2) = valve_names
#     (minutes1, minutes2) = minutes
#     already_checked.append([valve_name1, valve_name2, minutes1, minutes2])
#     valve1 = all_valves[valve_name1]
#     valve2 = all_valves[valve_name2]
#     possible_places1 = []
#     possible_places2 = []
    
#     for node in relevant_valves:
#         if node not in visited:
#             if valve1.distances[node] <= (minutes1 - 1):
#                 possible_places1.append(node)

#             if valve2.distances[node] <= (minutes2 - 1):
#                 possible_places2.append(node)
    
#     if not possible_places1 and not possible_places2:
#         print(visited, total)
#         return total

    
#     # for i in range(len(local_max)):
#     #     if len(visited) == (5 + i * 2):
#     #         if local_max[i] >= total:
#     #             return 0
#     #         else:
#     #             local_max[i] = total
            

#     all_totals1 = [0]
#     all_totals2 = [0]

#     if not possible_places1:
#         for node in possible_places2:
#             new_minutes = minutes2 - valve2.distances[node] - 1
#             new_total = total + new_minutes * all_valves[node].pressure
#             new_visited = copy.deepcopy(visited)
#             new_visited.append(node)
#             # if not [valve_name1, node, minutes1, new_minutes] in already_checked:
#             all_totals2.append(check_with_elephant((valve_name1,node), (minutes1, new_minutes), new_visited, new_total))
    
#     elif not possible_places2:
#         for node in possible_places1:
#             new_minutes = minutes1 - valve1.distances[node] - 1
#             new_total = total + new_minutes * all_valves[node].pressure
#             new_visited = copy.deepcopy(visited)
#             new_visited.append(node)
#             # if not [node, valve_name2, new_minutes, minutes2] in already_checked:
#             all_totals1.append(check_with_elephant((node, valve_name2), (new_minutes, minutes2), new_visited, new_total))
#     else:

#         for node1 in possible_places1:
#             new_minutes1 = minutes1 - valve1.distances[node1] - 1
#             new_total = total + new_minutes1 * all_valves[node1].pressure
#             new_visited = copy.deepcopy(visited)
#             new_visited.append(node1)
#             for node2 in possible_places2:
#                 if node2 not in new_visited:
#                     new_minutes2 = minutes2 - valve2.distances[node2] - 1
#                     new_total = new_total + new_minutes2 * all_valves[node2].pressure
#                     new_visited.append(node2)
#                     all_totals1.append(check_with_elephant((node1, node2), (new_minutes1, new_minutes2), new_visited, new_total))

#     return max(max(all_totals1), max(all_totals2))



def part_one():
    for data in details:
        part_1, part_2 = data.split(';')

        name = part_1[6:8]

        _, flow_rate = part_1.split('=')
        flow_rate = eval(flow_rate)

        # select only valves that are working
        if flow_rate != 0:
            relevant_valves.append(name)

        neighbours = part_2.strip(" tunnels lead to valves ").replace(' ','').split(',')
        all_valves[name] = Valve(name, flow_rate, neighbours)
    
    all_valves[start_point].compute_distance()
    for node in relevant_valves:
        all_valves[node].compute_distance()

    # part1
    # minutes = 30
    # print(check_recursively(start_point, minutes, [], 0))
    print("Getting ready")
    minutes = 26
    print(check_recursively_elephant(start_point, minutes, [], 0))
    result = 0
    for key1 in already_checked.keys():
        for key2 in already_checked.keys():
            if key1 & key2 == 0:
                result = max(result, already_checked[key1] + already_checked[key2])
    print(result)
    # print(check_with_elephant((start_point, start_point), (minutes, minutes), [], 0))
    

# main
with open('./16/input.txt') as f:
        details = f.readlines()

details = [s.strip('\n') for s in details]
all_valves = {}
relevant_valves = []
start_point = 'AA'
already_checked = {}
local_max = [0] * 6

part_one()
