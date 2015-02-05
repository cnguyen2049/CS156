#Shunt
import sys
import heapq

inputFile = sys.argv[1]
heuristic = sys.argv[2]
fuel = sys.argv[3]

values ={'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9}

goal = {'H':'Goal'}

class Node:
	def __init__(self,x,y,fuel,state,cost):
		self.x = x
		self.y = y
		self.fuel = fuel
		self.nextEl = None
		self.state = state
		self.cost = cost
	def get_self(self):	
		return self.fuel;
	def getNext():
		return self.nextEl

testNode = Node(1,1,1,'airport',1)

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

def checkMove(Map, airplane, move):
	airX = airplane.x
	airY = airplane.y
	fuel = airplane.fuel
	mapWidth = len(Map[0])
	mapHeight = len(Map)
	if airX == 0 and airY == 0 and move == ('up' or 'left'):
		return false
	elif airX == 0 and move == 'left':
		return false
	elif airX == mapWidth and move == 'right':
		return false
	elif airY == 0 and move == 'up':
		return false
	elif airY == mapHeight and move == 'down':
		return false
	elif move == 'up' and fuel - Map[airY+1][airX] < 0:
		return false
	elif move == 'down' and fuel - Map[airY-1][airX] < 0:
		return false
	elif move == 'right' and fuel - Map[airY][airX+1] < 0:
		return false
	elif move = 'left' and fuel - Map[airY][airX-1] < 0:
		return false
	else
		return true

	
def printOut(startingMap):
	output = ""
	test = []
	for eachRow in startingMap:
		test.append(eachRow)
		for element in eachRow:
			output = output + element
	return test

"""
This function finds the coordinates of the air plane
and fuel
"""
def planeFinder(startingMap,item):
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


"""
Beginning to implement A star algorithm
"""
def astar (node,start,goal): #start and goal will be coordinates
	frontier = []
	frontier.put(start,0);
	closedList = []
	accumulated_cost = []
	openList = None
	"""if(accumulated_cost + currentFuelCost > OurTotalFuel)
	{
		return false;
	}
	else if (node.type == airport)
	{
		return true;
	}
	if(nodeToGrab is in closedList)
	{
		#IGNORE THIS NODE
	}
	"""
	


input1 = readFile(inputFile)
out = printOut(input1)
location = planeFinder(input1,values)
print "X is %d " %(location.x)
print "Y is %d " % (location.y)



"""
Sample code for heap in python
pushing and adding to heap
"""

heap = []
testNode = Node(location.x,location.y,10,'airplane',2)
testNode2 = Node(5,5,5,'airport',3)
heapq.heappush(heap,testNode)
heapq.heappush(heap,testNode2)
#heapq.heapify(heap)
getValue = heapq.heappop(heap)
getValue2 = heapq.heappop(heap)

print getValue.y


