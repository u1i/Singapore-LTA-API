import json
import pycurl
from StringIO import StringIO
from datetime import datetime
import calendar
import pytz

endpoint="http://datamall2.mytransport.sg/ltaodataservice/BusArrivalv2"

execfile("apikey.cfg")
execfile("stops.cfg")

alert_stops=[]
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

	astop={}

	astop["code"] = stop["code"]
	levels=[]

	astop["services"] = []
	for s in data["Services"]:
		aservice={}
		l = s["NextBus"]["Load"]
		eta = s["NextBus"]["EstimatedArrival"].replace("+08:00","")
		aservice["service"] = s["ServiceNo"]
		aservice["load"] = l
		aservice["eta"] = eta
		astop["services"].append(aservice)

		levels.append(l)

	astop["level"] = "green"

	if "SDA" in levels:
		astop["level"] = "orange"

	if "LSD" in levels:
		astop["level"] = "red"
	
	alert_stops.append(astop)

print "stopsWithLoads = " + str(alert_stops)
print "singapore_timestamp = " + '"' + str(datetime.now(pytz.timezone('Asia/Singapore'))) + '"'

d = datetime.utcnow()
unixtime = calendar.timegm(d.utctimetuple())
print "utime = " + '"' + str(unixtime) + '"'


