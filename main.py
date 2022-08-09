import json
import re
import random

f = open("readme.json")

dataSet = json.load(f)

dataSetNew = {}

for key in dataSet:

	matchGroup = re.match(r'rx_queue_(\d+)_packets',key)

	if(matchGroup):

	    random_num = random.randint(0,500)

	    dataSet[key] = dataSet[key] + random_num


print(dataSet)

print(dataSetNew)

f.close()