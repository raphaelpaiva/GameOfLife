import numpy
from copy import deepcopy

DEFAULT_BOARD_SIZE = (200, 200)        # Board size. Only square boards are supported for now.
DEFAULT_CELL_LIFE_PROBABILITY = 0.10 # Probability of randomly generating a live cell when a new board is constructed.

DIRECTIONS = [
  (-1,-1), (-1, 0), (-1, 1),
  (0, -1),          (0,  1),
  (1, -1), (1,  0), (1,  1),
]

class GameOfLife(object):
  def __init__(self, board_size=DEFAULT_BOARD_SIZE, initial_board=None, cell_life_probability=DEFAULT_CELL_LIFE_PROBABILITY, wrap_board=True):
    self.cell_life_probability = cell_life_probability
    self.wrap = wrap_board
    self.generation_count = 0
    
    if initial_board is None:
      self.board_size = board_size
      self.board = self._generate_random_board(cell_life_probability)
    else:
      self.board = initial_board
      self.board_size = (len(self.board), len(self.board))

    numpy.random.seed()

  def _generate_random_board(self, cell_life_probability=None):
    if cell_life_probability is None:
      p = self.cell_life_probability
    else:
      p = cell_life_probability

    self.generation_count = 0
    return numpy.random.choice(a=[True, False], size=self.board_size, p=[p, 1 - p])
  
  def update_board(self):
    new_board = deepcopy(self.board)
    
    for i in range(len(self.board)):
      for j in range(len(self.board[i])):
        cell_alive = self.board[i][j]
        neighbours = self._count_neighbours(i, j)
        if cell_alive:
          if neighbours < 2 or neighbours > 3:
            new_board[i][j] = False
        else:
          if neighbours == 3:
            new_board[i][j] = True
    self.board = new_board
    self.generation_count += 1
    return self.board

  def _count_neighbours(self, i, j):
    neighbours = 0
    
    for direction in DIRECTIONS:
      ni = (i + direction[0]) 
      nj = (j + direction[1]) 
      
      if self.wrap:
       ni %= self.board_size[0]
       nj %= self.board_size[1]
      elif (ni > self.board_size[1] - 1) or (nj > self.board_size[0] - 1) or ni < 0 or nj < 0:
        # Do not wrap the board
        continue
      
      if self.board[ni][nj]:
        neighbours += 1

    return neighbours
