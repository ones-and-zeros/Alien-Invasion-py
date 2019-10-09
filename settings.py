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
        self.ship_limit = 3

        # bullet settings
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        self.bullet_sustain = False

        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # dir 1 = right, -1 =  left
        self.fleet_direction = 1


        self.debug_mode = True
        if self.debug_mode:
            self.full_screen = False
            self.screen_width = 600
            self.screen_height = 400

            self.bullet_width = 500
            self.bullet_sustain = True
