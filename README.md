#GameOfNim:

Python class, GameOfNim, defines the rules of the Game of Nim and can be used to play optimally against any opponent.

~ The class extends class Game in the games.py code.
~ Represent the state by a list which represents the number of objects in each pile/row. E.g., [5, 3, 1] represents 5 objects in the first row, 3 in the second, and 1 in the third row.
~ An action in this game is removing a certain number of objects from one pile. Represent an action by a 2-tuple (r, n) where r represents the row number (start counting from 0 for convenience as Python uses 0-based indexing) and n represents the number of objects to remove. E.g., (1,2) means remove 2 objects from row with index 1 (the second row).

The class is usable in the main function below to print the sequence of actions to reach the goal state.

from games import *

<code>


if __name__ == "__main__":
  nim = GameOfNim(board=[7, 5, 3, 1])
  utility = nim.play_game(alpha_beta_player, query_player) # computer moves first
  if (utility < 0):
    print("MIN won the game")
  else:
    print("MAX won the game")

GameOfNim class have a
1. a constructor which takes the initial board position and creates the initial GameState. A GameState includes all valid moves for that state. For example, if the board position= [0, 2, 3, 1], the valid moves are: [(1, 1), (1, 2), (2, 1), (2, 2), (2, 3), (3, 1)].
2. a method result(state, move) that returns the new state reached from the given state and the given move. The state for a multiplayer game also includes the player whose turn it is to play
3. a method actions(state) that returns a list of valid actions in the given state. 
4. a method terminal_test(state) that returns True if the given state represents the end of a game
5. a method utility(state, player) that returns +1 if MAX wins, -1 if MIN wins (the "names" of the players don't matter but they should be distinct)

Method Game.play_game() in Games.py is modified for printing the bot moves and the board state after that.

