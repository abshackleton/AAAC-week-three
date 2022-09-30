address_data = {'Adam': '127 Charming Avenue', 'Roger': '66 Tennis Street'}
wins_data = {'Adam': 2023, 'Roger': [2003, 2004, 2005, 2006, 2007, 2009, 2012, 2017]}

print(address_data['Adam'])
print(wins_data['Roger'])

for key in address_data:
    print(key, '=', address_data[key])

print(wins_data.keys())
print(wins_data.values())

print(wins_data.items())
for key, value in wins_data.items():
    print(key, '=', value)

# side note about interating over lists / dictionaries
# when looping over a list e.g.
animals = ["badger", "meercat", "rhino", "llama"]

# don't do this
for animal in range(len(animals)):
    print(animal)

# do this
for animal in animals:
    print(animal)

# end side note

# cast the keys to a list of keys
wins_data_keys = list(wins_data.keys())

# this isn't a python command, you need to run it from the windows command line
# python -m pip install requests

import json
import requests

base_url = 'http://rest.genenames.org/fetch/'
query = 'symbol/PPIA'

additional_headers = {'Accept': 'application/json'}

full_url = base_url + query
print(url)

r = requests.get(url=full_url, headers=additional_headers)
print(r.status_code)
print(json.dumps(r.json(), indent=2))

print(dir(r))
r.text
r.content
r.json()
r.status_code
r.headers

