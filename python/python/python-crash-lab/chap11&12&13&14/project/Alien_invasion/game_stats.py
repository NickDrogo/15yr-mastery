from pathlib import Path
class GameStat:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize statistics"""
        self.settings = ai_game.settings
        
        # High score should never be reset.
    
    

        self.level = 1

        
        self.reset_stats()


    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ship_left = self.settings.ship_limit
        self.score = 0
        self.high_score_file = Path("Alien_invasion/high_score.txt")
        self.high_score = int(self.high_score_file.read_text())
    

    
        

    
            
    

        
  