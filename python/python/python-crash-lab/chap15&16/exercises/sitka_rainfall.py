import matplotlib.pyplot as plx
import csv
from pathlib import Path
from datetime import datetime



path = Path('Notes/weather_data/sitka_weather_2021_full.csv')
lines = path.read_text().splitlines()
 

reader = csv.reader(lines)
header_row = next(reader)

# Extract dates and prcp.
dates, prcp = [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        no_of_rainfall = float(row[3])
    except ValueError:
        print(f"Missing data for {current_date}\n")
    else:
        dates.append(current_date)
        prcp.append(no_of_rainfall)
        
    


plx.style.use('seaborn-v0_8')
fig, ax = plx.subplots()
ax.plot(dates, prcp, color='red')


# Format plot
title =  "Sitka Rainfall"
ax.set_title(title, fontsize=24)
ax.set_xlabel(" ", fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("No of rainfall", fontsize=16)
ax.tick_params(labelsize=16)

plx.show()
