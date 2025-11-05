import plotly.express as px
import csv
from pathlib import Path
from datetime import datetime

path = Path('Notes/eq_data/world_fires_1_day.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)


# for index, column in enumerate(header_row):
#     print(index, column)


# Extract data
dates, lons, lats, volts = [], [], [], []
for row in reader:
    current_dates = datetime.strptime(row[5], '%Y-%m-%d')
    try:
        lat = float(row[0])
        lon = float(row[1])
        volt = float(row[2])
    except ValueError:
        print(f"Data for {current_dates} is missing")
    else:
        dates.append(current_dates)
        lats.append(lat)
        lons.append(lon)
        volts.append(volt)


title = 'World Fire'
fig = px.scatter_geo(lat=lats, lon=lons, size=volts, title=title,
                     color=volts, 
                     data_frame=dates,
                     color_continuous_scale='viridis',
                     labels={'color':'Magnitude'},
                     projection='natural earth',
                     )



fig.show()
 
