import json
import requests

# THAT LINK CHANGES EVEYR MINUTE
r = requests.get('https://api.nicehash.com/api?method=simplemultialgo.info')
data = r.json()

algos = {}

for a in data['result']['simplemultialgo']:
    algos.update({a['name']:a['paying']})

print algos



# get machine hashrate for reasonable algorithims

# multiple our hashrates by those

# sort results

# siwtch miner to whichever one is best

# run this on a curl script


# todo: change to average over time
