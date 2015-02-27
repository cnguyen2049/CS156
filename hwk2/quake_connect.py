""" A python module to play a variant of the popular Connect Four game.
"""
import sys
import copy
import random as rand

bottom_row = "|1|2|3|4|5|6|7|"
empty_row = '| | | | | | | |'
null_row = [0,0,0,0,0,0,0]

"""
I am thinking we can represent the board like this
0 if its empty and we can change the value to X or O
given the situation

"""
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

class GameBoard(object):
    """ A game board object.
    """
    def __init__(self, width=7, init_height=6):
        """ height_map: A variable to store the use height of the
                columns of the board.
            the_board: A list of lists which represents the board.
        """
        self.row_gen = lambda num_cols: [0 for val in range(num_cols)]
        self.the_board = [self.row_gen(width) for row in range(init_height)]
        self.height_map = self.row_gen(width)
        self.width = width

    def __repr__(self):
        map_str = '['
        for cnt, row in enumerate(self.the_board):
            if cnt == 1:
                map_str += '{}\n'.format(row)
            elif cnt != len(self.the_board) - 1:
                map_str += ' {}\n'.format(row)
            else:
                map_str += ' {}]\n'.format(row)
        return map_str

    def __str__(self):
        return self.__repr__()

    def insert(self, column_num, value):
        """ column_number: The Zero left aligned column index to insert value
            value: The value to be inserted
        """
        # Insert a new row if we're at the top of this column_num
        col_height = self.height_map[column_num] 
        if col_height == len(self.the_board):
            self.the_board.insert(0, self.row_gen(self.width))
        col_index = col_height + 1
        row_index = len(self.the_board) - col_index
        self.the_board[row_index][column_num] = value
        self.height_map[column_num] += 1



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


def win_horizontal(Node, symbol,num):
    """
    Find the winning state
    """
    count = 0
    # check horizontal winning positions
    for n in the_board:
        for el in n:
            if(el == symbol):
                count += 1
            else:
                count = 0
            if count == num:
                return True
    return False

def win_vertical(the_board,symbol,num):
    """
    Find winning state for vertical
    """
    count = 0
    for i in range(7):
        for n in the_board:
            if n[i] == symbol:
                count += 1
            else:
                count = 0
            if count == 4:
                return True
    return False

def check_diagonal(the_board,symbol):
    height = len(the_board)
    for row in range(height-3):
        for col in range(4):
             if(the_board[row][col] == 1 and the_board[row+1][col+1] == 1 and the_board[row+2][col+2] == 1 and the_board[row+3][col+3] == 1):
                 return True
    for row in range(height-1,2,-1):
        for col in range(0,3):
             print (row,col)
             #print row+1,col+1
             if(the_board[row][col] == 1 and the_board[row-1][col+1] == 1 and the_board[row-2][col+2] == 1 and the_board[row-3][col+3] == 1):
                 return True        
    return False


def print_map(the_board):
    """
    Prints out the map like the Pollet example.
    param: a board state
    """
    row_str = ''
    iterations = 1
    for row in the_board:
        for el in row:
            if(el == 1):
                row_str += '|{}'.format('X')
            elif(el == 2):
                row_str += '|{}'.format('O')
            else:
                row_str += '| '
            if iterations % 7 == 0:
                row_str += '|'
                row_str += '\n'
            iterations += 1
    row_str += bottom_row
    print empty_row
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



G1 = GameBoard()
print G1.__str__()
