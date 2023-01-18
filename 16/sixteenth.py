from typing import List

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
        if node not in visited and valve.distances[node] <= (minutes + 1):
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

    minutes = 30
    print(check_recursively(start_point, minutes, [], 0))


# main
with open('./16/input.txt') as f:
        details = f.readlines()

details = [s.strip('\n') for s in details]
all_valves = {}
relevant_valves = []
time_limit = 30
start_point = 'AA'

part_one()
