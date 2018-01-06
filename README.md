# Experimenting with Singapore LTA APIs

Using open data from Land Transport Authority (LTA) to find out which bus stops at a given time are very popular and result in packed bus services.

Here are the [interactive maps with data snapshots](http://lta.sotong.io/maps/) on Google Maps

## How to ?
![sample](https://raw.githubusercontent.com/u1i/Singapore-LTA-API/master/sample-map.png)

![](https://raw.githubusercontent.com/u1i/Singapore-LTA-API/master/analysis/SG-20180105.png)

1 - Request access on the [LTA website](https://www.mytransport.sg/content/mytransport/home/dataMall.html)

2 - Make sure you read the [Terms of Service](https://www.mytransport.sg/content/mytransport/home/dataMall/apitermsofservice.html)

3 - Check out the [API Documentation](https://www.mytransport.sg/content/dam/mytransport/DataMall_StaticData/LTA_DataMall_API_User_Guide.pdf)

4 - clone this repository and create a file called 'apikey.cfg' with the following content:

`AccountKey="[your key]"`

Example:

AccountKey="WW91cktleTEyQ1Njc4=="

for Google Maps take a note of your key ID and put it in a file called googlemaps-key.inc

5 - test the scripts

