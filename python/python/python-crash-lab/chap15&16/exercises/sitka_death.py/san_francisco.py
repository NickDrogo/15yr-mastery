import matplotlib.pyplot as plx
import csv
from datetime import datetime
from pathlib import Path

path = Path('Notes/weather_data/san-francisco-weather_2025_simple.csv')
lines = path.read_text().splitlines()


reader = csv.reader(lines)
header_row = next(reader)

# for index, column in enumerate(header_row):
#     print(index, column)

dates, lows, highs = [], [], []

for row in reader:
    current_date = datetime.strptime(row[5], '%Y-%m-%d')
    try:
        high = int(row[6])
        low = int(row[7])
    except ValueError:
        print(f"\nMissing data for {current_date}")
    else:
        dates.append(current_date)
        highs.append(high)
        lows.append(low)


plx.style.use('seaborn-v0_8')
fig, ax = plx.subplots()
ax.plot(dates, highs, color='red', alpha=0.5)
ax.plot(dates, lows, color='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)




# Format plot
title =  "Daily High and Low Temperatures, 2025\nSan Francisco"
ax.set_title(title, fontsize=24)
ax.set_xlabel(" ", fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperatures (f)", fontsize=16)
ax.tick_params(labelsize=16)

