'''
Created on July, 2018; Updated and refactored October 2020

@author: sharina stubbs

Project Description: 
A web-based mapping project of locations, with interactive pop-ups and color-coding. Project uses folium, pandas, python; csv is used to store the data.
Note - dataframes converted into python lists to improve speed of program.

Version: 1.0

'''


import folium
import pandas


data = pandas.read_csv("places_visited.csv")
lat = list(data["LATITUDE"])
lon = list(data["LONGITUDE"])
des = list(data["DESTINATION"])
vis = list(data["VISITS"])


def visit_times(visits):
    if visits < 2:
        return 'green'
    elif 2 <= visits < 6:
        return 'blue'
    elif 6 <= visits < 11:
        return 'yellow'
    elif 11 <= visits < 16:
        return 'orange'
    else:
        return 'red' #for 16 and upward
    

base_map = folium.Map(location=[48.864716,2.349014], zoom_start=2)

fg = folium.FeatureGroup(name="Travel Map")
fg.add_child(folium.Marker(location=[47.608013, -122.335167], popup="Home Base", icon=folium.Icon(color='pink')))

for lt, ln, ds, vs in zip(lat,lon,des,vis):
    if vs <2:
        fg.add_child(folium.Marker(location=[lt,ln], popup="Visited " + str(vs) + " time", icon=folium.Icon(color=visit_times(vs))))
    else:
        fg.add_child(folium.Marker(location=[lt,ln], popup="Visited " + str(vs) + " times", icon=folium.Icon(color=visit_times(vs))))
        

base_map.add_child(fg)

base_map.save("map_of_explorations.html")




#===============================================================================
# print(data)
# print(data.columns)
# print(lat)
# print(lon)
# print(des)
# print(help(folium.Marker))
#===============================================================================





    











