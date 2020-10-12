'''
Created on July, 2018; Updated and refactored October 2020

@author: sharina stubbs

Project Description:
A web-based mapping project of locations, with interactive pop-ups and
color-coding. Project uses folium, pandas, python; csv is used to store the 
data.

Version: 2.0
'''

import folium
import pandas

# read data from the csv file
file_data = pandas.read_csv("places_visited.csv")
# access columns of data in csv file
latitude = list(file_data["LATITUDE"])
longitude = list(file_data["LONGITUDE"])
location_name = list(file_data["LOCATION_NAME"])
visit_type = list(file_data["VISIT_TYPE"])
# set initial zoom level at a particular focus point on the map
base_map = folium.Map(location=[48.864716, 2.349014], zoom_start=2)
# create a feature group to populate base map with
homes_and_visits = folium.FeatureGroup(name="My Travel Map")


def show_visit_category(visit_type):
    if visit_type == 1:
        return 'orange'  # markers that are orange are home locations
    return 'blue'  # markers that are blue are locations that were visited


def add_markers(latitude, longitude, location_name, visit_type):
    for lat, long, location, visit in zip(
        latitude,
        longitude,
        location_name,
        visit_type
    ):
        # add location data to feature_group
        homes_and_visits.add_child(folium.Marker(
                location=[lat, long],
                popup=str(location),
                icon=folium.Icon(color=show_visit_category(visit)))
                )


def populate_map():
    add_markers(latitude, longitude, location_name, visit_type)
    base_map.add_child(homes_and_visits)
    base_map.save("exploration_map.html")


populate_map()




#===============================================================================
# print(data)
# print(data.columns)
# print(latitude)
# print(lon)
#print(location_name)
# print(help(folium.Marker))
#===============================================================================





    











