from geopy.geocoders import Nominatim
from geopy.distance import vincenty
import sys

geolocator = Nominatim()

centers = [
    "Ashburn, VA", 
    "Atlanta, GA", 
    "Chicago, IL",
    "Dallas/Fort Worth, TX",
    "Jacksonville, FL",
    "Los Angeles, CA",
    "Miami, FL", 
    "New York, NY",
    "Palo Alto, CA",
    "Seattle, WA",
#    "South Bend, IN",
    "St. Louis, MO",
    "Boardman, OR",
]

coords = []
for i in centers:
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
