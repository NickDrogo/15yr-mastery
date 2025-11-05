import plotly.express as plt
from random_walk import Randomwalk 

# Keep making new walks, as long as the program is active.


while True:
    rw = Randomwalk(5_000)
    rw.fill_walk()

    point_numbers = range(rw.num_points)
    fig = plt.scatter(rw.x_values, rw.y_values)
    fig.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
