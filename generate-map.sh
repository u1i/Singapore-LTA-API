echo Generating inserts...
python generate_MapInserts.py | grep -v busgreen > inserts.inc
echo Concatenating...

# for this to work please create a file called googlemaps-key.inc and copy paste your Google Maps key into it. echo $key > googlemaps-key.inc

google=$(cat googlemaps-key.inc)

cp map-1.html out.html
cat inserts.inc >> out.html
cat map-2.html | sed "s/GOOGLE_KEY/$google/;" >> out.html
