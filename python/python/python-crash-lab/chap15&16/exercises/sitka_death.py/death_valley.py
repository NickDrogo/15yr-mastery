import matplotlib.pyplot as plx
import csv
from pathlib import Path
from datetime import datetime

path = Path('Notes/weather_data/death_valley_2021_simple.csv')
lines = path.read_text().splitlines()
 

reader = csv.reader(lines)
header_row = next(reader)


# for index, column_header in enumerate(header_row):
#     print(index, column_header)

# Extract dates and high temperatures
dates, highs, lows = [], [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        high = int(row[3])
        low = int(row[4])
    except ValueError:
        print(f"Missing data for {current_date}\n")
    else:
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

# Plot the high and low temperatures.

plx.style.use('seaborn-v0_8')
fig, ax = plx.subplots()
ax.plot(dates, highs, color='red', alpha=0.5)
ax.plot(dates, lows, color='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)




# Format plot
title =  "Daily High and Low Temperatures, 2021\nDeath Valley, CA"
ax.set_title(title, fontsize=24)
ax.set_xlabel(" ", fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperatures (f)", fontsize=16)
ax.tick_params(labelsize=16)

ax.set_ylim(0, 130)
plx.show()
