#Shivangi Shakya
#Divya Barsode
#Mohit Bishnoi

from games import *

class GameOfNim(Game):
    """Play GameOfNim, with Max (first player) and Min (second player).
    A state has the player to move, a cached utility, a list of moves in
    the form of a list of (x, y) positions, and a board, in the form of
    list with each row indicating the number of enteries in it."""

    def __init__(self, board):
        """takes the initial board position and creates the initial GameState"""
        moves = list()
        for x in range(len(board)):
            for y in range(1, board[x]+1):
                moves.append((x, y))
        self.initial = GameState(to_move='MAX', utility=0, board=board, moves=moves)

    def actions(self, state):
        """returns a list of valid actions in the given state."""
        return state.moves

    def result(self, state, move):
        if move not in state.moves:
            return state  # Illegal move has no effect
        """returns the new state reached from the given state and the given move."""
        board = state.board.copy()
        board[move[0]] = board[move[0]] - move[1]
        
        moves = list()
        for x in range(len(board)):
            for y in range(1, board[x]+1):
                moves.append((x, y))
        
        return GameState(to_move=('MIN' if state.to_move == 'MAX' else 'MAX'),
                         utility=state.utility,board=board, moves=moves)

    def utility(self, state, player):
        """Return the value to player; 1 for win, -1 for loss, 0 otherwise."""
        result = all(element == 0 for element in state.board)
        if (result == True and state.to_move=='MAX'):
            return 1
        elif (result == True and state.to_move=='MIN'):
            return -1
        else:
            return 0

    def terminal_test(self, state):
        """A state is terminal if it is won."""
        return all(element == 0 for element in state.board)

    def display(self, state):
        board = state.board
        result = all(element == 0 for element in state.board)
        if not(result):
            print("board: "+ str(board))
        
if __name__ == "__main__":
  nim = GameOfNim(board=[7, 5, 3, 1])
  utility = nim.play_game(alpha_beta_player, query_player) # computer moves first
  if (utility < 0):
    print("MIN won the game")
  else:
    print("MAX won the game")

