class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize te game's settings."""

        # Screen settings
        self.full_screen = False
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)  # light grey

        # ship settings
        self.ship_limit = 3

        # bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        self.bullet_sustain = False

        # Alien settings
        self.fleet_drop_speed = 10

        # How quickly the game speeds up
        self.speedup_scale = 1.1
        # How quickly the alien point values increase
        self.score_scale = 1.5

        # These attributes will be set later
        self.ship_speed = None
        self.bullet_speed = None
        self.alien_speed = None
        self.alien_points = None
        self.fleet_direction = None

        self.initialize_dynamic_settings()

        # Locate image directory
        self.use_alt_images = False
        self.image_dir = None  # will be populated later
        self.set_alt_images(self.use_alt_images)

        self.debug_mode = False
        if self.debug_mode:
            self.full_screen = False
            self.screen_width = 600
            self.screen_height = 400

            self.bullet_width = 500
            self.bullet_sustain = True

            self.ship_limit = 1

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game"""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        # Scoring
        self.alien_points = 50

        # dir 1 = right, -1 =  left
        self.fleet_direction = 1

    def increase_speed(self):
        """Increase speed setting and point values."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)

    def get_alt_images(self):
        """Get state of alternate images"""
        return self.use_alt_images

    def set_alt_images(self, alt_image):
        """Modify the alternate images"""
        self.use_alt_images = alt_image
        if self.use_alt_images:
            self.image_dir = 'images_alt/'
        else:
            self.image_dir = 'images/'
