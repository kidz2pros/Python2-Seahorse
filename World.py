import pygame


class World:

    def __init__(self, width, height):
        self.actors = []
        self.background = pygame.image.load('defaultBackground.png')
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))

    def add_actor(self, actor: object, x: object, y: object) -> object:
        self.actors.append(actor)
        actor.x = x
        actor.y = y
        actor.world = self
        actor.added_to_world(self)

    def remove_actor(self, actor):
        if actor in self.actors:
            self.actors.remove(actor)
            actor.world = None

    def actor_bounds(self):
        for actor in self.actors:
            if actor.x < 0:
                actor.x = 0
            if actor.x > self.width:
                actor.x = self.width
            if actor.y < 0:
                actor.y = 0
            if actor.y > self.height:
                actor.y = self.height

    def draw_screen(self):
        self.screen.blit(self.background, (0,0))
        for actor in self.actors:
            actor.draw_self(self.screen)

    def manage_actions(self):
        self.act()
        for actor in self.actors:
            actor.act()
        self.actor_bounds()

    def get_actors_of_type(self, type):
        of_type = []
        for actor in self.actors:
            if isinstance(actor, type):
                of_type.append(actor)
        return of_type

    def act(self):

        return


