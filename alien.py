import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """class for a single alien in a fleet"""

    def __init__(self, ai_game):
        """Initialize the alien and set it's (starting position"""
        super().__init__()
        self.screen = ai_game.screen

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each nre alien near the top left of screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position
        self.x = float(self.rect.x)
