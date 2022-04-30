"""
How many people are returned by the API? Show how you can solve this without using the results count attribute
author Daniel Apetri
"""

from urllib.request import Request, urlopen
from json import loads

url = 'https://swapi.dev/api/people'
results = []
while url is not None:
    req = Request(url, None, {
        'User-agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'
    })
    data = loads(urlopen(req).read().decode("utf-8"))
    results.extend(data['results'])
    url = data['next']

# print(len(results))
count = 0
for person in results:
    # print(person)
    if person['name']:
        print(person['name'])
        count += 1
print(count)
