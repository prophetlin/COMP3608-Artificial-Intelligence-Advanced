'''
About: COMP3608 Assignment 1

----------------------------------------------------------------------------------------------------
Class for the state nodes and building tree.
----------------------------------------------------------------------------------------------------

'''
from game_actions import *

class State():
	def __init__(self, player, board, move, win, full=False, parent=None):
		self.player = player # who's turn to play
		self.board = board
		self.parent = parent # node reference
		self.children = [] # contains all children of this node.
		self.value = 0
		self.move = move # the OG move.
		self.win = win # Check if game is over.
		self.full = full # Still able to play moves.


	def create_children(self):
		'''Create children for the current state.'''
		possible_moves = valid_moves(self.board)
		for move in possible_moves:
			if move == None:
				self.full = True # checks if board full.
				return
			# Create children of this current node.
			self.children.append(create_child(parent=self, move=move, board=np.copy(self.board), player_turn=self.player))


def create_child(parent, move, board, player_turn):
	'''Creates child node by updating move.'''
	turn_to_play = None
	if parent.player == PLAYER_YELLOW: # Get opposite player.
		turn_to_play = PLAYER_RED
	else:
		turn_to_play = PLAYER_YELLOW
	row, column = move
	update_row = list(board[row])
	update_row[column] = player_turn
	board[row] = ''.join(update_row)
	if(NUM_IN_A_ROW(4, board, parent.player)>0):
		# Game won already.
		return State(player=turn_to_play, board=board, move=parent.move, parent=parent, win=True)
	else:
		return State(player=turn_to_play, board=board, move=parent.move, parent=parent, win=False)


def create_tree(depth, board, player_turn):
	'''Build tree of the whole game.'''
	root = State(player_turn, board, move=None, win=False, parent=None)
	i = 0
	recurse_build(root, i, depth)
	return root


def recurse_build(node, current_depth, depth):
	'''Recursively build the tree.'''
	if current_depth == depth: # base case.
		return

	node.create_children() # build children.
	for child in node.children:
		# So that we don't build terminal nodes.
		if child.win == False and child.full == False:
			recurse_build(child, current_depth+1, depth)
