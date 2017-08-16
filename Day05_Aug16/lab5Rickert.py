# pip install googlemaps
from googlemaps import Client
from datetime import datetime


api_key = 'Your key here'
gmaps = Client(api_key)
dir(gmaps)
whitehouse = '1600 Pennsylvania Avenue, Washington, DC'
whitehouse_geoloc = gmaps.geocode(whitehouse)
print whitehouse_geoloc

destination = gmaps.reverse_geocode((38.897096, -77.036545))
print destination

now = datetime.now()
directions_result = gmaps.directions("Sydney Town Hall",
                                     "Parramatta, NSW",
                                     mode="transit",
                                     departure_time=now)

lat_long = (gmaps.geocode('326 Perkins Library, Durham, NC 27708')[0]['geometry']['location']['lat'], gmaps.geocode('326 Perkins Library, Durham, NC 27708')[0]['geometry']['location']['lng'])
print lat_long
duke = gmaps.reverse_geocode(lat_long)[0]['formatted_address']
print duke

local = gmaps.places('restaurant near ' + duke)
print local['results'][0]['formatted_address']
print local['results'][0]['name']

directions = gmaps.directions(duke, whitehouse)
print directions[0]['legs'][0]['distance']

for step in directions[0]['legs'][0]['steps']:
	print step['html_instructions']

embassies = [[38.917228,-77.0522365],
	[38.9076502, -77.0370427],
	[38.916944, -77.048739] ]

embassies0 = (embassies[0][0], embassies[0][1])


# TODO: write code to answer the following questions:
# which embassy is closest to the White House in meters? how far?
def meterconverter(miles):
    meters = miles * 1609.34
    return meters
distancelist = []
for i in range(0,3):
    directions = gmaps.directions(embassies[i], whitehouse)
    Distance = directions[0]['legs'][0]['distance']
    DistanceInMeters = round(meterconverter(float(Distance[u'text'][:-3])),2)
    distancelist.append(DistanceInMeters)
m = min(distancelist)
[i for i, j in enumerate(distancelist) if j == m]
ClosestEmbassyDist = distancelist[1]
print "The closest embassy is the Australian Embassy, which is %s meters away." %ClosestEmbassyDist
# what is its address?
ClosestEmbassy = gmaps.reverse_geocode(embassies[1])[0]['formatted_address']
print "The closest embassy is located at %s" %ClosestEmbassy
# if I wanted to hold a morning meeting there, which cafe would you suggest?
cafes = gmaps.places('cafe near ' + ClosestEmbassy)
CafeDist = []
for i in range(0,20):
    directions = gmaps.directions(ClosestEmbassy,cafes['results'][i]['formatted_address'])
    Distance = directions[0]['legs'][0]['distance']
    DistanceInMeters = round(meterconverter(float(Distance[u'text'][:-3])),2)
    CafeDist.append(DistanceInMeters)
m = min(CafeDist)
ClosestCafeIndex = [i for i, j in enumerate(CafeDist) if j == m][0]
print "The closest cafe is %s, which is %s meters away." %(cafes['results'][ClosestCafeIndex]['name'],CafeDist[ClosestCafeIndex])

# if I wanted to hold an evening meeting there, which bar would you suggest?
bars = gmaps.places('bar near ' + ClosestEmbassy)
BarRating = []
for i in range(0,len(bars)):
    BarRating.append(bars['results'][i]['rating'])
m = max(BarRating)
BestBarIndex= [i for i, j in enumerate(BarRating) if j == m][0]
print "The best bar is %s, which is rated %s stars" %(bars['results'][BestBarIndex]['name'], BarRating[BestBarIndex])
