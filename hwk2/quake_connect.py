""" A python module to play a variant of the popular Connect Four game.
"""
import sys
import random as rand

bottom_row = "|1|2|3|4|5|6|7|"
empty_row = [0,0,0,0,0,0,0]

the_board = [[0,0,0,0,0,0,0],  # 7 x infinity
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0]]
"""
My idea is to have each Node represent a state in the game.
-Chris
"""


class GameNode(object):

    """
    Node for each game state. I am thinking we can just store the state in lists of lists ( each row represents a row ) and we can easily delete the first row by popping.
    We can also append the new rows by simply appending to the state list.
    """

    def __init__(self):
        self.state = []
        self.parent = None
        self.alpha
        self.alpha = 0

    def getState(self):
        return self.state

    def getParent():
        return self.parent


def winning_horizontal(Node, symbol):
    """
    Find the winning state
    """
    count = 0
    current = Node.getState()
    # check horizontal winning positions
    for n in current:
        for el in n:
            if(el == symbol):
                count += 1
            else:
                count = 0
            if count == 4:
                return 1
    return 0

def winning_vertical(Node,symbol):
    """
    Find winning state for vertical
    """
    count = 0
    current = Node.getState()
    for i in range(7):
        for n in current:
            if n[i] == symbol:
                count += 1
            else:
                count = 0
            if count == 4:
                return 1
    return 0

def print_map(the_board):
	row_str = ''
	iterations = 1
	for row in the_board:
		for el in row:
			if( el == 'X' or el == 'O'):
				row_str += '|{}'.format(el)
			else:
				row_str += '| '
			#row_str += '|'
			if iterations % 7 == 0:
				row_str += '|'
				row_str += '\n'
			iterations += 1
	print row_str


class ConnectFour(object):

    """ A python class to do something for our assignment.
    """
    fmat_row = '|{}|{}|{}|{}|{}|{}|{}|'
    empty_row = '| | | | | | | |'
    base_row = '|1|2|3|4|5|6|7|'

    def __init__(self, player_first=False, indicate_quake=False):
        """ Inputs:
                player_first: Boolean True condition for the player to go
                    first or False for computer to go first.
              indicate_quake: Boolean True for computer to indicate when
                    a quake happens or False to ask if a quake happened.
        """
        print self.empty_row, '\n', self.base_row
        # Use a Dictionary to store the positions as a First In Queue.
        self.position_map = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: []}
        self.max_height = 1  # Keep track of the max height for printing.

        if player_first:
            prompt_start = 'Please enter a slot from 1 to 7 for your move: '
            start_slot = int(raw_input(prompt_start))
            if start_slot < 0 or start_slot > 7:  # Burp if out of range.
                raise ValueError('Invalid start position')
            self.position_map[start_slot].append('X')
            self.print_map('Your Move')
        else:
            start_slot = rand.randint(0, 7)
            self.position_map[start_slot].append('O')
            self.print_map('My Move')

    def print_map(self, who_move):
        """ A function to print the map in it's current state.
        """
        print 'Board After {}:'.format(who_move)
        print self.empty_row
        for row in range(self.max_height - 1, -1, -1):
            row_str = ''
            for column in range(1, 8):
                value = self.position_map[column]
                if len(value) > row:
                    row_str += '|{}'.format(value[row])
                else:
                    row_str += '| '
            row_str += '|'
            print row_str
        print self.base_row

    def insert_move(self, player, column):
        """ A function to insert a players move in the correct column.
            Inputs:
                player: String with 'X' or 'O'
                column: Integer value with domain [0, 7]
        """
        if player != 'X' and player != 'O':
            raise ValueError('This is not the correct notation for a player.')
        self.position_map[column].append(player)
        column_height = len(self.position_map[column])
        if column_height > self.max_height:
            self.max_height = column_height


if __name__ == '__main__':
    import copy
    ARGS = copy.deepcopy(sys.argv)
