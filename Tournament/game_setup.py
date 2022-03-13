'''
About: COMP3608 Assignment 1

----------------------------------------------------------------------------------------------------
Setting up the game for tournament.
----------------------------------------------------------------------------------------------------

'''

import numpy as np
import sys

ROW = 6 # These are constant for the board.
COLUMN = 7
PLAYER_RED = 'r'
PLAYER_YELLOW = 'y'


def start_game():
	'''Initialises the game and return dict.'''
	parameters = sys.argv
	board = parameters[1].split(',')
	player = "" # Who's about to play
	if parameters[2] == 'red':
		player = 'r'
	else:
		player = 'y'
	return {'board_state':board, 'player':player}


def create_board(list_of_states):
	'''Create NUMPY array from list of lists.'''
	return np.array([np.array(row) for row in list_of_states])


def within_range(i, j):
	'''Check if outside of bound.'''
	if i >= ROW or j >= COLUMN or i < 0 or j < 0:
		return False
	return True


def print_board(array_board):
	'''Print out board.'''
	for i in range(ROW-1, -1, -1):
		for j in range(0, COLUMN):
			print(array_board[i][j], end=' ')
		print()