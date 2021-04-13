import pygame

DEFAULT_MAX_FPS     = 30              # Frames per second.
DEFAULT_SCREEN_SIZE = (800, 800)      # Default Screen size
DEFAULT_CELL_SIZE   = 10              # "Zoom". It grows the cells so they are more easily visible.

class Plotter(object):
  def __init__(self, game, cell_size=DEFAULT_CELL_SIZE, screen_size=DEFAULT_SCREEN_SIZE, max_fps=DEFAULT_MAX_FPS):
    self.game = game
    self.cell_size = cell_size
    self.max_fps = max_fps
    
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
      clock.tick(self.max_fps)
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
        self.game.board = self.game.board.Random(size=self.game.board.size, cell_life_probability=self.game.cell_life_probability)
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

    lines, columns = board.size

    for line in range(lines):
      for column in range(columns):
        if board.state[line][column]:
          cell_rect = pygame.Rect(column * self.cell_size, line * self.cell_size, self.cell_size, self.cell_size)
          pygame.draw.rect(self.screen, 0, cell_rect)
