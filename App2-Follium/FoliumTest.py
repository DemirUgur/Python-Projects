import folium
from pandas import read_csv


def color_picker(height):
    if height < 1500:
        return 'green'
    elif height < 2000:
        return 'orange'
    else:
        return 'red'

def myFunc(x):
    if x['properties']['POP2005'] < 10000000:
        return {'fillColor': 'green'}
    elif x['properties']['POP2005'] < 50000000:
        return {'fillColor': 'yellow'}
    else:
        return {'fillColor': 'red'}

data = pandas.read_csv("Volcanoes.txt")
map = folium.Map()
lon = list(data["LON"])
lat = list(data["LAT"])
elev = list(data["ELEV"])
fgv = folium.FeatureGroup(name = "Volcanoes")
for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location =[lt, ln], popup=str(el), radius = 6, fill_color = color_picker(el), color = 'grey', fill_opacity=0.7 ))

fgp = folium.FeatureGroup(name = "Population")
fgp.add_child(folium.GeoJson(data = open('world.json', 'r', encoding='utf-8-sig').read(),
                                style_function = lambda x : myFunc(x) ))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl()) #It is necceseray for us to add LayerControl after we add all the other childs.
map.save("Map1.html")