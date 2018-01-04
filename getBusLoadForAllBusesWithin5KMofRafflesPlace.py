import json
import pycurl
from StringIO import StringIO

endpoint="http://datamall2.mytransport.sg/ltaodataservice/BusArrivalv2"

execfile("apikey.cfg")
execfile("stops.cfg")


for stop in stops:

	buffer = StringIO()
	c = pycurl.Curl()
	c.setopt(pycurl.HTTPHEADER, ['AccountKey: ' + AccountKey])
	c.setopt(c.URL, endpoint + "/?BusStopCode=" + str(stop["code"]))
	c.setopt(c.WRITEDATA, buffer)
	c.perform()
	c.close()
	
	body = buffer.getvalue()
	data = json.loads(body)

	for s in data["Services"]:
		l = s["NextBus"]["Load"]
		if l != "SEA":
			print str(stop["code"]) + " " + str(s["ServiceNo"]) + " " +  str(l)
