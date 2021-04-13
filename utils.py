from PIL import Image
import numpy

import json
import gol

def load_board_json(filename):
  with open(filename) as f:
      return json.load(f)

def dump_board(board, filename):
  board_dimensions = (len(board), len(board[0]))

  img = Image.new(mode='RGB', size=board_dimensions, color='white')
  pixels = img.load()

  lines, columns = board_dimensions

  for i in range(lines):
    for j in range(columns):
      if board[i][j]:
        pixels[i,j] = (0, 0, 0)
    
  img.save(filename, format='bmp')

def json_to_bmp(json_filename, bmp_filename):
  board = load_board_json(json_filename)
  dump_board(board, bmp_filename)

def load_board(filename):
  img = Image.open(filename)
  img.load()

  lines, columns = img.size
  board = numpy.zeros(shape=img.size, dtype=bool)

  for i in range(lines):
    for j in range(columns):
      board[i][j] = img.getpixel((i, j)) == (0, 0, 0)

  return board

def generate_test_board(size):
  game = gol.GameOfLife(board_size=(size, size))
  dump_board(game.board, f'testboard_{size}.bmp')
