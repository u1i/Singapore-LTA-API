from geopy.geocoders import Nominatim
from geopy.distance import vincenty
geolocator = Nominatim()

loc1=(1.283897,103.8511256)
loc2=(1.3032469,103.8129041)
# Raffles Place
location1 = geolocator.reverse(loc1)

# Orchard Towers
location2 = geolocator.reverse(loc2)
print(location1.address)
print(location2.address)

# Print distance
print(vincenty(loc1, loc2).meters)
