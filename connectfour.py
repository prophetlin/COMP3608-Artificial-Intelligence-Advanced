'''
About: COMP3608 Assignment 1

----------------------------------------------------------------------------------------------------
This is testing purposes and used to modularise the code.
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
	root = create_tree(initial_state['depth'], board, initial_state['player'])
	
	if initial_state['algo'] == 'M':
		# Minimax algorithm.
		value = min_max(root, initial_state['depth'], True, root.player, 0)
		for i, node in enumerate(root.children):
			if node.value == value[0]:
				print(i)
				break
		print(value[1])
	else:
		# Alpha Beta
		value = alpha_beta(root, initial_state['depth'], -100000000, 100000000,  True, root.player, 0)
		for i, node in enumerate(root.children):
			if node.value == value[0]:
				print(i)
				break
		print(value[1])
			

if __name__ == '__main__':
	main()