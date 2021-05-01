import cProfile
from pstats import Stats, SortKey

import json
import gol
import utils

TEST_BOARD_FILENAME = 'scenarios/testboard_100_emptyq.bmp'
testboard      = utils.load_board(TEST_BOARD_FILENAME)

print(
f"""
Profile parameters: 
board file: {TEST_BOARD_FILENAME}
board size: {testboard.size}
"""
)

for max_depth in range(3):
  game = gol.GameOfLife(
    initial_board=testboard,
    max_depth=max_depth + 1
  )

  print(f'# Max Depth: {max_depth + 1}')
  print('```')

  with cProfile.Profile() as pr:
    for i in range(1000):
      game.update_board()
  pr.print_stats()
  
  print('```')
