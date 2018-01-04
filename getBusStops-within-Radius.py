import json
import pycurl
from StringIO import StringIO

from geopy.geocoders import Nominatim
from geopy.distance import vincenty

geolocator = Nominatim()

# the centre of the circle
reference_location = (1.283897,103.8511256)

# radius in metres
radius = 5000.0

endpoint="http://datamall2.mytransport.sg/ltaodataservice/BusStops"

execfile("apikey.cfg")

stops=[]

for sk in 0,500,1000,1500,2000,2500,3000,3500,4000,4500:

	buffer = StringIO()
	c = pycurl.Curl()
	c.setopt(pycurl.HTTPHEADER, ['AccountKey: ' + AccountKey])
	c.setopt(c.URL, endpoint + "/?$skip=" + str(sk))
	c.setopt(c.WRITEDATA, buffer)
	c.perform()
	c.close()
	
	body = buffer.getvalue()
	data = json.loads(body)
	
	stops1 = data['value']

	for stop in stops1:
		stops.append(stop)

# print stops

relevant_stops=[]	
for stop in stops:
	code = stop["BusStopCode"]
	road = stop["RoadName"]
	lat = stop["Latitude"]
	lon = stop["Longitude"]

	loc = (float(lat), float(lon))
	distance = (vincenty(reference_location, loc).meters)

	if distance < radius:
		# print code, road, lat, lon, distance
		rstop = {}
		rstop["code"] = code
		rstop["road"] = road
		rstop["lat"] = lat
		rstop["lon"] = lon
		
		relevant_stops.append(rstop)
		# print str(lat) + "," + str(lon)
		# print code

print "stops = " + str(relevant_stops)
