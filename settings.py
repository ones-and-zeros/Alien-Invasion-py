class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialize te game's settings."""
        # Screen settings
        self.full_screen = True
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)  # light grey
        
        # ship settings
        self.ship_speed = 1.5

