from pathlib import Path
import plotly.express as plx
import json



# Read the data as a string and convert to a python object.
path = Path('Notes/eq_data/2.5_day.geojson')
contents = path.read_text(encoding="utf-8")
all_eq_data = json.loads(contents)



# Examine all earthquakes in the dataset.
all_eq_dicts = all_eq_data['features']

name = all_eq_data["metadata"]['title']

mags, lons, lats, eq_titles = [], [], [], []
for eq_dict in all_eq_dicts:
    mags.append(eq_dict['properties']['mag'])
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])
    eq_titles.append(eq_dict['properties']['title'])
    

title = name
fig = plx.scatter_geo(
    lat=lats, lon=lons, size=mags, title=title,
    color=mags, 
    color_continuous_scale='Viridis',
    labels={'color':'Magnitude'},
    projection='natural earth',
    hover_name=eq_titles,
    )

fig.show()
