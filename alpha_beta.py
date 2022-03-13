'''
About: COMP3608 Assignment 1

----------------------------------------------------------------------------------------------------
Alpha-Beta Algorithm.
----------------------------------------------------------------------------------------------------

'''
from game_actions import *
from game_setup import *
from game_actions import *

def alpha_beta(node, depth, alpha, beta, maximizing_player, original_player, count):
    '''
    Alpha Beta algorithm for the board.
    '''
    count += 1
    if depth == 0: # Reached the leaf.
        if node.win==True:
            if node.parent.player == original_player:
                node.value = 10000
                return 10000, count
            else:
                node.value = -10000
                return -10000, count
        return EVALUATION(node.board, original_player), count

    # In case we terminate early.
    if node.win==True:
        if node.parent.player == original_player:
            node.value = 10000
            return 10000, count
        else:
            node.value = -10000
            return -10000, count

    if maximizing_player==True:
        best_value = -100000000
        for child in node.children:
            value, count = alpha_beta(child, depth-1, alpha, beta, False, original_player, count)
            child.value = value
            best_value = max(best_value, value)
            alpha = max(best_value, alpha)
            if beta <= alpha:
                break
        return best_value, count

    else:
        best_value = 100000000
        for child in node.children:
            value, count = alpha_beta(child, depth-1, alpha, beta, True, original_player, count)
            child.value = value
            best_value = min(best_value, value)
            beta = min(best_value, beta)
            if beta <= alpha:
                break
        return best_value, count