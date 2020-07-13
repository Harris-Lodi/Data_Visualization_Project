import json
from plotly.graph_objs import Scattergeo, Layout 
from plotly import offline 
from plotly import colors 

# explore geojson data from file
# source: https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php
filename = 'data/1.0_month.geojson'
with open(filename, encoding='utf8') as f:
    all_eq_data = json.load(f)

# rewrite data from filename to a new file readable_file, 
# this new json format will be more usable with python
# following block of code needs update to run only if readable_file is 
# not found in the data folder
readable_file = 'data/readable_eq_data.json'
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4)

# create list that contains the 'features'
# from every earthquake recorded in json 
all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts)) # print the number of earthquakes in file

# extract magnitude, longitude, lateral, and hover_text_data for each earthquake
mags, lons, lats, hover_text = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    title = eq_dict['properties']['title']
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_text.append(title)

# print first 10 mags, lons, and lats on record
# print(mags[:10])
# print(lons[:10])
# print(lats[:10])

# print available color schemes to use for 'colorscale' setting below
# print('color scale keys are: ')
# for key in colors.PLOTLY_SCALES.keys():
#     print(key)

# map the earthquakes
# insert data from file to var data, also customize marker size and color
# 'size' of marker is determined my magnitude of earthquake times 5 for each event in mags list
# mags list is also used to determine the 'color' setting
# 'colorscale' is viridis, 'reversescale' is true meaning lower value are yellow, high ones blue
# 'colorbar' shows us what the colors represent on plot
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_text,
    'marker': { # nested dict 'marker' contains settings for marker properties
        'size': [5 * mag for mag in mags],
        'color': mags,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'},
    },
}] 
my_layout = Layout(title = 'Global Earthquakes from June 11th, 2020 to July 11th, 2020') # name our plot and init plot layout

fig = {'data': data, 'layout': my_layout} # set plot axis 
offline.plot(fig, filename = 'global_earthquakes.html') # offline create an html file with plotted data

