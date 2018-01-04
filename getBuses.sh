#!/bin/bash

endpoint="http://datamall2.mytransport.sg/ltaodataservice/BusServices"

source apikey.cfg

if [ "$AccountKey" = "" ]
then
        echo ERROR: could not read AccountKey from apikey.cfg
        exit 1
fi

echo "AccountKey: $AccountKey"

curl -H "AccountKey:$AccountKey" "$endpoint" > buses.1
curl -H "AccountKey:$AccountKey" "$endpoint?\$skip=500" > buses.2
