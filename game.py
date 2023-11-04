# game.py
import pygame
from player import Player
from food import Food
from world import World

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.running = True
        self.world = World(self.screen.get_width(), self.screen.get_height())
        self.player = Player(self.screen.get_width() // 2, self.screen.get_height() - 30, self.world)
        self.food = pygame.sprite.Group()

    def run(self):
        while self.running:
            self.events()
            self.update()
            self.draw()
            self.clock.tick(60)  # Frame rate

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            self.player.handle_event(event)

    def update(self):
        self.player.update()
        self.food.update()



        # Check for food hitting the ground
        for food in self.food:  # Assuming food is a group or list of Food objects
            if food.rect.bottom >= self.world.ground_level:
                food.rect.bottom = self.world.ground_level
                food.velocity_y = 0



    def draw(self):
        self.screen.fill((0, 0, 128))  # Fill the screen with a blue color (like water)
        self.world.draw(self.screen)
        self.food.draw(self.screen)
        self.player.draw(self.screen)

        pygame.display.flip()  # Update the full display surface to the screen



    def spawn_food(self):
        new_food = Food()
        self.food.add(new_food)

if __name__ == '__main__':
    game = Game()
    game.run()
