from random import choice

class Randomwalk:
    """A class to generate random walks."""

    def __init__(self, num_points=5000):
        """Initialize attributes of a walk."""
        self.num_points = num_points

        # All walks start at (0, 0).
        self.x_values = [0]
        self.y_values = [0]


    def fill_walk(self):
        """Calculate all the points in the walk."""

        # Keep taking steps until the walk reaches the desired length.
        while len(self.x_values) < self.num_points:

            self.get_step_x()
            self.get_step_y()
            
            # Reject moves that go nowhere.
            if self.x == 0 and self.y == 0:
                continue

            # Calculate the new position.
            x = self.x_values[-1] + self.x
            y = self.y_values[-1] + self.y

            self.x_values.append(x)
            self.y_values.append(y)

    def get_step_x(self):
        # Decide whick direction to go, and how far to go.
        x_direction = choice([1, -1])
        x_distance = choice([0, 1, 2, 3, 4])
        self.x = x_direction * x_distance

    def get_step_y(self):
            # Decide whick direction to go, and how far to go.
            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            self.y = y_direction * y_distance


