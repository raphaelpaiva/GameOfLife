import numpy
from numpy.typing import ArrayLike

from typing import Tuple
from copy import deepcopy

DEFAULT_BOARD_SIZE = (100, 100)      # Board size. Only square boards are supported for now.
DEFAULT_CELL_LIFE_PROBABILITY = 0.10 # Probability of randomly generating a live cell when a new board is constructed.

# y,x or lines,columns
DIRECTIONS = [
  (-1,-1), (-1, 0), (-1, 1),
  (0, -1),          (0,  1),
  (1, -1), (1,  0), (1,  1),
]

class Board(object):
  def __init__(self, size: Tuple[int, int] = DEFAULT_BOARD_SIZE, initial_state: ArrayLike = None, cell_life_probability: float = DEFAULT_CELL_LIFE_PROBABILITY):
    if initial_state is None:
      self.size = size
      self.state = self.Random(cell_life_probability).state
    else:
      self.state = initial_state
      self.size = (len(self.state), len(self.state))
    
  @staticmethod
  def Random(size: Tuple[int, int] = DEFAULT_BOARD_SIZE, cell_life_probability: float = DEFAULT_CELL_LIFE_PROBABILITY):
    p = cell_life_probability
    
    numpy.random.seed()
    random_board = numpy.random.choice(a=[True, False], size=size, p=[p, 1 - p])
    
    return Board(size, random_board)

class GameOfLife(object):
  def __init__(self, board_size=DEFAULT_BOARD_SIZE, initial_board: Board = None, cell_life_probability: float = DEFAULT_CELL_LIFE_PROBABILITY, wrap_board=True):
    self.cell_life_probability = cell_life_probability
    self.wrap = wrap_board
    self.generation_count = 0
    
    if initial_board is None:
      self.board = Board.Random(board_size, self.cell_life_probability)
    else:
      self.board = initial_board
  
  def update_board(self):
    new_board = deepcopy(self.board)

    lines, columns = self.board.size
    
    for i in range(lines):
      for j in range(columns):
        cell_alive = self.board.state[i][j]
        neighbours = self._count_neighbours(i, j)
        if cell_alive:
          if neighbours < 2 or neighbours > 3:
            new_board.state[i][j] = False
        else:
          if neighbours == 3:
            new_board.state[i][j] = True
    self.board = new_board
    self.generation_count += 1
    return self.board

  def _count_neighbours(self, i, j):
    neighbours = 0
    
    lines, columns = self.board.size

    for direction in DIRECTIONS:
      ni = (i + direction[0]) 
      nj = (j + direction[1]) 
      
      if self.wrap:
       ni %= lines
       nj %= columns
      elif (ni > lines - 1) or (nj > columns - 1) or ni < 0 or nj < 0:
        # Do not wrap the board
        continue
      
      if self.board.state[ni][nj]:
        neighbours += 1

    return neighbours
