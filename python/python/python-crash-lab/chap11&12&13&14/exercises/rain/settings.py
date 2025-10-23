class Settings:
    """A class to tore all settings for Alien Invasions"""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        # (0,0) for full screen
        self.screen_width = 500
        self.screen_height = 300
        self.bg_color = (230, 230, 230)
    

        # rain Settings
        self.rain_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1