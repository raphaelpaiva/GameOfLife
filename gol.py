import pygame
import numpy as np
import json
import sys

from copy import deepcopy

import utils

FPS = 30                             # Frames per second.
DEFAULT_BOARD_SIZE = (80, 80)        # Board size. Only square boards are supported for now.
DEFAULT_SCREEN_SIZE = (800, 800)      # Default Screen size
DEFAULT_CELL_SIZE = 10               # "Zoom". It grows the cells so they are more easily visible.
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

    np.random.seed()

  def _generate_random_board(self, cell_life_probability=None):
    if cell_life_probability is None:
      p = self.cell_life_probability
    else:
      p = cell_life_probability

    self.generation_count = 0
    return np.random.choice(a=[True, False], size=self.board_size, p=[p, 1 - p])
  
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

class Plotter(object):
  def __init__(self, game, cell_size=DEFAULT_CELL_SIZE, screen_size=DEFAULT_SCREEN_SIZE):
    self.game = game
    self.cell_size = cell_size
    
    self.running = True
    
    self.screen_size = DEFAULT_SCREEN_SIZE
    self.screen = pygame.display.set_mode(self.screen_size)

  def run(self):
    pygame.init()
    clock = pygame.time.Clock()
    pygame.font.init()
    system_default_font = pygame.font.get_default_font()
    self.font = pygame.font.SysFont(system_default_font, 30)
    
    while self.running:
      clock.tick(FPS)
      self._handle_events()
      self._plot()
      self._update_game()
      

    pygame.quit()

  def _handle_events(self):
    if pygame.event.get(eventtype=pygame.QUIT):
      self._exit()

    key_events = pygame.event.get(eventtype=pygame.KEYDOWN)
    for key_event in key_events:
      if key_event.key == pygame.K_SPACE:
        self.game.board = self.game._generate_random_board()
      if key_event.key == pygame.K_ESCAPE:
        self._exit()

    mouse_events = pygame.event.get(eventtype=pygame.MOUSEBUTTONDOWN)
    for mouse_event in mouse_events:
      if mouse_event.button == 4: # Mousewheel up
        self.cell_size += 1
      if mouse_event.button == 5: # Mousewheel down
        self.cell_size -= 1
  
  def _exit(self):
    self.running = False

  def _update_game(self):
    self.game.update_board()

  def _plot(self):
    self._plot_board()
    
    textsurface = self.font.render(f"Generation: {self.game.generation_count}", False, (255, 0, 255))
    
    self.screen.blit(textsurface, (0, 0))

    pygame.display.flip()

  def _plot_board(self):
    self.screen.fill((255,255,255))
    board = self.game.board

    for line in range(len(board)):
      for column in range(len(board[line])):
        if board[line][column]:
          cell_rect = pygame.Rect(column * self.cell_size, line * self.cell_size, self.cell_size, self.cell_size)
          pygame.draw.rect(self.screen, 0, cell_rect)

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

  game = GameOfLife(initial_board=initial_board)

  plotter = Plotter(game=game)

  plotter.run()

if __name__ == '__main__':
  main()