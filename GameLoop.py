import pygame
import PlayerInput


class GameLoop:

    def __init__(self, worlds):
        self.worlds = worlds
        self.running = True
        self.active_world = worlds[0]
        self.clock = pygame.time.Clock()

    def set_world(self, world):
        self.active_world = world

    def execute_event_loop(self):
        while self.running:
            time_passed = self.clock.tick(50)
            PlayerInput.reset_key_list()
            for event in pygame.event.get():
                PlayerInput.key_input_listener(event)
                if event.type == pygame.QUIT:
                    running = False
            self.active_world.manage_actions()
            self.active_world.actor_bounds()
            self.active_world.draw_screen()
            pygame.display.update()

