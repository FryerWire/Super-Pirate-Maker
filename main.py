
"""
Stopped at 1:43 which is the start of the "Creating Tiles" chapter
"""

import pygame
from settings import *
from pygame.image import load
from editor import Editor

class Main():
    def __init__(self):
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.clock = pygame.time.Clock()

        self.editor = Editor()

        # Cursor
        surf = load("Super-Pirate-Maker\graphics\cursors\mouse.png")
        cursor = pygame.cursors.Cursor((0, 0), surf)
        pygame.mouse.set_cursor(cursor)

    def run(self):
        while True:
            dt = self.clock.tick() / 1000

            self.editor.run(dt)
            pygame.display.update()

if __name__ == "__main__":
    main = Main()
    main.run()