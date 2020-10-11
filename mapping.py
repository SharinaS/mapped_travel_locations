'''
Created on July, 2018; Updated and refactored October 2020

@author: sharina stubbs

Project Description: 
A web-based mapping project of locations, with interactive pop-ups and color-coding. Project uses folium, pandas, python; csv is used to store the data.
Note - dataframes converted into python lists to improve speed of program.

Version: 1.0

'''

#TODO: clean-up naming of variables


import folium
import pandas

data = pandas.read_csv("places_visited.csv")
latitude = list(data["LATITUDE"])
longitude = list(data["LONGITUDE"])
location_name = list(data["LOCATION_NAME"])
visit_type = list(data["VISIT_TYPE"])
# set initial zoom level at a particular focus point on the map
base_map = folium.Map(location=[48.864716, 2.349014], zoom_start=2)
feature_group = folium.FeatureGroup(name="Travel Map")


def show_visit_category(visit_type):
    if visit_type == 1:
        return 'orange'  # lived there
    return 'blue'  # visited


for lat, long, location, visit in zip(
    latitude,
    longitude,
    location_name,
    visit_type
):
    feature_group.add_child(folium.Marker(
            location=[lat, long],
            popup=str(location),
            icon=folium.Icon(color=show_visit_category(visit)))
            )


base_map.add_child(feature_group)

base_map.save("map_of_explorations.html")




#===============================================================================
# print(data)
# print(data.columns)
# print(latitude)
# print(lon)
#print(location_name)
# print(help(folium.Marker))
#===============================================================================





    











