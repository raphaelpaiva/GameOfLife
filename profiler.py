import cProfile
from pstats import Stats, SortKey

import json
import gol
import utils

TEST_BOARD_FILENAME = 'scenarios/testboard.bmp'

testboard      = utils.load_board(TEST_BOARD_FILENAME)
testboard_size = (len(testboard), len(testboard[0]))

print(
f"""
Profile parameters: 
board file: {TEST_BOARD_FILENAME}
board size: {testboard_size}
"""
)



game = gol.GameOfLife(
  initial_board=testboard
)

with cProfile.Profile() as pr:
  for i in range(1000):
    game.update_board()
pr.print_stats()
