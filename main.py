# we will use cProfile to get some function call stats
import cProfile, pstats, io
from pstats import SortKey

def random_move(board):
    return np.random.choice(list(board.legal_moves))

def play_random_policy(board, num_turns=100):
    for turn in range(num_turns):
        if board.outcome() is not None:
            # Game Ended
            return board

        if turn % 2 == 0:
            #White turn
            
            move = random_move(board)
            board.push(move)
        else:
            #black turn
            
            move = random_move(board)
            board.push(move)
        

if __name__ == "__main__":
    # from games import *
    import chess
    import random
    import numpy as np
    
    np.random.seed(20220813)
    
    # initiliaze a chess games
    board = chess.Board()
    
    # generate random chess board by playing randomly for a couple of turns
    newboard = play_random_policy(board, num_turns=25)

    print('The current board is:')
    print(board)
    print('----------------------------------------------------------------------------')
    