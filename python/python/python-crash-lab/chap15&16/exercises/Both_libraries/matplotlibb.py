from random import randint
import matplotlib.pyplot as plx

class Die:
    def __init__(self, num_sides=8):
        self.num_sides = num_sides

    def roll(self):
        return randint(1, self.num_sides)
    


    
die_1 = Die()
die_2 = Die()



# Make some rolls, and store results in a list.
results = []
for roll_num in range(1_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_result+1)

for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)


plx.style.use('seaborn-v0_8')
fig, ax = plx.subplots()
ax.bar(poss_results, frequencies, width=1, edgecolor="white", linewidth=0.7)


# Set chart title and label axes.
ax.set_title("Results of Rolling Two D8 1000 Times", fontsize=24)
ax.set_xlabel("Result", fontsize=14)
ax.set_ylabel("Frequency of Result", fontsize=14)



# Further customize chart.
# plx.update_layout(xaxis_dtick=1)
plx.xticks(range(2, 17))

plx.show()


