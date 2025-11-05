from random import randint
import plotly.express as px

class Die:
    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        return randint(1, self.num_sides)
    
die_1 = Die()
die_2 = Die()
die_3 = Die()


# Make some rolls, and store results in a list.
results = []
for roll_num in range(1_000):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)


# Analyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
poss_results = range(3, max_result+1)

for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.
title = 'Results of Rolling Three D6 1000 Times'
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)

# Further customize chart.
fig.update_layout(xaxis_dtick=1)

fig.show()


