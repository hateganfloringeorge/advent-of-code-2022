from typing import List
from collections import deque
import copy

class Situation:
    def __init__(self, minutes_left: int, robots: List[int], ores: List[int]):
        self.minutes_left = minutes_left
        self.robots = robots
        self.ores = ores

def part_one():
    
    blueprints = [[0 for i in range(6)]
                        for j in range(len(instructions))]
    
    # parsing this thing
    for i in range(len(instructions)):
        separated = instructions[i].split('.')

        # first robot cost
        _, first_cost_line = separated[0].split(':')
        blueprints[i][0] = int(first_cost_line.strip('Each clay robot costs ore'))

        # second robot cost
        blueprints[i][1] = int(separated[1].strip('Each clay robot costs ore'))

        # third robot cost
        ore_part_3rd, clay_part_3rd = separated[2].split('and')
        blueprints[i][2] = int(ore_part_3rd.strip("Each obsidian robot costs ore"))
        blueprints[i][3] = int(clay_part_3rd.strip(" clay"))

        # last robot
        ore_part_4th, obsidian_part_4th = separated[3].split('and')
        blueprints[i][4] = int(ore_part_4th.strip("Each geode robot costs ore"))
        blueprints[i][5] = int(obsidian_part_4th.strip(" obsidian"))

    # compute max obsidian for blueprint

    final_result = 0
    for k in range(len(blueprints)):
        
        blueprint = blueprints[k]

        max_ore = max(blueprint[0], blueprint[1], blueprint[2], blueprint[4])
        max_clay = blueprint[3]

        intitial_situation = Situation(24, [1, 0, 0, 0], [0, 0, 0, 0])
        q = deque()
        q.append(intitial_situation)
        
        max_geode = 0

        while q:
            situation = q.popleft()

            while situation.minutes_left > 0:
                
                # add resources
                for i in range(4):
                    situation.ores[i] += situation.robots[i]
                
                # decrease time and check
                situation.minutes_left -= 1
                if situation.minutes_left == 0:
                    max_geode = max(max_geode, situation.ores[3])
                    continue

                # see if decisions need to be made

                # check if should skip situation
                # where you could have produced robot in previous round
                
                if situation.ores[0] - situation.robots[0] >= blueprint[4] and situation.ores[2] - situation.robots[2] >= blueprint[5]:
                    #if not(situation.ores[0] - 2 * situation.robots[0] >= blueprint[2] and situation.ores[1] - 2 * situation.robots[1] >= blueprint[3]):
                        new_robots = copy.deepcopy(situation.robots)
                        new_robots[3] += 1
                        new_ores = copy.deepcopy(situation.ores)
                        new_ores[0] -= blueprint[4]
                        new_ores[2] -= blueprint[5]
                        q.append(Situation(situation.minutes_left, new_robots, new_ores))
                else:

                    if situation.ores[0] - situation.robots[0] >= blueprint[2] and situation.ores[1] - situation.robots[1] >= blueprint[3]:
                        
                        new_robots = copy.deepcopy(situation.robots)
                        new_robots[2] += 1
                        new_ores = copy.deepcopy(situation.ores)
                        new_ores[0] -= blueprint[2]
                        new_ores[1] -= blueprint[3]
                        q.append(Situation(situation.minutes_left, new_robots, new_ores))
                    
                    else:

                        if situation.ores[0] - situation.robots[0] >= blueprint[0]:
                            if max_ore > situation.robots[0]:
                                if not (situation.ores[0] - 3 * situation.robots[0] >= blueprint[0]):
                                    new_robots = copy.deepcopy(situation.robots)
                                    new_robots[0] += 1
                                    new_ores = copy.deepcopy(situation.ores)
                                    new_ores[0] -= blueprint[0]
                                    q.append(Situation(situation.minutes_left, new_robots, new_ores))

                        if situation.ores[0] - situation.robots[0] >= blueprint[1]:
                            if max_clay > situation.robots[1]:
                                if not (situation.ores[0] - 3 * situation.robots[0] >= blueprint[1]):
                                    new_robots = copy.deepcopy(situation.robots)
                                    new_robots[1] += 1
                                    new_ores = copy.deepcopy(situation.ores)
                                    new_ores[0] -= blueprint[1]
                                    q.append(Situation(situation.minutes_left, new_robots, new_ores))
        
        print("For {} we found {} ", k+1, max_geode)
        final_result += (k + 1) * max_geode 

    print(final_result)


# main
with open('./19/input.txt') as f:
        instructions = f.readlines()

instructions = [s.strip() for s in instructions]

part_one()