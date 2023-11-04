# game.py
import pygame
from player import Player
from food import Food
from world import World
import random

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.running = True
        self.world = World(self.screen.get_width(), self.screen.get_height())
        self.start_game()
        self.last_spawn_time = 0
        self.spawn_interval = 3000  # Time in milliseconds
        self.spawn_food()
        self.score = 0

    def start_game(self):
        self.player = Player(self.screen.get_width() // 2, self.screen.get_height() - 30, self.world)
        self.food = {}
        self.score = 0

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
        self.update_food()

        if self.player.health <= 0:
            self.start_game()

    def update_food(self):
        if pygame.time.get_ticks() - self.last_spawn_time > self.spawn_interval:
            self.spawn_food()
        food_to_delete = []
        for uuid, item in self.food.items():
            item.update()
            if item.collide_with_object(self.player):
                self.score += 1
                self.player.energy += 10
                if self.player.energy > 100:
                    self.player.energy = 100
                food_to_delete.append(uuid)

        for uuid in food_to_delete:
            del self.food[uuid]

    def spawn_food(self):
        new_food = Food(random.randint(0, self.screen.get_width()), 0, self.world)  # Assuming Food takes x, y coordinates
        self.food[new_food.uuid] = new_food  # Assuming Food has a uuid attribute
        self.last_spawn_time = pygame.time.get_ticks()

    def draw(self):
        self.screen.fill((54, 106, 130))  # Fill the screen with a blue color (like water)
        self.world.draw(self.screen)
        self.player.draw(self.screen)
        for uuid, food in self.food.items():
            food.draw(self.screen)
        self.draw_bars()  # Draw the energy and health bars

        pygame.display.flip()  # Update the full display surface to the screen

    # Assuming this is within the Game class

    def draw_bars(self):
        # Define colors
        green_variant = (137, 208, 238)  # A darker shade of green for energy
        red_variant = (128, 0, 0)  # A darker shade of red for health
        box_border_color = (221, 243, 254)  # Light blue from your player color

        # Define bar properties
        bar_width = 200
        bar_height = 20
        spacing = 10
        border_thickness = 3

        # Calculate the energy and health as a percentage
        energy_percentage = self.player.energy / 100.0
        health_percentage = self.player.health / 100.0

        # Define positions
        box_x, box_y = 10, 10  # Upper left corner

        # Draw the grouping box
        total_box_height = (2 * bar_height) + (3 * spacing)
        pygame.draw.rect(self.screen, box_border_color, (box_x, box_y, bar_width + (spacing * 2), total_box_height),
                         border_thickness)

        # Draw the energy bar
        energy_bar_rect = (box_x + spacing, box_y + spacing, bar_width * energy_percentage, bar_height)
        pygame.draw.rect(self.screen, green_variant, energy_bar_rect)

        # Draw the health bar below the energy bar
        health_bar_rect = (
        box_x + spacing, box_y + (2 * spacing) + bar_height, bar_width * health_percentage, bar_height)
        pygame.draw.rect(self.screen, red_variant, health_bar_rect)

        # Define score text properties
        score_color = (221, 243, 254)  # Light blue, matching the box border
        font_size = 24  # Size of the font
        font = pygame.font.Font(None, font_size)  # Default font

        # Render the score text
        score_text = f"Score: {self.score}"  # Assuming the score is stored in self.score
        score_surface = font.render(score_text, True, score_color)
        score_rect = score_surface.get_rect()

        # Position the score text at the top right corner, with some margin
        score_rect.topright = (self.screen.get_width() - 10, 10)

        # Draw the score text onto the screen
        self.screen.blit(score_surface, score_rect)


if __name__ == '__main__':
    game = Game()
    game.run()
