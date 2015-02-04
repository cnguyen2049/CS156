#Shunt
import sys
import heapq

inputFile = sys.argv[1]
#heuristic = sys.argv[2]

values ={'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9}

goal = {'H':'Goal'}

class Node:
	def __init__(self,x,y,fuel):
		self.x = x
		self.y = y
		self.fuel = fuel
		self.nextEl = None
	def get_self(self):	
		return self.fuel;
	def getNext():
		return self.nextEl

testNode = Node(1,1,1)

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
	global startX , startY
	y = 0
	for eachRow in startingMap:
		x = 0
		for column in eachRow:
			for key in values:
				if column == key: 
					startX = x
					startY = y
					return values[key]
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
def astar (node,start,goal): #start and goal will be coordinates
	frontier = []
	frontier.put(start,0);
	closedList = []
	accumulated_cost = []
	openList = None
	if(accumulated_cost + currentFuelCost > OurTotalFuel)
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
	
	


input1 = readFile(inputFile)
out = printOut(input1)
location = planeFinder(input1,values)
print "X is %d " %(startX)
print "Y is %d " % (startY)



"""
Sample code for heap in python
pushing and adding to heap
"""
print location
heap = []
testNode = Node(7,(startX,startY))
testNode2 = Node(5,(5,5))
heapq.heappush(heap,testNode)
heapq.heappush(heap,testNode2)
#heapq.heapify(heap)
getValue = heapq.heappop(heap)[0]
print getValue


