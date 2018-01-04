ts=$(export TZ="Asia/Singapore";date +%Y%m%d-%H%M)

python getBusyBusStops.py > busStopsWithLoads.cfg

cp busStopsWithLoads.cfg data/busStopsWithLoads-$ts.cfg
