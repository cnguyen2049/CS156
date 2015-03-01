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
    def __init__(self, width=7, init_height=6, game_board=None):
        """ height_map: A variable to store the use height of the
                columns of the board.
            the_board: A list of lists which represents the board.
        """
        self.row_gen = lambda num_cols: [0 for val in range(num_cols)]
        if game_board is None:
            self.the_board = [self.row_gen(width) for row in range(init_height)]
            self.height_map = self.row_gen(width)
            self.width = width
        else:
            self.the_board = copy.deepcopy(game_board.the_board)
            self.height_map = copy.deepcopy(game_board.height_map)
            self.width = game_board.width

    def __repr__(self):
        map_str = '['
        for cnt, row in enumerate(self.the_board):
            if cnt == 0:
                map_str += '{}\n'.format(row)
            elif cnt != len(self.the_board) - 1:
                map_str += ' {}\n'.format(row)
            else:
                map_str += ' {}]\n'.format(row)
        return map_str

    def __str__(self):
        return self.__repr__()

    def earthquake(self):
        """ A function to cause an earthquake.
        """
        base_row = self.the_board.pop(len(the_board)-1)
        for cnt, b_row in enumerate(base_row):
            if b_row != 0:
                self.height_map[cnt] -= 1
        del base_row

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
    Node for each game state. I am thinking we can just store the state in
    lists of lists ( each row represents a row ) and we can easily delete the
    first row by popping. We can also append the new rows by simply
    appending to the state list.
    """

    def __init__(self, parent=None):
        """ Inputs:
        parent: a parent GameNode() object of this GameNode.
        This copies the state of <parent> into self.node_board since the child
        has the configuration of the parent plus one move.
        """
        self.state = []
        self.alpha = 0
        if type(parent) is GameNode:
            self.parent = parent
            self.node_board = GameBoard(game_board=parent.node_board)
        else:
            # If we're the root node, set parent to our own reference.
            self.parent = self
            self.node_board = GameBoard()
            # If no parent.  We're first.

    def getState(self):
        return self.state

    def getParent():
        return self.parent

def get_heuristic(the_board, symbol, row_index, column_index):
    """ A function to find the maximum heuristic for a particular position
    and particular players symbol at a specific location of the board.
    Inputs:
        the_board- A nested list of list object representing the board.
        symbol   - The symbol whose heuristic is to be calculated.
        row_index- The index of the list which represents the row.
        column_index- The index of the column to check
    """
    if the_board[row_index][column_index] != symbol:
        return 0
    heuristics = []
    heuristics.append(heuristic_horizontal(the_board, symbol, row_index, column_index))
    heuristics.append(heuristic_vertical(the_board, symbol, row_index, column_index))
    heuristics.append(heuristic_diagonal(the_board, symbol, row_index, column_index))
    return max(heuristics)

def heuristic_horizontal(the_board, symbol, row_index, column_index):
    """ A Method which only checks the number of symbol to the right of indexes.
    Inputs:
        the_board- A nested list of list object representing the board.
        symbol   - The symbol whose heuristic is to be calculated.
        row_index- The index of the list which represents the row.
        column_index- The index of the column to check
    """
    r_ind, c_ind = row_index, column_index
    # Ignore symbols we don't care about.
    this_symbol = lambda: the_board[r_ind][c_ind] == symbol 
    # Don't exceed the right side of the rows of the_board.
    right_bound = lambda: c_ind < len(the_board[r_ind])
    heuristic = 0
    while(this_symbol() and right_bound()):
        heuristic += 1
        c_ind += 1
    return heuristic

def heuristic_vertical(the_board, symbol, row_index, column_index):
    """ A Method which only checks the number of symbol above the indexes.
    Inputs:
        the_board- A nested list of list object representing the board.
        symbol   - The symbol whose heuristic is to be calculated.
        row_index- The index of the list which represents the row.
        column_index- The index of the column to check
    """
    r_ind, c_ind = row_index, column_index
    # Ignore symbols we don't care about.
    this_symbol = lambda: the_board[r_ind][c_ind] == symbol 
    # Don't exceed the size of the columns of the_board
    upper_bound = lambda: r_ind >= 0 
    heuristic = 0
    while(this_symbol() and upper_bound()):
        heuristic += 1
        r_ind -= 1
    return heuristic

def heuristic_diagonal(the_board, symbol, row_index, column_index):
    """ A Method which checks the number of symbol to the upper diagonals of indexes.
    Inputs:
        the_board- A nested list of list object representing the board.
        symbol   - The symbol whose heuristic is to be calculated.
        row_index- The index of the list which represents the row.
        column_index- The index of the column to check
    """
    # Ignore symbols we don't care about.
    this_symbol = lambda: the_board[r_ind][c_ind] == symbol 
    # Boundary booleans.  Don't exceed the limits of the matrix.
    right_bound = lambda: c_ind < len(the_board[r_ind])  
    upper_bound = lambda: r_ind >= 0 
    left_bound = lambda: c_ind >= 0 
    left_heuristic, right_heuristic = 0, 0
    # Check left diagonal.
    r_ind, c_ind = row_index, column_index
    while(this_symbol() and left_bound() and upper_bound()):
        left_heuristic += 1
        # Up left is actually left one and up one, hince r_ind -=1
        c_ind -= 1
        r_ind -= 1

    # Check right diagonal.
    r_ind, c_ind = row_index, column_index
    while(this_symbol() and right_bound()  and upper_bound()):
        right_heuristic += 1
        # Up right is actually to the right one and up one, hince r_ind -=1
        c_ind += 1
        r_ind -= 1
    return max([left_heuristic, right_heuristic])


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
    height = the_board.node_board
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

def get_winner(the_board,symbol):
    if check_diagonal(the_board,symbol) == True or win_vertical(the_board,symbol) == True or win_horizontal(the_board,symbol) == True:
        return True
    return False 

def earthquake():
    "Roll the dice function"
    num = randInt(1,6)
    if num == 6:
        return True
    return False


def print_map(the_board):
    """
    Prints out the map like the Pollet example.
    param: a board state
    """
    value_map = {0:' ', 1:'X', 2:'O'}
    row_str = ''
    iterations = 1
    for row in the_board:
        for el in row:
            row_str += '|{}'.format(value_map[el])
            if iterations % 7 == 0:
                row_str += '|\n'
            iterations += 1
    row_str += bottom_row
    print empty_row
    print row_str

def human_player():
    prompt_start = 'Please enter a slot from 1 to 7 for your move: '
    print prompt_start, 
    invalid = True
    while(invalid):
        try:
            start_slot = int(raw_input(''))
            if start_slot <= 0 or start_slot > 7:  # Burp if out of range.
                raise ValueError('Invalid position')
            invalid = False
        except ValueError:
            print 'Invalid Input.  Enter a slot from 1 to 7: ', 
            invalid = True
    return start_slot-1

def computer_player():
    return rand.randint(0, 6)


class ConnectFour(object):

    """ A python class to do something for our assignment.
    """
    fmat_row = '|{}|{}|{}|{}|{}|{}|{}|'
    empty_row = '| | | | | | | |'
    base_row = '|1|2|3|4|5|6|7|'
    # A map to assign the Character symbols to the value.
    player_map = {0:'', 1:'X', 2:'O'}
    # A Map to flip the turn. Hopefully Zero will cause an exception.
    opposite_turn = {0:0, 1:2, 2:1}
    first_player, second_player = 1, 2
    player_map = {}
    root_depth = 0

    def __init__(self, player_first=False, indicate_quake=False):
        """ Inputs:
                player_first: Boolean True condition for the player to go
                    first or False for computer to go first.
              indicate_quake: Boolean True for computer to indicate when
                    a quake happens or False to ask if a quake happened.
        """
        player_1, player_2 = self.first_player, self.second_player
        self.root_state = GameNode()
        self.tree_map = {}
        self.turn_map = {}
        self.turn = player_1
        if player_first:
            self.player_map = {player_1: human_player, player_2: computer_player}
            self.move_map = {player_1:'Your Move', player_2:'My Move'}
            start_slot = self.player_map[player_1]() # Key out the function.
            self.insert(start_slot, player_1)
            self.print_map()
        else:
            self.player_map = {player_1: computer_player, player_2: human_player}
            self.move_map = {player_1:'My Move', player_2:'Your Move'}
            start_slot = 3 # The middle is the best possible opening move.
            self.insert(start_slot, player_1)
            self.print_map()
        self.state_machine()

    def print_map(self):
        """ A function to print the map in it's current state.
        """
        this_move = self.move_map[self.turn]
        print 'Board After {}:'.format(this_move)
        print_map(self.root_state.node_board.the_board)

    def insert(self, column, player):
        """ A function to insert a players move in the correct column.
            Inputs:
                player: String with 'X' or 'O'
                column: Integer value with domain [0, 7]
        """
        self.turn = player
        self.root_state.node_board.insert(column, player)

    def state_machine(self):
        """ A fucntion to handle the turn taking process between player
        and the algorithm.
        """
        self.turn = self.opposite_turn[self.turn]
        # xrange on the number of turns.
        for cnt in xrange(10):
            move = self.player_map[self.turn]() # Key out the function.
            self.insert(move, self.turn)
            self.print_map()
            self.turn = self.opposite_turn[self.turn]

    def generate_successors(self, depth):
        """ Generate the sucessor tree of the current state of the board with
        <depth> nodes below.
        self.tree_map = {depth_of_tree: [list_of_childeren]}
        # The child of tree_map[depth][N] is tree_map[depth+1][N*7]
        """
        # Clear the map of depths for new tree & the map of whose turn @ depth
        self.tree_map, self.turn_map = {}, {}
        self.turn_map[self.root_depth] = self.turn
        self.tree_map[self.root_depth] = [self.root_state]
        # This is the turn which is opposite to the turn at this state.
        turn_tracker = self.opposite_turn[self.turn]
        depth_tracker = 1
        while(depth_tracker <= depth):
            childeren = []
            for parent in self.tree_map[depth_tracker-1]:
                # Record whose turn it was at this depth.
                self.turn_map[depth_tracker] = turn_tracker
                # Seven childeren for a width of 7 board.
                for cnt in range(7):
                    # Passing the parent node, and the turn at child node.
                    child = GameNode(parent=parent)
                    # Insert the next move for the right turn.
                    child.node_board.insert(cnt, turn_tracker)
                    childeren.append(child)
            # Flip the turn for the next level.
            turn_tracker = self.opposite_turn[turn_tracker]
            self.tree_map[depth_tracker] = childeren
            depth_tracker += 1


if __name__ == '__main__':
    import copy
    ARGS = copy.deepcopy(sys.argv)

C = ConnectFour()

