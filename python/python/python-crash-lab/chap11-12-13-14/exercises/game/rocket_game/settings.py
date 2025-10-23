class Settings:
    """A class to tore all settings for Alien Invasions"""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        # (0,0) for full screen
        self.screen_width = 0
        self.screen_height = 0
        self.bg_color = (230, 230, 230)
        #ship speed
        self.ship_speed = 1.5