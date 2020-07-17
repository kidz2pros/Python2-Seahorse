import pygame
from World import World
from SeaHorse import SeaHorse
from Label import Label
from Bomb import Bomb
import random

class Sea(World):

    def __init__(self):
        super().__init__(960, 540)
        self.background = pygame.image.load('3_game_background.png')
        self.add_actor(SeaHorse(), 100, 400)
        self.add_actor(Bomb(), 200, 0)
        self.time_count = 0
        self.max_time_count = 100

    def act(self):
        self.bomb_timer()

    def add_bomb(self):
        x = random.randrange(0, self.width, 1)
        self.add_actor(Bomb(), x , 0)

    def bomb_timer(self):
        if self.time_count <= 0:
            self.time_count = random.randrange(0, 50, 1) + 10
            self.add_bomb()
        else:
            self.time_count -= 1

