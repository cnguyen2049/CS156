#Shunt
import sys
import heapq
import math
inputFile = sys.argv[1]
h = sys.argv[2]
global fuel 
fuel = sys.argv[3]

letters ={'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9}
numbers ={1:'A',2:'B',3:'C',4:'D',5:'E',6:'F',7:'G',8:'H',9:'I'}
goal = {'P':'P'}



class Node:
	def __init__(self,x,y,fuel,state,cost):
		self.x = x
		self.y = y
		self.fuel = fuel
		self.state = state #this is the letter
		self.cost = cost #this is wind




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
		return heapq.heappop(self.elements)[0]


def buildNode(x,y,fuel,state,cost):
	n = Node(x,y,fuel,state,cost)
	return n


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
	elif airX > mapWidth-1:
		return false
	elif airY < 0:
		return False
	elif airY > mapHeight-1:
		return False
	else:
		return True

def ifLetter(letter,dictionary):
	for key in dictionary:
		if(letter == key):
			return True
		else:
			return False

def produceNodes(Map,node):
	y = node.x
	x = node.y
	nodes = []
	
	if checkNeighbors(Map,x-1,y) and (node.fuel - (int)(Map[x-1][y])):
		state = (int)(Map[x-1][y])
		cost = (int)(Map[x-1][y])
		n = buildNode(x-1,y,0,numbers[state],cost)
		nodes.append(n)
	if checkNeighbors(Map,x+1,y) and (node.fuel - (int)(Map[x+1][y])):
		state = (int)(Map[x+1][y])
		cost = (int)(Map[x+1][y])
		n = buildNode(x+1,y,0,numbers[state],cost)
		nodes.append(n)
	if checkNeighbors(Map,x,y-1) and (node.fuel - (int)(Map[x][y-1])):
		state = (int)(Map[x-1][y])
		nodes.append(buildNode(x,y-1,0,numbers[(int)(Map[x][y-1])],(int)(Map[x][y-1])))
	
	if (checkNeighbors(Map,x,y+1)) and (node.fuel - (int)(Map[x][y+1])):
		state = (int)(Map[x][y+1])
		cost = (int)(Map[x][y+1])
		n = buildNode(x,y+1,0,numbers[state],cost)
		nodes.append(n)
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
	
	fuel = 7
	y = 0
	for eachRow in startingMap:
		x = 0
		for column in eachRow:
			for key in item:
				if column == key: 
					return Node(x,y,fuel,key,item[key])
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


def checkInOpen(node,succesor,f):
	nx = node.x
	ny = node.y
	sx = succesor.y
	sy	= succesor.y
	print nx,sx
	print ny, sy
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

def astar (Map,start,goal): #start and goal will be Nodes
	frontier = PriorityQueue()
	frontier.put(0,start)
	closedList = []
	
	loop = 0
	print frontier.empty()
	while not frontier.empty():
		print "We loop through %d" %(loop)
		node = frontier.get()
		print "NODE STATE"
		print node.state
		if node.x == goal.x and node.y == goal.y:
			closedList.append(node)
			print "Broke here 0"
			return closedList
		else:
			print "Broke here 1"
			closedList.append(node)
			neighbors = produceNodes(Map,node)
			print "Length of neighbor list %d " %(len(neighbors))
			for next in neighbors:
				print "next State is"
				print next.state
				if(next.x == goal.y and next.y == goal.y):
					return closedList.append(next)
				
				g = node.cost + heuristic(next,node)
				h = node.cost + heuristic(node,goal)
				f = g + h
				print f,g,h
				
				if(checkInOpen(node,next,f)):
					print "Broke here 1"
					continue
				elif(checkInClosed(node,next,f)):
					print "Broke here 2 "
					continue

				else:
					print "f is %d" %(f)
					print "next.state is %s" %(next.state)
					frontier.put(f,next)
		
	return closedList
	

Map = readFile(inputFile)
print Map
testQ = PriorityQueue()
testQ.put(1.222324323432,10)
print "POP"
print testQ.get()
Goal = Finder(Map,goal)
start = Finder(Map,letters)
#Map[start.x][start.y] = letters[start.state]
#Map[Goal.y][Goal.x] = 0
print Map
print "Goal X,Y"
print Goal.x, Goal.y
path = astar(Map,start,Goal)
print path
neighbors = produceNodes(Map,start)
print "Print neighbors %d" % len(neighbors)
print "Points in neighbors"
for node in neighbors:
	print node.x, node.y,node.state
print "Points in path"
for node in path:
	print node.x, node.y,node.state
"""
print numbers[(int)(Map[1][3])]

testNode = Node(0,0,0,0,0)
array = produceNodes(Map,testNode)
print len(array)
"""
