import random

class  Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(random.randint(1, self.sides))


player = Die()

player.roll_die()
player.roll_die()
player.roll_die()
player.roll_die()
player.roll_die()
player.roll_die()
player.roll_die()
player.roll_die()
player.roll_die()
player.roll_die()

print()

player1 = Die(10)
player1.roll_die()
player1.roll_die()
player1.roll_die()
player1.roll_die()
player1.roll_die()
player1.roll_die()
player1.roll_die()
player1.roll_die()
player1.roll_die()
player1.roll_die()

print()


player2 = Die(20)
player2.roll_die()
player2.roll_die()
player2.roll_die()
player2.roll_die()
player2.roll_die()
player2.roll_die()
player2.roll_die()
player2.roll_die()
player2.roll_die()
player2.roll_die()