"""
What is the name and planet origin of the species is associated with the largest number of characters (people)?
author Daniel Apetri
"""

from urllib.request import Request, urlopen
from json import loads


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


def read_api1(url):
    results = ""
    while url != None:
        req = Request(url, None, {
            'User-agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'
        })
        data = loads(urlopen(req).read().decode("utf-8"))
        results = results + (data['name'])
        break

    return results


def name_origin(data):
    max = 0
    # find the maximum amount of people
    for species in data:
        temp = len(species['people'])
        if max < temp:
            max = temp

    # for in data to get from the API the data that is in people[homeworld] to find the planet of the race
    for species in data:
        if max == len(species['people']):
            url_planet_name = species['homeworld']
            planet_name = read_api1(url_planet_name)
            print("the species that is associated with the largest number of characters(people) is : ", species['name'],
                  "\nthe name of planet is : ", planet_name)


def main():
    data = read_api("https://swapi.dev/api/species/")
    # print(data)
    name_origin(data)


if __name__ == '__main__':
    main()
