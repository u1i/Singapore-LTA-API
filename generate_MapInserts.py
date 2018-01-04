execfile("stops.cfg")
execfile("busStopsWithLoads.cfg")

for s in stopsWithLoads:
	code = s["code"]
	level = s["level"]
	svc = s["services"]

	svc_str=""

	for service in svc:
		if service["load"] == "LSD":
			svc_str = svc_str + " Bus " + service["service"] + " full | "
		elif service["load"] == "SDA":
			svc_str = svc_str + " Bus " + service["service"] + " standing only | "
	for lookup in stops:
		if lookup["code"] == code:
			road = lookup["road"].replace("'"," ")
			lat = lookup["lat"]
			lon = lookup["lon"]

	print "{ position: new google.maps.LatLng(" + str(lat) + "," + str(lon) + "), type: 'bus" + str(level) + "', title: '" + str(road) + "', text: '" + svc_str + "' },"
