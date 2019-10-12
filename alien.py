import pygame, random
from pygame.sprite import Sprite


class Alien(Sprite):
    """class for a single alien in a fleet"""

    def __init__(self, ai_game):
        """Initialize the alien and set it's (starting position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the alien image and set its rect attribute.
        self.image = None
        self.update_image()
        self.rect = self.image.get_rect()

        # Start each nre alien near the top left of screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position
        self.x = float(self.rect.x)

    def check_edges(self):
        """return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= screen_rect.left:
            return True

    def update_image(self):
        """Update the alien's image."""
        self.image = pygame.image.load(self.settings.image_dir + 'alien_' + str(random.randint(1, 6)) + '.bmp')

    def update(self):
        """Move Aliens"""
        self.x += (self.settings.alien_speed *
                   self.settings.fleet_direction)
        self.rect.x = self.x
