from geopy.geocoders import Nominatim
from geopy.distance import vincenty
import sys

geolocator = Nominatim()

centers = [
    "Austin, TX",
    "Boise, ID",
    "Denver, CO",
    "Las Vegas, NV",
    "Miami, FL", 
    "Minneapolis, MN",
    "Nashville, TN",
    "New York, NY",
    "Palo Alto, CA",
    "Seattle, WA"
]

coords = []
for i in centers:
    print i
    location = geolocator.geocode(i)
    coords.append((location.latitude, location.longitude))


adj = []
for i in coords:
    tmp = []
    for j in coords:
        if (i==j):
            tmp.append(0)
        else:
            tmp.append(round(vincenty(i,j).miles,2))
    adj.append(tmp)

print(adj)

for i in coords:
    print(str(i[0])+" "+str(i[1]))

for arr in adj:
    for a in arr:
       sys.stdout.write(str(a)+" ")        
    print("")
