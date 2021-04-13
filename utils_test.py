import unittest
import utils
import gol
import numpy

class UtilsTest(unittest.TestCase):

  def test_load_board(self):
    expected_state = numpy.array([
      [0,1,0,1,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,1,0,0,1,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
    ])

    testboard = utils.load_board('scenarios/testboard2.bmp')

    state_comparison = expected_state == testboard.state

    self.assertTrue(state_comparison.all())

  def test_dump_board(self):
    filename = 'tests/test_dump_board.bmp'
    control_state = numpy.array([
      [0,1,0,1,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,1,0,0,1,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
    ])

    control_board = gol.Board(initial_state=control_state)
    utils.dump_board(board=control_board, filename=filename)
    loaded_board = utils.load_board(filename)

    state_comparison = control_board.state == loaded_board.state

    self.assertTrue(state_comparison.all(), state_comparison)

  def test_dump_board_quadrant(self):
    filename = 'tests/test_dump_board_quadrant'
    control_state = numpy.array([
      [0,1,0,1,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,1,0,0,1,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
    ])
    expected_quadrants = [
      (0, 1, 0, 4), (0, 1, 5, 9),
      (2, 4, 0, 4), (2, 4, 5, 9)
    ]

    control_board = gol.Board(initial_state=control_state)
    self.assertEquals(control_board.quadrants, expected_quadrants)

    q1 = control_state[0:2,0:5]
    q2 = control_state[0:2,5:10]
    q3 = control_state[2:5,0:5]
    q4 = control_state[2:5,5:10]

    control_quadrants = [ 
      q1, q2,
      q3, q4
    ]

    for i in range(len(control_board.quadrants)):
      quadrant = control_board.quadrants[i]
      quadrant_filename = f'{filename}_q{i+1}.bmp'
      utils.dump_board(control_board, quadrant_filename, quadrant=quadrant)
      
      quadrant_board = utils.load_board(quadrant_filename)
      quadrant_comparison = control_quadrants[i] == quadrant_board.state
      self.assertTrue(quadrant_comparison.all(), f'q={i+1}\n{quadrant_comparison}')

if __name__ == '__main__':
  unittest.main()