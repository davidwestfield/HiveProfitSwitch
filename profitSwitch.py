import json
import requests
from operator import itemgetter

# Fetches api data. This link changes every minute
r = requests.get('https://api.nicehash.com/api?method=simplemultialgo.info')
data = r.json()

# Sorts paying for each algo into a dictionary
paying = {}
speed = {}
for a in data['result']['simplemultialgo']:
    paying.update({a['name']: a['paying']})
    speed.update({a['name']: 0})

# EDIT THIS (Later it will fetch machine hashrate)
# Your speed for each algorithim. Double check units
speed['daggerhashimoto'] = 0.186
speed['equihash'] = 0.00000258

# Finds and sorts profability
profability = {}
for a in paying:
    profit = round(float(paying[a]) * speed[a], 5)
    if profit > 0:
        profability.update({a: profit})
sortedProfit = sorted(profability.items(), key=lambda x: x[1], reverse=True)

# Prints results
for x in sortedProfit:
    print x[0], x[1], "btc"


# fetch usd

# switch miner
