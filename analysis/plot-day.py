import pylab
import random
import math

data = pd.read_csv('20180105.dataset')

data.head()


pylab.figure(figsize=(14, 6), facecolor='w') 
red = []
green = []
yellow = []
hours = []
hours_disp = []

for i in range(len(data["time"])-1):
    hours.append(data["time"][i+1])

for i in range(0, len(data["time"])-1,8):
    hours_disp.append(data["time"][i+1])

for i in range(len(data["time"])-1):
    red.append(data["red"][i+1])

for i in range(len(data["time"])-1):
    yellow.append(data["yellow"][i+1])
    
for i in range(len(data["time"])-1):
    green.append(data["green"][i+1])
    
pylab.title('Singapore Buses 2017-01-05')
pylab.xlabel('Hour')
pylab.ylabel('Number of full Buses')
pylab.xticks(range(0, len(data["time"])-1,8), hours_disp)

#frame = pylab.gca()
#frame.axes.get_xaxis().set_ticklabels([])

pylab.plot(hours, red, color='red')
#pylab.plot(green, color='green')
#pylab.plot(yellow, color='orange')

pylab.show() # show figure on screen
