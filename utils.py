from PIL import Image
import numpy

import json
from gol import GameOfLife, Board

def load_board_json(filename):
  with open(filename) as f:
      return json.load(f)

def dump_board(board: Board, filename: str):

  img = Image.new(mode='RGB', size=board.size, color='white')
  pixels = img.load()

  lines, columns = board.size

  for i in range(lines):
    for j in range(columns):
      if board.state[i][j]:
        pixels[i,j] = (0, 0, 0)
    
  img.save(filename, format='bmp')

def json_to_bmp(json_filename, bmp_filename):
  board = load_board_json(json_filename)
  dump_board(board, bmp_filename)

def load_board(filename):
  img = Image.open(filename)
  img.load()

  lines, columns = img.size
  board_state = numpy.zeros(shape=img.size, dtype=bool)

  for i in range(lines):
    for j in range(columns):
      board_state[i][j] = img.getpixel((i, j)) == (0, 0, 0)

  return Board(initial_state=board_state)

def generate_test_board(size: int):
  game = GameOfLife(board_size=(size, size))
  dump_board(game.board, f'testboard_{size}.bmp')

if __name__ == '__main__':
  generate_test_board(200)