class GameStats:
    """Track statistics for Alien Invasion"""

    def __init__(self, ai_game):
        """Initialize statistics"""
        self.settings = ai_game.settings
        self.reset_stats()

    def reset_stats(self):
        """Initialize statisctics that can change during game"""
        self.ships_left = self.settings.ship_limit
        # Start game in inactive state 
        self.game_active = False
        self.score = 0
                