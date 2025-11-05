import matplotlib.pyplot as plt


input_values = range(1, 6)
cubes = [x ** 3 for x in input_values]


plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()

ax.plot(input_values, cubes, color='red', linewidth=3)

ax.set_title("Cube Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=24)
ax.set_ylabel("Cube Of Values", fontsize=14)

ax.tick_params(labelsize=14)

plt.show()

