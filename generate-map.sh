echo Getting bus stop loads...
./getStopsWithLoad.sh

echo Generating inserts...ignoring bus stops where all buses look ok
python generate_MapInserts.py | grep -v busgreen > inserts.inc
echo Concatenating...

#ts=$(export TZ="Asia/Singapore";date +%Y%m%d-%H%M)
#out="out/sg-$ts.html"

ts=$(export TZ="Asia/Singapore";date +%Y-%m-%d/%H-%M)
out="maps/$ts.html"
dir=$(dirname $out)
mkdir -p $dir 2>/dev/null

# for this to work please create a file called googlemaps-key.inc and copy paste your Google Maps key into it. echo $key > googlemaps-key.inc

google=$(cat googlemaps-key.inc)

cp map-1.html $out
cat inserts.inc >> $out
cat map-2.html | sed "s/GOOGLE_KEY/$google/;" >> $out

# regenrate the index document in the 'out' dir
./generate-index.sh

