import sys

import utils
from gol import GameOfLife
from plotter import Plotter

def _load_board_from_file():
  if len(sys.argv) <= 1:
    return None
  
  filename = sys.argv[1]
  try:
      return utils.load_board(filename)
  except Exception as e:
    print(f'Failed to load {filename}.')
    print(e)
    return None

def main():
  initial_board = _load_board_from_file()
  
  if initial_board is None:
    print('Generating random board...')

  print(
    """
    A Simple Conway's Game of Life implementation.
    
    You can tweak the Games' parameters in the source file.

    You can pass a json file as a initial state. Only square matrices are supported. Check the example at scenarios/blinker.json

    Press Space at any time to generate a random board.
    """
  )

  game = GameOfLife(
    initial_board=initial_board,
    board_size=(300,300),
    cell_life_probability=0.1,
    max_depth=0,
    wrap_board=False
  )

  plotter = Plotter(game=game)

  plotter.run()

if __name__ == '__main__':
  main()