import pygame
import pygame.freetype
from Actor import Actor


class Label(Actor):

    def __init__(self, text, size):
        super().__init__()
        self.text = text
        self.size = size
        self.color = (0,0,0)
        self.font = pygame.freetype.SysFont("Arial", self.size)
        self.rendered, rect = self.font.render(self.text, self.color)
        self.image = self.rendered
        self.display = self.rendered

    def set_text(self, text):
        self.text = text
        self.render()

    def set_size(self, size):
        self.size = size
        self.render()

    def set_color(self, color):
        self.color = color
        self.render()

    def render(self):
        self.font = pygame.freetype.SysFont("Arial", self.size)
        self.rendered, rect = self.font.render(self.text, self.color)
        self.image = self.rendered
        self.display = self.rendered
