#Shunt
import sys
import copy
import heapq
import math
inputFile = sys.argv[1]
h = sys.argv[2]
global fuel 
fuel = (int)(sys.argv[3])

global letters 
letters ={'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'P':0}
numbers ={1:'A',2:'B',3:'C',4:'D',5:'E',6:'F',7:'G',8:'H',9:'I'}
airport = {'P':'P'}
global airplane
airplane = ['A','B','C','D','E','F','G','H','I']

class Graph:
    def __init__(self):
        self.edges = {}
    
    def neighbors(self, id):
        return self.edges[id]


class PriorityQueue:
	def __init__(self):
		self.elements = []
	def empty(self):
		return len(self.elements) ==0
	def length(self):
		return len(self.elements)
	def put(self, priority,item):
		heapq.heappush(self.elements,(item,priority))
	def get(self):
		return heapq.heappop(self.elements)[0]
"""
Beginning to write function to read in the text file
"""

def readFile(inputFile):
	inputMap = open(inputFile,'r')
	startingMap = []
	for line in inputMap:
		eachRow = []
		for character in line:
			if line != '\n':
				eachRow.append(character)
		startingMap.append(eachRow)
	return startingMap

def checkneighbors(Map,x,y):
	airX = y
	airY = x
	mapWidth = len(Map[0])-1
	mapHeight = len(Map)-1

	if airX < 0 and airY < 0:
		return False
	elif airX < 0:
		return False
	elif airX > mapWidth:
		return False
	elif airY < 0:
		return False
	elif airY > mapHeight:
		return False
	else:
		return True

def is_letter(Map,letter,x,y):
	letter = Map[x][y]
	loopval = 0
	for key in airplane:
		if letter == key:
			return True
	return False
def ifGoal(letter):
	if(letter == 'P'):
		return True
	return False

def printOut(startingMap):
	output = ""
	for eachRow in startingMap:
		for element in eachRow:
			output = output + element
	return output

"""
This function finds the coordinates
and the starting value of the fuel
"""
def Finder(startingMap,item):
	fuel = 7
	y = 0
	for eachRow in startingMap:
		x = 0
		for column in eachRow:
			for key in item:
				if column == key: 
					return x,y
			x = x + 1
			#print "X is %d" %(x)
		y = y + 1
		#print "Y is %d" %(y)

def euclidian(node,goal):
	x1 = node[0]
	y1 = node[1]
	x2 = goal[0]
	y2 = goal[1]
	euclidian = math.sqrt(x1*x2 + y1 * y2)
	return euclidian

def manhattan(airplane,airport):
	x = airplane.x - airport.x
	y = airplane.y - airport.y
	manhattan = abs(x) + abs(y)
	return manhattan


def checkInOpen(node,succesor,f):
	nx = node.x
	ny = node.y
	sx = succesor.y
	sy	= succesor.y
	#print nx,sx
	#print ny, sy
	if(nx == sx and ny == sy):
		return True
	
def checkInClosed(node,succesor,f):
	nx = node.x
	ny = node.y
	sx = succesor.y
	sy	= succesor.y
	if(nx == sx and ny == sy):
		return True


h = "euclidian"
if h == "euclidian" :
    heuristic = euclidian
elif heur == "manhattan" :
    heuristic = manhattan
else:
    heuristic = custom
"""
Beginning to implement A star algorithm
"""
"""
		if not is_letter(Map,letters,x,y):
			tank = tank - int(Map[x][y])
		if(tank < 0):
			return None"""
def astar (Map,start,goal): #start and goal will be Nodes
	print start	
	global fuel
	tank = fuel
	frontier = PriorityQueue()
	frontier.put(0,start)
	loop = 0
	cost_so_far= {}
	traveled = []
	#closedset = {start}
	came_from ={start:None}
	cost_so_far[start] = 0
	closedset = {start}
	neighbors = set()
	while not frontier.empty():
		current = frontier.get()
		print "Current is"
		y = current[0]
		x = current[1]
		print current 
		if current == goal:
			print "BROKE HERE"
			#print "Why doesn't it break here"
			print current
			came_from[current] = goal
			break
		#print "Made empty set"
		if checkneighbors(Map,x+1,y) and not (x+1,y)in came_from:
			neighbors |= ({(x+1,y)})
			print neighbors
		if checkneighbors(Map,x-1,y) and not (x-1,y)in came_from:
			neighbors  |= {(x-1,y)}
			print neighbors
		if checkneighbors(Map,x,y+1) and not (x,y+1)in came_from:
			neighbors  |= {(x,y+1)}
			print neighbors
		if checkneighbors(Map,x,y-1) and not (x,y-1)in came_from:
			neighbors  |= {(x,y-1)}	
			print neighbors
		#print " all the elements in neighbors"
		#print neighbors

		print neighbors
		for next in neighbors:
			new_cost = cost_so_far[current]
			if next not in came_from:
				cost_so_far[next] = new_cost
				priority = new_cost + heuristic(next,goal)
				#print "f is %d" %priority
				#print next
				frontier.put(priority,next)
				came_from[next] = current
				#print "Came from added
		closedset = closedset | {current}
		if frontier == []:
			return None
	#newPath = copy.copy(came_from[current])
	#newPath.append(current)	

	#print "Came from is"
	
	#newPath = copy.copy(came_from);
	print sorted(cost_so_far)
	print came_from
	return sorted(came_from)
	
def printStep(Map,path):
	if(path == None):
		print "No Solutions"
		return None
	else:
		global fuel
		Map = readFile(inputFile)
		output = printOut(Map)
		steps = 1
		for node in path:
			print "Map %d Fuel %s" %(steps,fuel)
			steps = steps + 1 
			x = node.x
			y = node.y
			if(node.state == 'P'):
				Map[x][y] = 'H'
			else:
				Map[x][y]= node.state
			output = printOut(Map)

			Map[x][y] = str(node.cost)
			fuel = fuel - node.cost
			print output

def reconstruct_path(came_from, start, goal):
    current = goal
    path = [current]
    while current != start:
        current = came_from[current]
        path.append(current)
    return path	

def build_edges(Map,tup):
	x = tup[1]
	y = tup[0]
	nodes = []
	if checkneighbors(Map,x+1,y):
		nodes.append((x+1,y))
	if checkneighbors(Map,x-1,y):
		nodes.append((x-1,y))
	if checkneighbors(Map,x,y-1):
		nodes.append((x,y-1))
	if checkneighbors(Map,x,y+1):
		nodes.append((x,y+1))
	#print nodes
	return nodes
def build_graph(Map,g):
	length =len(Map[0])-1
	height = len(Map)
	print height
	print length
	y = 0	
	for y in range(0,height):
		print "Y is %d" %y 
		x = 0
		for x in range (0,length):
			print "X is %d" %x
			neighbors = build_edges(Map,(x,y))
			g.edges.update({(x,y):neighbors})
			x += 1
		y+= 1
	return g			
Map = readFile(inputFile)
output = printOut(Map)
#print output
goal = Finder(Map,airport)
start = Finder(Map,airplane)
#print goal
#print start
#path = astar(Map,start,goal)
g = Graph()
#g.edges = {(1,0):[(0,0)]}
#g.edges.update({(2,0):[(1,1)]})
g = build_graph(Map,g)
print g.edges
"""
g.edges = {
    'A': ['B'],
    'B': ['A', 'C', 'D'],
    'C': ['A'],
    'D': ['E', 'A'],
    'E': ['B']
}
"""
#g = build_graph(Map,g)
#print g.edges
#g = build_edges(Map,g,start)
#print g.edges
"""
g.edges = {(0,0):[(0,1),(1,0)]} 
#print g.edges

practice = []
practice.append((1,0))
practice.append((0,1))
#print practice
g.edges = {start:practice}
"""
#print g.edges
#print path[0]
#if (2,1) == (2,1):
	#print "true"
#solution = reconstruct_path(path,start,goal)
"""	
union = set()
union |= {(2,1)}
union |= {(0,0)}
union |= {(1,1)}
union |= {(2,2)}
print union

testq = PriorityQueue()

tuple2 = (2,1)
testq.put(0,tuple2)
current = testq.get()
x = current[0]
print x
"""
