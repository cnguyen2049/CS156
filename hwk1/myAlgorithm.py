#Shunt
import sys
import heapq

inputFile = sys.argv[1]
heuristic = sys.argv[2]
fuel = sys.argv[3]

letters ={'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9}
numbers ={1:'A',2:'B',3'C',4:'D',5:'E',6:'F',7:'G',8:'H',9:'I'}
goal = {'H':'H'}

class Node:
	def __init__(self,x,y,fuel,state,cost):
		self.x = x
		self.y = y
		self.fuel = fuel
		self.state = state #this is the letter
		self.cost = cost #this is wind
		self.nextEl = None
	def get_self(self):	
		return self.fuel;
	def getNext():
		return self.nextEl


findKey(values,2)

class PriorityQueue:
	def __init__(self):
		self.elements = []
	def empty(self):
		return len(self.elements) ==0
	def length(self):
		return len(self.elements)
	def put(self, item,priority):
		heapq.heappush(self.elements,(priority,item))
	def get(self):
		return heapq.heappop(self.elements)[1]

def buildNode(x,y,fuel,state,cost):
	n = Node(x,y,fuel,state,cost)
	return n

MakeNode2 = buildNode(1,2,3,'A',5)
print MakeNode2.state
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

def checkNeighbors(Map,x,y):
	airX = y
	airY = x
	mapWidth = len(Map[0])
	mapHeight = len(Map)
	if airX < 0 and airY < 0:
		return False
	elif airX < 0:
		return False
	elif airX > mapWidth:
		return false
	elif airY < 0:
		return False
	elif airY > mapHeight:
		return False
	else:
		return True



def produceNodes(Map,node):
	x = node.x
	y = node.y
	nodes = []
	if checkNeighbors(Map,x-1,y) and (node.fuel - (int)(Map[x-1][y])):
		nodes.append(buildNode(x-1,y,0,numbers[(int)(Map[x-1][y])],(int)(Map[x-1][y])))
	if checkNeighbors(Map,x+1,y) and (node.fuel - (int)(Map[x+1][y])):
		nodes.append(buildNode(x+1,y,0,numbers[(int)(Map[x+1][y])],(int)(Map[x+1][y])))
	if checkNeighbors(Map,x,y-1) and (node.fuel - (int)(Map[x][y-1])):
		nodes.append(buildNode(x,y-1,0,numbers[(int)(Map[x][y-1])],(int)(Map[x][y-1])))
	if checkNeighbors(Map,x,y+1) and (node.fuel - (int)(Map[x][y+1])):
		nodes.append(buildNode(x,y+1,0,numbers[(int)(Map[x][y+1])],(int)(Map[x][y+1])))
	return nodes

def printOut(startingMap):
	output = ""
	test = []
	for eachRow in startingMap:
		test.append(eachRow)
		for element in eachRow:
			output = output + element
	return test

"""
This function finds the coordinates
and the starting value of the fuel
"""
def Finder(startingMap,item):
	y = 0
	for eachRow in startingMap:
		x = 0
		for column in eachRow:
			for key in values:

				if column == key: 
					return Node(x,y,fuel,'plane',values[key])
			x = x + 1
			#print "X is %d" %(x)
		y = y + 1
		#print "Y is %d" %(y)

def euclidian(airplane,airport):
	x = airplane.x - airport.x
	y = airplane.y - airport.y
	euclidian = math.sqrt(x*x + y * y)
	return euclidian

def manhattan(airplane,airport):
	x = airplane.x - airport.x
	y = airplane.y - airport.y
	manhattan = abs(x) + abs(y)
	return manhattan


"""
Beginning to implement A star algorithm
"""
def astar (airplane, Map, goal): #start and goal will be Nodes
	frontier = PriorityQueue()
	frontier.put(start,0);
	closedList = set()
	prevNode = 
	path_cost = 0
	while not frontier.empty():
		node = frontier.get()
		if node.state == 'H':
			return true
		closedList |= node
		neighbors = createNeighbors(node,Map)

