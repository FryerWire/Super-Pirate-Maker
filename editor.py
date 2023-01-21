
import pygame, sys
from pygame.math import Vector2 as vector
from pygame.mouse import get_pressed as mouse_buttons
from pygame.mouse import get_pos as mouse_pos
from settings import *

class Editor():
    def __init__(self):
        # Main setup
        self.display_surface = pygame.display.get_surface()

        # Navigation
        self.origin = vector()
        self.pan_active = False
        self.pan_offset = vector()

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            self.pan_input(event)

    def pan_input(self, event):
        # Middle mouse button pressed / released
        if event.type == pygame.MOUSEBUTTONDOWN and mouse_buttons()[1]:
            self.pan_active = True
            self.pan_offset = vector(mouse_pos()) - self.origin
            
        if not mouse_buttons()[1]:
            self.pan_active = False

        # Mouse wheel
        if event.type == pygame.MOUSEWHEEL:
            if pygame.key.get_focused()[pygame.K_LCTRL]:
                self.origin.y -= event.y * 50
            else:
                self.origin.x -= event.y * 50

            
        # Panning update
        if self.pan_active:
            self.origin = vector(mouse_pos()) - self.pan_offset

    # Drawing
    def draw_tile_lines(self):
        cols = WINDOW_WIDTH // TILE_SIZE
        rows = WINDOW_HEIGHT // TILE_SIZE

        for col in range(cols):
            pygame.draw.line(self.display_surface, LINE_COLOR, (x, y), (x, y))

    def run(self, dt):
        self.display_surface.fill("white")
        self.event_loop()
        pygame.draw.circle(self.display_surface, "red", self.origin, 10)
