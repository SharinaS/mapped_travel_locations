# Interactive Map of the World

A web-based mapping project built with:

* Python
* Folium - a Python library used for visualizing geospatial data
* Pandas - a Python data manipulation library
* A .csv file for data storage

The output of the program is a global map with markers placed in locations determined by geographic coordinates stored in a .csv file. When the user clicks on color-coded markers, additional information appears, such as city name, as a pop-up (determined, again, by data in the .csv).

![screenshot of map](images/demo-map.png)

By changing the data in the .csv file, you can change both the location of the markers and the pop-up information provided by the markers.

For example, a properly formatted .csv file for this project should have the following format:

```txt
LOCATION_NAME,VISIT_TYPE,LATITUDE,LONGITUDE
Quinault WA,2,47.46028,-123.802838
Saba,20,17.633333333333,-63.239444444444
Sint Eustatius,2,17.4826800,-62.9832400
```

|Column Name|Description|Example|
|----|----|----|
|LOCATION_NAME|The location where the marker will be placed|Quinault, WA|
|VISIT_TYPE|A number of either 1 or 2; 1 indicates a residence, while 2 represents a visit|2|
|LATITUDE|The latitude of the destination|47.46028|
|LONGITUDE|The longitude of the destination|-123.802838|

An online search for locations coordinates will quickly provide you with latitude and longitude values.

## How To Use this Repo to Run the Program and Build the Map

1. Clone the GitHub repo into your local machine.
2. Create a virtual environment, such as with the command `pipenv shell`
3. Open your code editor, such as VS Code
4. Install folium and pandas into your virtual environment, ie, `pipenv install folium`.
5. Make sure you are in the root of your project, then run the program by typing the command `python mapping.py` into your command line.
6. A .html file will be built, and placed at the root level of the project directory
7. Drag the .html file into the URL bar at the top of the browser window.
8. A global map with interactive markers will appear after the page loads.

## Contributor

Sharina Stubbs

## Resources

* [Folium docs](https://python-visualization.github.io/folium/)
* [Pandas docs](https://pandas.pydata.org/)
