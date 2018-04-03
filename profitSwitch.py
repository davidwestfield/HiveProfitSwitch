import json
import requests

# Fetches api data. This link changes every minute
r = requests.get('https://api.nicehash.com/api?method=simplemultialgo.info')
data = r.json()

# Sorts paying for each algo into a dictionary
paying = {}
speed = {}
for a in data['result']['simplemultialgo']:
    paying.update({a['name']:a['paying']})
    speed.update({a['name']:0})

# EDIT THIS
# Your speed for each algorithim. Double check units

speed['daggerhashimoto'] = 0.400
speed['equishash'] = 400



# Prints profability
for a in paying:
    profit = float(paying[a]) * speed[a]
    print("%s: %f btc" % (a, profit))


# fetch usd



# get machine hashrate for reasonable algorithims

# multiple our hashrates by those

# sort results

# siwtch miner to whichever one is best

# run this on a curl script


# todo: change to average over time
