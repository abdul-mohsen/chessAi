# we will use cProfile to get some function call stats
import cProfile, pstats, io
from pstats import SortKey

def random_move(board):
    np.random.choice(list(board.legal_moves))

def play_random_policy(board, num_turns=100):
    for turn in range(num_turns):
        
        if board.outcome() is None:
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
    from games import *
    import chess
    import random
    import numpy as np
    
    np.random.seed(20220813)
    
    # initiliaze a chess games
    board = chess.Board()
    
    # generate random chess board by playing randomly for a couple of turns
    play_random_policy(board, num_turns=25)

    print('The current board is:')
    print(board)
    print('----------------------------------------------------------------------------')
    
    # run h_minimax with profiler to get stats on function calls
    pr = cProfile.Profile()
    pr.enable()
    hval, move = h_minimax(board, depth_limit=4)
    pr.disable()
    s = io.StringIO()
    ps = pstats.Stats(pr, stream=s).sort_stats(SortKey.CALLS).strip_dirs()
    ps.print_stats("h_minimax*|max_node*|min_node*")
    print(s.getvalue())
    print('h_minimax return is hvalue {}, move {}'.format(hval, move))
    
    print('----------------------------------------------------------------------------')
    
    # run h_minimax_alpha_beta with profiler to get stats on function calls
    pr = cProfile.Profile()
    pr.enable()
    hvalab, moveab = h_minimax_alpha_beta(board, depth_limit=4)
    pr.disable()
    s = io.StringIO()
    ps = pstats.Stats(pr, stream=s).sort_stats(SortKey.CALLS).strip_dirs()
    ps.print_stats("h_minimax*|max_node*|min_node*")
    print(s.getvalue())
    print('h_minimax_alpha_beta return is hvalue {}, move {}'.format(hvalab, moveab))