"""
What species appears the second-most often in a film?
author Daniel Apetri
"""

from urllib.request import Request, urlopen
from json import loads
from heapq import nlargest


def read_api(url):

    results = []
    while url != None:
        req = Request(url, None, {
            'User-agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'
        })
        data = loads(urlopen(req).read().decode("utf-8"))
        results.extend(data['results'])
        url = data['next']

    return results

def second(data):

    res = {}
    for species in data:
        res.setdefault(species['name'], [])
        res[species['name']].append(len(species['films']))

    largest = 0
    #second_largest = max(res.items(), key = lambda x:x[1])

    sorted_dict = sorted(res.items(), key=lambda kv: kv[1])

    #second_largest = nlargest(2,res, key=res.get,)

    count  = 0
    for key,values in res.items():
        for i in values:
            if largest < i:
                largest = i
    first = second = float('-inf')

    for key,values in sorted_dict:
        for i in values:
            if i > first:
                second = first
                first = i

    for key,values in res.items():
        for i in values:
            if i == second:
                print(key)
    print (second)
def main():

    data = read_api("https://swapi.dev/api/species/")
    second(data)
if __name__ == '__main__':
    main()