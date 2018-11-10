import csv
import bokeh
import numpy as np
import matplotlib.pyplot as plt


# Open the earthquake data file.
#filename = 'earthquake.csv'
#with open("c:\Python27/earthquake.csv", "r") as csvfile:
 #   myfile = csv.reader(csvfile)


# Create empty lists for the latitudes and longitudes.
location = []

# Read through the entire file, skip the first line,
#  and pull out just the lats and lons.
with open("c:\Python27/earthquake.csv", "r") as csvfile:
    # Create a csv reader object.
    reader = csv.reader(csvfile)

    # Ignore the header row.
    next(reader)

    # Store the latitudes and longitudes in the appropriate lists.
    for row in reader:
        location.append(str(row))
       # lons.append(float(row[2]))

# --- Build Map ---


# llcrnrlat,llcrnrlon,urcrnrlat,urcrnrlon
# are the lat/lon values of the lower left and upper right corners
# of the map.
# resolution = 'c' means use crude resolution coastlines.


from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
# setup Lambert Conformal basemap.
# set resolution=None to skip processing of boundary datasets.
m = Basemap(width=12000000,height=9000000,projection='lcc',
            resolution=None,lat_1=45.,lat_2=55,lat_0=50,lon_0=-107.)
m.bluemarble()
plt.show()
