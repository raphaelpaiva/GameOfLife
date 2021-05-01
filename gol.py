import numpy
from numpy.typing import ArrayLike

from typing import Tuple
from copy import deepcopy

DEFAULT_BOARD_SIZE = (100, 100)      # Board size. Only square boards are supported for now.
DEFAULT_CELL_LIFE_PROBABILITY = 0.10 # Probability of randomly generating a live cell when a new board is constructed.

BoardSize_t = Tuple[int, int]

# y,x or lines,columns
DIRECTIONS = [
  (-1,-1), (-1, 0), (-1, 1),
  (0, -1),          (0,  1),
  (1, -1), (1,  0), (1,  1),
]

class Board(object):
  def __init__(self, size: BoardSize_t = DEFAULT_BOARD_SIZE, initial_state: ArrayLike = None, cell_life_probability: float = DEFAULT_CELL_LIFE_PROBABILITY):
    if initial_state is None:
      self.size = size
      self.state = self.Random(cell_life_probability).state
    else:
      self.state = initial_state
      self.size = (len(self.state), len(self.state[0]))
    
    self.height = self.size[0]
    self.width = self.size[1]
    self.quadrants = self.partition(0, 0, self.size)

  @staticmethod
  def partition(i_start: int, j_start: int, size: BoardSize_t):
    lines, columns = size
    midpoint_i = i_start + int(lines / 2)
    midpoint_j = j_start + int(columns / 2)
    endpoint_i = i_start + lines
    endpoint_j = j_start + columns

    #----+----+
    #  1 |  2 |
    #----+----+
    #  3 |  4 |
    #----+----+
    return [
      (i_start, midpoint_i - 1,      j_start, midpoint_j - 1), # first quadrant
      (i_start, midpoint_i - 1,      midpoint_j, endpoint_j - 1), # second quadrant
      (midpoint_i, endpoint_i - 1,   j_start, midpoint_j - 1), # third quadrant
      (midpoint_i, endpoint_i - 1,   midpoint_j, endpoint_j - 1)  # fourth quadrant
    ]

  @staticmethod
  def Random(size: BoardSize_t = DEFAULT_BOARD_SIZE, cell_life_probability: float = DEFAULT_CELL_LIFE_PROBABILITY):
    p = cell_life_probability
    
    numpy.random.seed()
    random_board = numpy.random.choice(a=[1, 0], size=size, p=[p, 1 - p])
    
    return Board(size, random_board)

class GameOfLife(object):
  def __init__(self, board_size=DEFAULT_BOARD_SIZE, initial_board: Board = None, cell_life_probability: float = DEFAULT_CELL_LIFE_PROBABILITY, wrap_board=True, max_depth: int = 3):
    self.cell_life_probability = cell_life_probability
    self.wrap = wrap_board
    self.generation_count = 0
    self.max_depth = max_depth
    
    if initial_board is None:
      self.board = Board.Random(board_size, self.cell_life_probability)
    else:
      self.board = initial_board
  
  def update_board(self):
    new_board = deepcopy(self.board)

    lines, columns = self.board.size

    if self.max_depth == 0:
      quadrants = [(0, self.board.width - 1, 0, self.board.height - 1)]
    else:
      quadrants = self.board.partition(0, 0, self.board.size)
    for quadrant in quadrants:
      self._analyze_quadrant(quadrant, new_board, 1)
    
    self.board = new_board
    self.generation_count += 1

    return self.board

  def _analyze_quadrant(self, quadrant, new_board, depth):
    i_start, i_stop, j_start, j_stop = quadrant
    lines, columns = (i_stop - i_start) + 1, (j_stop - j_start) + 1
    size = (lines, columns)
    
    live_cell_count = self.board.state[i_start:i_stop + 2,j_start:j_stop + 2].sum() # nasty + 2.

    if live_cell_count > 0:
      if depth >= self.max_depth:
          self._analyze_range(quadrant, new_board)
      else:
        quadrants = self.board.partition(i_start, j_start, size)
        for new_quadrant in quadrants:
          self._analyze_quadrant(new_quadrant, new_board, depth + 1)

  def _analyze_range(self, arange, new_board):
    i_start, i_stop, j_start, j_stop = arange
    lines, columns = (i_stop - i_start) + 1, (j_stop - j_start) + 1

    for i in range(lines):
      line = i + i_start
      for j in range(columns):
        column = j + j_start
        cell_alive = self.board.state[line][column]
        neighbours = self._count_neighbours(line, column)
        if cell_alive:
          if neighbours < 2 or neighbours > 3:
            new_board.state[line][column] = 0
        else:
          if neighbours == 3:
            new_board.state[line][column] = 1

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
