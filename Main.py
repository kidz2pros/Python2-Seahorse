import pygame
from GameLoop import GameLoop
from Sea import Sea

pygame.init()

width = 800
height = 600


game = GameLoop( [Sea()])

game.execute_event_loop()






