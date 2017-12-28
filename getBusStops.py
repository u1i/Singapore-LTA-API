import json
import pycurl
from StringIO import StringIO

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

for stop in stops:
	print str(stop["Latitude"]) + ", " + str(stop["Longitude"])

