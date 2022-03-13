'''
About: COMP3608 Assignment 1

----------------------------------------------------------------------------------------------------
Actions that the game can take when generating it.
----------------------------------------------------------------------------------------------------

'''
from game_setup import *
import numpy as np

ROW = 6 # These are constant for the board.
COLUMN = 7
PLAYER_RED = 'r'
PLAYER_YELLOW = 'y'

def is_sequence_horizontal(i, j, count, player, array_board):
	'''Checks whether horizontal sequence of length count for player'''
	
	if(within_range(i, j-1) and array_board[i][j-1] == player):
		return 0 # Current token is part of previous sequence
	if(within_range(i, j+count) and array_board[i][j+count] == player):
		return 0 # Part of longer sequence.
	track = 0
	for step in range(0, count):
		if(within_range(i, j+step)):
			if(array_board[i][j+step] != player):
				return 0
			track +=1 # To ensure if only 1 token at end, doesn't break
	
	if(track != count):
		return 0
	return 1


def is_sequence_vertical(i, j, count, player, array_board):
	'''Checks whether vertical sequence of length count for player'''
	
	if(within_range(i-1, j) and array_board[i-1][j] == player):
		return 0 # Current token is part of previous sequence
	
	if(within_range(i+count, j) and array_board[i+count][j] == player):
		return 0 # Part of longer sequence.
	track = 0
	for step in range(0, count):
		if(within_range(i+step, j)):
			if(array_board[i+step][j] != player):
				return 0
			track +=1 # To ensure if only 1 token at end, doesn't break
	
	if(track != count):
		return 0
	return 1


def is_sequence_right_diagonal(i, j, count, player, array_board):
	'''Checks whether right diagonal sequence of length count for player'''
	
	if(within_range(i-1, j-1) and array_board[i-1][j-1] == player):
		return 0 # Current token is part of previous sequence
	
	if(within_range(i+count, j+count) and array_board[i+count][j+count] == player):
		return 0 # Part of longer sequence.
	track = 0
	for step in range(0, count):
		if(within_range(i+step, j+step)):
			if(array_board[i+step][j+step] != player):
				return 0
			track +=1 # To ensure if only 1 token at end, doesn't break
	
	if(track != count):
		return 0
	return 1


def is_sequence_left_diagonal(i, j, count, player, array_board):
	'''Checks whether left diagonal sequence of length count for player'''
	
	if(within_range(i-1, j+1) and array_board[i-1][j+1] == player):
		return 0 # Current token is part of previous sequence


	if(within_range(i+count, j-count) and array_board[i+count][j-count] == player):
		return 0 # Part of longer sequence.

	track = 0
	for step in range(0, count):
		if(within_range(i+step, j-step)):
			if(array_board[i+step][j-step] != player):
				return 0
			track +=1 # To ensure if only 1 token at end, doesn't break
	
	if(track != count):
		return 0
	return 1


def NUM_IN_A_ROW(count, array_board, player):
	'''Computes the number in a row for a player with a given state.'''
	num_vert = 0
	num_hor = 0
	num_diag_r = 0
	num_diag_l = 0
	for i in range(0, ROW):
		for j in range(0, COLUMN):
			if(array_board[i][j] == player):
				# We found a sequence to begin
				num_hor += is_sequence_horizontal(i, j, count, player, array_board)
				num_vert += is_sequence_vertical(i, j, count, player, array_board)
				num_diag_r += is_sequence_right_diagonal(i, j, count, player, array_board)
				num_diag_l += is_sequence_left_diagonal(i, j, count, player, array_board)
	
	return (num_hor + num_vert + num_diag_r + num_diag_l)


def COUNT_ALL(array_board, player):
	'''Count all the winning moves.'''
	final_result = 0
	for i in range(0, ROW):
		for j in range(0, COLUMN):
			if(array_board[i][j] == player):
				for count in range(2, 5):					
					num_vert = 0
					num_hor = 0
					num_diag_r = 0
					num_diag_l = 0
					# We found a sequence to begin
					num_hor += is_sequence_horizontal(i, j, count, player, array_board)
					num_vert += is_sequence_vertical(i, j, count, player, array_board)
					num_diag_r += is_sequence_right_diagonal(i, j, count, player, array_board)
					num_diag_l += is_sequence_left_diagonal(i, j, count, player, array_board)
					# Multiply result by multiple.
					final_result = final_result + ((num_hor + num_vert + num_diag_l + num_diag_r)*(10**(count-1)))

	return final_result + count_total_tokens(array_board, player)


def SCORE(array_board, player):
	'''Computes the SCORE of a player.'''
	#return count_total_tokens(array_board, player) + (10*NUM_IN_A_ROW(2, array_board, player)) + (100*NUM_IN_A_ROW(3, array_board, player)) + (1000*NUM_IN_A_ROW(4, array_board, player))
	return COUNT_ALL(array_board, player)

def count_total_tokens(array_board, player):
	'''Count total number of tokens player has on board'''
	count = 0
	for i in range(0, ROW):
		for j in range(0, COLUMN):
			if(array_board[i][j] == player):
				count += 1
	return count


def valid_moves(array_board):
	'''Figures out valid moves from NUMPY array and stores coordinates.'''
	moves_can_make = []
	for j in range(0, COLUMN):
		for i in range(0, ROW):
			if(array_board[i][j] == '.'):
				moves_can_make.append((i, j))
				break
	return moves_can_make


def EVALUATION(array_board, PLAYER):
	'''Evaluates the state.'''
	if PLAYER == PLAYER_RED:
		return SCORE(array_board, PLAYER_RED) - SCORE(array_board, PLAYER_YELLOW)
	else:
		return SCORE(array_board, PLAYER_YELLOW) - SCORE(array_board, PLAYER_RED)