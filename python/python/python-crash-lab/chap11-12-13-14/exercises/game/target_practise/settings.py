class Settings:
    """A class to tore all settings for Alien Invasions"""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        # (0,0) for full screen
        self.screen_width = 600
        self.screen_height = 300
        self.bg_color = (230, 230, 230)
        #ship settings
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Target Settings
        self.target_drop_speed = 10

        self.speedup_scale = 1.1


    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 2.5
        self.target_speed = 1.0

        self.target_direction = 1

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.target_speed *= self.speedup_scale