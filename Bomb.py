from Actor import Actor
import pygame
from SeaHorse import SeaHorse
from Label import Label

class Bomb(Actor):

    def __init__(self):
       super().__init__()
       self.set_image(pygame.image.load('Bomb.png'))
       self.speed = 2

    def act(self):
        self.fall()
        self.touch_sea_horse()
        self.disappear()

    def fall(self):
        self.set_location(self.x, self.y + self.speed)

    def disappear(self):
        if self.y >= self.world.height:
            self.world.remove_actor(self)

    def touch_sea_horse(self):
        touches = self.get_one_intersector(SeaHorse)
        if touches is not None:
            self.world.remove_actor(touches)
            self.world.add_actor(Label("You Lose!", 100), 250, 220)
