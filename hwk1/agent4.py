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
letters ={'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9}
numbers = {'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'P':0}
letters_to_numbers ={1:'A',2:'B',3:'C',4:'D',5:'E',6:'F',7:'G',8:'H',9:'I',0:'H'}
global goal_dic
goal_dic = {}
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

def readfile(inputFile):
	inputMap = open(inputFile,'r')
	startingMap = []
	for line in inputMap:
		eachRow = []
		for character in line:
			if line != '\n':
				eachRow.append(character)
		startingMap.append(eachRow)
	return startingMap


def checkneighbors(Map,row,col):
	airX = col
	airY = row
	#print "Row  %d and col %d" %(airY ,airX)
	mapWidth = len(Map[0])-1
	mapWidth -=2
	mapHeight = len(Map)-1
	#print (mapWidth,mapHeight)
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
					node.append((row,col))
			col = col + 1
			#print "X is %d" %(x)
		row = row + 1
		#print "Y is %d" %(y)
	return node

def euclidian(node,goal):
	x1 = node[0]
	y1 = node[1]
	x2 = goal[0]
	y2 = goal[1]
	euclidian = math.sqrt(x1*x2 + y1 * y2)
	return euclidian

def manhattan(tup1,tup2):
	col = tup1[1] - tup2[1]
	row = tup[0] - tup2[0]
	manhattan = abs(x) + abs(y)
	return manhattan


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

def astar (weathermap,start,goal): #start and goal will be Nodes
	frontier = PriorityQueue()
	frontier.put(0,start)
	came_from = {}
	cost_so_far = {}
	came_from[start] = None
	cost_so_far[start] = 0
	while not frontier.empty():
		current = frontier.get()
		if current == goal:
			print "Goal Reached"
			#print current
			break
		for next in weathermap.neighbors(current):
			#print "next"
			#print next
			next_row = next[0]
			next_col = next[1]
			print next_row,next_col
			val = Map[next_row][next_col]
			print "val is %s" %val
			new_cost = cost_so_far[current] + numbers[val]
			if next not in cost_so_far or new_cost < cost_so_far[next]:
				cost_so_far[next] = new_cost
				f = new_cost + heuristic(next,goal)
				frontier.put(f,next)
				print "Added to the Open List"
				print frontier.elements
				came_from[next] = current
		#if frontier == []:
			#return None
	return came_from

def check_fuel(Map,path):
	length = len(path)-1
	i = 0
	tank = fuel
	while i!=length:
		tup = path[i]
		col = tup[1]
		row = tup[0]
		#print col,row
		cost = int(Map[row][col])
		tank = tank - cost
		i += 1
	if tank < 0:
		return True
	else:
		return False

def printStep(Map,path):
	tank = fuel
	if(path == None):
		print "Breaks"
		return "No Solutions"
	elif check_fuel(Map,path):
		print "Breaks"
		return "No Solution" 	
	else:
		i = 0
		steps = 1
		length = len(path)
		while i < length:
			print "step %d fuel is %d" %(steps,tank)
			row = path[i][0]
			col = path[i][1]
			print Map
			if Map[row][col] == 'P':
				val = 0
			else:
				val = int(Map[row][col])
			tank = tank - val
			print Map
			
			Map[row][col] = str(letters_to_numbers[val])
			print Map
			print printOut(Map)			
			#print Map
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
	return path	

def build_edges(Map,tup):
	row = tup[0]
	col = tup[1]
	nodes = []
	if checkneighbors(Map,row+1,col):
		nodes.append((row+1,col))
	if checkneighbors(Map,row-1,col):
		nodes.append((row-1,col))
	if checkneighbors(Map,row,col-1):
		nodes.append((row,col-1))
	if checkneighbors(Map,row,col+1):
		nodes.append((row,col+1))
	print nodes
	return nodes

def build_graph(Map,g):
	length =len(Map[0]) -1
	height = len(Map)
	row = 0	
	for row in range(0,height):
		col = 0
		for col in range (0,length):
			neighbors = build_edges(Map,(row,col))
			g.edges.update({(row,col):neighbors})
			col += 1
		row+= 1
	return g		

	
global Map 
Map= readfile(inputFile)
output = printOut(Map)
global goal
input1 = Finder(Map,letters)
input2 = Finder(Map,airport)
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
