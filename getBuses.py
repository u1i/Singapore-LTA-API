import json
import pycurl
from StringIO import StringIO

endpoint="http://datamall2.mytransport.sg/ltaodataservice/BusServices"

execfile("apikey.cfg")

# print "Using AccountKey " +str(AccountKey)

# Get the first batch
buffer = StringIO()
c = pycurl.Curl()
c.setopt(pycurl.HTTPHEADER, ['AccountKey: ' + AccountKey])
c.setopt(c.URL, endpoint)
c.setopt(c.WRITEDATA, buffer)
c.perform()
c.close()

body = buffer.getvalue()
data = json.loads(body)

services1 = data['value']

# Get the second batch
buffer2 = StringIO()
c = pycurl.Curl()
c.setopt(pycurl.HTTPHEADER, ['AccountKey: ' + AccountKey])
c.setopt(c.URL, endpoint + "/?$skip=500")
c.setopt(c.WRITEDATA, buffer2)
c.perform()
c.close()

body = buffer2.getvalue()
data = json.loads(body)

services2 = data['value']

# Concat both lists
services = services1 + services2

for service in services:
	print str(service['ServiceNo'])

