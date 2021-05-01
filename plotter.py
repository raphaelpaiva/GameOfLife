from dataclasses import dataclass
import pygame

DEFAULT_MAX_FPS     = 60              # Frames per second.
DEFAULT_SCREEN_SIZE = (800, 800)      # Default Screen size
DEFAULT_CELL_SIZE   = 10              # "Zoom". It grows the cells so they are more easily visible.

@dataclass
class ViewPort:
  width:  int
  height: int
  pos_x:  int
  pos_y:  int
  step:   int

  def move_left(self):
    self.pos_x -= self.step
    if self.pos_x < 0:
      self.pos_x = 0

  def move_right(self):
    self.pos_x += self.step

  def move_down(self):
    self.pos_y += self.step
  
  def move_up(self):
    self.pos_y -= self.step
    if self.pos_y < 0:
      self.pos_y = 0

  def get_bounds(self, ratio):
    if ratio > 1.0:
      return int((self.pos_x + self.width)  * ratio), int((self.pos_y + self.height) * ratio)
    else:
      return self.pos_x + self.width, self.pos_y + self.height


class Plotter(object):
  def __init__(self, game, cell_size=None, screen_size=DEFAULT_SCREEN_SIZE, max_fps=DEFAULT_MAX_FPS):
    self.game = game
    self.max_fps = max_fps
    self.clock = pygame.time.Clock()

    self.running = True
    self.paused = True
    
    self.screen_size = screen_size
    
    self.screen = pygame.display.set_mode(self.screen_size)

    self.ideal_cell_size = int( self.screen.get_height() / self.game.board.height )
    if cell_size is not None:
      self.cell_size = cell_size
    else:
      self.cell_size = self.ideal_cell_size

    self.viewport = ViewPort(self.game.board.width, self.game.board.height, 0, 0, int(self.cell_size / 4))
    
    self.keypress_events_by_key = {
      pygame.K_EQUALS: self._increase_cell_life_probability,
      pygame.K_MINUS:  self._decrease_cell_life_probability,
      pygame.K_UP:     self.viewport.move_up,
      pygame.K_RIGHT:  self.viewport.move_right,
      pygame.K_DOWN:   self.viewport.move_down,
      pygame.K_LEFT:   self.viewport.move_left
    }

    self.toggle_events_by_key = {
      pygame.K_SPACE:  self._reset,
      pygame.K_ESCAPE: self._exit,
      pygame.K_p:      self._toggle_pause,
      pygame.K_s:      self._update_game
    }

  def run(self):
    pygame.init()
    
    pygame.font.init()
    system_default_font = pygame.font.get_default_font()
    self.font = pygame.font.SysFont(system_default_font, 20)
    
    while self.running:
      self.clock.tick(self.max_fps)
      self._handle_events()
      self._plot()
      if not self.paused:
        self._update_game()

    pygame.quit()
  
  def _handle_events(self):
    if pygame.event.get(eventtype=pygame.QUIT):
      self._exit()

    pressed_keys = pygame.key.get_pressed()
    for key in self.keypress_events_by_key.keys():
      if pressed_keys[key]:
        self.keypress_events_by_key[key]()

    for key_event in pygame.event.get(eventtype=pygame.KEYDOWN):
      if key_event.key in self.toggle_events_by_key:
        self.toggle_events_by_key[key_event.key]()

    mouse_events = pygame.event.get(eventtype=pygame.MOUSEBUTTONDOWN)
    for mouse_event in mouse_events:
      if mouse_event.button == 4: # Mousewheel up
        self._increase_zoom()
      if mouse_event.button == 5: # Mousewheel down
        self._decrease_zoom()

  def _increase_zoom(self):
    self.cell_size += 1
    self.viewport.step = self.cell_size

  def _decrease_zoom(self):
    self.cell_size -= 1
    if self.cell_size < 1:
      self.cell_size = 1
    
    self.viewport.step = self.cell_size
  
  def _increase_cell_life_probability(self):
    self.game.cell_life_probability += 0.01
  
  def _decrease_cell_life_probability(self):
    self.game.cell_life_probability -= 0.01
    if self.game.cell_life_probability < 0.01:
      self.game.cell_life_probability = 0.01
  
  def _reset(self):
    self.game.board = self.game.board.Random(size=self.game.board.size, cell_life_probability=self.game.cell_life_probability)
    self.game.generation_count = 0

  def _toggle_pause(self):
    self.paused = not self.paused

  def _exit(self):
    self.running = False

  def _update_game(self):
    self.game.update_board()

  def _plot_hud(self):
    text = f"Gen: {self.game.generation_count} FPS: {self.clock.get_fps():.2f} {'paused' if self.paused else ''} Zoom: {self.cell_size} Cell Prob: {self.game.cell_life_probability}"
    textsurface = self.font.render(text, False, (255, 0, 255))
    self.screen.blit(textsurface, (0, 0))

  def _plot(self):
    self._plot_board()
    self._plot_hud()

    pygame.display.flip()

  def _plot_board(self):
    self.screen.fill((255,255,255))
    board = self.game.board

    viewport_width, viewport_height = self.viewport.get_bounds(self.ideal_cell_size / self.cell_size)
    
    stop_y = min(self.game.board.height, viewport_height)
    stop_x = min(self.game.board.width,  viewport_width)

    for line in range(self.viewport.pos_y, stop_y):
      for column in range(self.viewport.pos_x, stop_x):
        if board.state[line][column]:
          screen_x = (column  - self.viewport.pos_x) * self.cell_size
          screen_y = (line  - self.viewport.pos_y) * self.cell_size
          cell_rect = pygame.Rect(screen_x, screen_y, self.cell_size, self.cell_size)
          pygame.draw.rect(self.screen, 0, cell_rect)
