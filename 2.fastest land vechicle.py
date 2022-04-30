"""
What is the fastest land vehicle?
author Daniel Apetri
"""

from urllib.request import Request, urlopen
from json import loads

def get_api(url):

    results = []
    while url != None:
        req = Request(url, None, {
            'User-agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'
        })
        data = loads(urlopen(req).read().decode("utf-8"))
        results.extend(data['results'])
        url = data['next']
        print (results)

    return results

def check_fastest(results):

    fast = 0
    count =0
    zero = 0

    for vehicle in results:
        if vehicle['max_atmosphering_speed'] == 'unknown':
            vehicle['max_atmosphering_speed'] = '0'
        vehicle_int = int(vehicle['max_atmosphering_speed'])
        count +=1
        if fast < vehicle_int:
            fast = vehicle_int

    print("the fastest land vehicle has the speed  : ", fast)
    print(count)


def main():

    results = get_api('https://swapi.dev/api/vehicles')
    check_fastest(results)

if __name__ == "__main__":
    main()
