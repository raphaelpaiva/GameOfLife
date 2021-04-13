from PIL import Image
import numpy

import json
from gol import GameOfLife, Board

def load_board_json(filename):
  with open(filename) as f:
      return json.load(f)

def dump_board(board: Board, filename: str, quadrant=None):
  if quadrant:
    i_start, i_stop, j_start, j_stop = quadrant
    lines, columns = (i_stop - i_start) + 1, (j_stop - j_start) + 1
  else:
    lines, columns = board.size
    i_start = j_start = 0

  img = Image.new(mode='RGB', size=(columns, lines), color='white')
  pixels = img.load()

  for i in range(lines):
    for j in range(columns):
      if board.state[i + i_start][j + j_start]:
        img.putpixel((j, i), (0, 0, 0))
      j += 1
    i += 1
    
  img.save(filename, format='bmp')

def json_to_bmp(json_filename, bmp_filename):
  board = load_board_json(json_filename)
  dump_board(board, bmp_filename)

def load_board(filename):
  img = Image.open(filename)
  img.load()

  columns, lines = img.size
  board_state = numpy.zeros(shape=(lines, columns), dtype=int)

  for i in range(lines):
    for j in range(columns):
      board_state[i][j] = img.getpixel((j, i)) == (0, 0, 0)

  return Board(initial_state=board_state)

def generate_test_board(size: int):
  game = GameOfLife(board_size=(size, size))
  dump_board(game.board, f'testboard_{size}.bmp')

def print_quadrants(board_filename: str):
  board = load_board(board_filename)

  for i in range(len(board.quadrants)):
    quadrant = board.quadrants[i]
    dump_board(board=board, quadrant=quadrant, filename=f'{board_filename}_q{i+1}.bmp')

if __name__ == '__main__':
  print_quadrants('scenarios/testboard.bmp')