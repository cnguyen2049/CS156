"""
# Shunt
# Chris
"""
import sys
import copy
import heapq
import math
inputFile = sys.argv[1]
h = sys.argv[2]
global fuel
fuel = (int)(sys.argv[3])
global letters
letters = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7,
           'H': 8, 'I': 9}
numbers = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
           '9': 9, 'P': 0}
letters_to_numbers = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G',
                      8: 'H', 9: 'I', 0: 'J'}
airport = {'P': 'P'}


class Graph:

    def __init__(self):
        self.edges = {}

    def neighbors(self, id):
        return self.edges[id]


class PriorityQueue:

    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def length(self):
        return len(self.elements)

    def put(self, priority, item):
        heapq.heappush(self.elements, (priority,item))

    def get(self):
        return heapq.heappop(self.elements)[1]
"""
Beginning to write function to read in the text file
"""


def read_file(inputFile):
    inputMap = open(inputFile, 'r')
    startingMap = []
    for line in inputMap:
        eachRow = []
        for character in line:
            if line != '\n':
                eachRow.append(character)
        startingMap.append(eachRow)
    return startingMap


def check_neighbors(Map, row, col):
    airX = col
    airY = row
    # print "Row  %d and col %d" %(airY ,airX)
    mapWidth = len(Map[0])-1
    mapWidth -= 1
    mapHeight = len(Map) - 1
    #print (mapWidth,mapHeight)
    if col < 0 or row < 0:
        return False
    elif col > mapWidth:
        return False
    elif row > mapHeight:
        return False
    else:
        return True


def print_out(startingMap):
    output = ""
    for eachRow in startingMap:
        for element in eachRow:
            output = output + element
    return output

"""
This function finds the coordinates
and the starting value of the fuel
"""


def finder(startingMap, item):
    node = []
    fuel = 7
    row = 0
    for eachRow in startingMap:
        col = 0
        for column in eachRow:
            for key in item:
                if column == key:
                    replace = item[key]
                    startingMap[row][col] = str(replace)
                    node.append((row, col))
            col = col + 1
            # print "X is %d" %(x)
        row = row + 1
        # print "Y is %d" %(y)
    return node


def euclidian(node, goal):
    x1 = node[0]
    y1 = node[1]
    x2 = goal[0]
    y2 = goal[1]
    x = x1 - x2
    y = y1 - y2
    # print x1,y1
    # print x2,y2
    euclidian = math.sqrt(x * x + y * y)
    return euclidian


def manhattan(tup1, tup2):
    col = tup1[1] - tup2[1]
    row = tup[0] - tup2[0]
    manhattan = abs(x) + abs(y)
    return manhattan


h = "euclidian"
if h == "euclidian":
    heuristic = euclidian
elif heur == "manhattan":
    heuristic = manhattan
else:
    heuristic = custom
"""
Beginning to implement A star algorithm
"""


def astar(weathermap, start, goal):
    frontier = PriorityQueue()
    frontier.put(0, start)
    path = {}
    cost = {}
    path[start] = None
    cost[start] = 0
    while not frontier.empty():
        print frontier.elements
        current = frontier.get()
        if current == goal:
            break
        for next in weathermap.neighbors(current):
            next_row = next[0]
            next_col = next[1]
            print next_row,next_col
            val = Map[next_row][next_col]
            new_cost = cost[current] + numbers[val]
            if next not in cost or new_cost < cost[next]:
                cost[next] = new_cost
                f = new_cost + heuristic(next, goal)
                print f,next
                frontier.put(f, next)
                path[next] = current
        if frontier == []:
            return None
    return path


def check_fuel(Map, path):
    tank = fuel
    for val in path:
        # print path[i]
        col = val[1]
        row = val[0]
        # print col,row
        key = (Map[row][col])
        cost = numbers[key]
        tank = tank - cost

    if tank < 0:
        return True
    else:
        return False


def print_step(Map, path):
    tank = fuel
    if(path is None):
        print "No route exists"
    else:
        i = 0
        steps = 1
        length = len(path)
        while i < length:
            print "Map:%d Fuel is:%d" % (steps, tank)
            row = path[i][0]
            col = path[i][1]
            if Map[row][col] == 'P':
                val = 0
            else:
                val = int(Map[row][col])
            tank = tank - val
            Map[row][col] = str(letters_to_numbers[val])
            print print_out(Map)
            Map[row][col] = str(val)
            i += 1
            steps += 1
    return ""


def reconstruct_path(came_from, start, goal):
    current = goal
    path = [current]
    while current != start:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path


def build_edges(Map, tup):
    row = tup[0]
    col = tup[1]
    nodes = []
    if check_neighbors(Map, row + 1, col):
        nodes.append((row + 1, col))
    if check_neighbors(Map, row - 1, col):
        nodes.append((row - 1, col))
    if check_neighbors(Map, row, col - 1):
        nodes.append((row, col - 1))
    if check_neighbors(Map, row, col + 1):
        nodes.append((row, col + 1))
    return nodes


def build_graph(Map, g):
    length = len(Map[0])-1
    height = len(Map)
    #print height
    for row in range(0, height):
        for col in range(0, length):
            neighbors = build_edges(Map, (row, col))
            g.edges.update({(row, col): neighbors})
        #col += 1
    #row += 1
    return g


def execute(Map, g, start, goal):
    if start == []:
		return None
    s = start[0]
    for points in goal:
        goal_point = points
        #print goal_point
        solution = astar(g, s, goal_point)
        path = reconstruct_path(solution, s, goal_point)
        if not check_fuel(Map, path):
            return path
    return None

global Map
Map = read_file(inputFile)
global goal

start = finder(Map, letters)

goal = finder(Map, airport)
g = Graph()
g = build_graph(Map, g)

answer = execute(Map, g, start, goal)
#print answer
print_step(Map, answer)
#print check_neighbors(Map,1,3)
#print build_edges(Map,(1,3))
#print_step(Map, answer)

"""
start = input2[0]
goal = input1[0]

#print goal
#print start
#print Map

g = Graph()
#print Map[0][3]
g = build_graph(Map,g)
print sorted(g.edges)
print g.edges
solution = astar(g,start,goal)
s = reconstruct_path(solution,start,goal)
#print Map
print printStep(Map,s)
/n
"""
