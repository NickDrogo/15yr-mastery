class Settings:
    """A class to tore all settings for Alien Invasions"""

    def __init__(self):
        """Initialize the game static settings."""
        """Initialize the game's settings."""
        # Screen settings
        # (0,0) for full screen
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
    
        self.ship_limit = 2

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        self.boss_bullet_allowed = 50

    
        self.fleet_drop_speed = 10
        self.alienboss_drop_speed = 20
        # fleet_direction of 1 represents right; -1 represents left


        #How quickly the game speeds up 
        self.speedup_scale = 1.1

        # How quickly the alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings_default()

    def initialize_dynamic_settings_default(self):
        """Initialize settings that change_throughout the game."""
        self.ship_speed = 1.5
        self.bullet_speed = 2.5
        self.alien_speed = 1.0
        self.alien_boss_speed = 1.8

        # Scoring Settings
        self.alien_points = 50


        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
    
    
    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)



    def initialize_dynamic_settings_medium(self):
        """Initialize speed settings and alien point values."""
        self.ship_speed = 1.9
        self.bullet_speed = 2.5
        self.alien_speed = 2.0

    def initialize_dynamic_settings_hard(self):
        """Initialize settings that change_throughout the game."""
        self.ship_speed = 2.3
        self.bullet_speed = 2.5
        self.alien_speed = 3.0





     