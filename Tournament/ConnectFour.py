'''
About: COMP3608 Assignment 1

----------------------------------------------------------------------------------------------------
Tournament mode for COMP3608.
----------------------------------------------------------------------------------------------------

'''
import sys
from game_setup import * # Contains all functions to set up game
from game_actions import *
from state import *
from minmax import *
from alpha_beta import *

def main():

	initial_state = start_game()
	board = create_board(initial_state['board_state'])
	# Create game tree.
	root = create_tree(3, board, initial_state['player'])

	# For first round move.
	if first_move(board, initial_state['player']) == True:
		return
	else:
		# Alpha Beta
		value = alpha_beta(root, 3, -100000000, 100000000,  True, root.player, 0)
		for i, node in enumerate(root.children):
			if node.value == value[0]:
				if board[5][i] == '.':
					# Make sure not playing invalid position.
					print(i)
					return

		# Unable to play any moves so play random moves from the top.
		for i in range(5, -1, -1):
			for j in range(6, -1, -1):
				if board[i][j] == '.' and board[i-1][j] != '.':
					print(j)
					return

if __name__ == '__main__':
	main()
