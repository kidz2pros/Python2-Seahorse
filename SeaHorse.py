import pygame
import PlayerInput
from Actor import Actor
from Label import Label

class SeaHorse(Actor):

    def __init__(self):
        super().__init__()
        self.set_image(pygame.image.load('Seahorse.png'))
        self.speed = 3
        self.rising = False
        self.starting_y = 0
        self.rise_height = 60
        self.rise_speed = 3
        self.fall_speed = 1

    def act(self):
        self.key_commands()
        self.rise_check()
        self.too_low()

    def key_commands(self):
        if PlayerInput.is_key_down(pygame.K_LEFT):
            self.set_location(self.x - self.speed, self.y)
        if PlayerInput.is_key_down(pygame.K_RIGHT):
            self.set_location(self.x + self.speed, self.y)
        if PlayerInput.is_key_pressed(pygame.K_SPACE):
            self.start_rising()

    def start_rising(self):
        self.rising = True
        self.starting_y = self.y

    def rise_check(self):
        self.rise()
        if (self.y < self.starting_y - self.rise_height) or (self.y <= 0):
            self.rising = False

    def rise(self):
        if self.rising:
            self.set_location(self.x, self.y - self.rise_speed)
        else:
            self.set_location(self.x, self.y + self.fall_speed)

    def too_low(self):
        if self.y > self.world.height - 50:
            self.world.add_actor(Label("You Lose!", 100), 250, 220)
            self.world.remove_actor(self)
