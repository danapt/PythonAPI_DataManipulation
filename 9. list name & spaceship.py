"""
For all people associated with spaceships, list their names, the spaceships’ names and the cost of each spaceship
author Daniel Apetri
"""

from urllib.request import Request, urlopen
from json import loads

#read data from the api and added to a list
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

#read data from the api and added to a list
def read_api1(url):
    results = []
    while url != None:
        req = Request(url, None, {
            'User-agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'
        })
        data = loads(urlopen(req).read().decode("utf-8"))
        results.append(data['name'])
        results.append(data['cost_in_credits'])
        break


    return results

def people_starships_cost(data):

    """
    go in the data list and print people name and after go to a different url and read from there the name of the spaceship and cost

    """
    for people in data:
        print("Name : ", people['name'])
        if len(people['starships']) == 0:
            print("no ships associated with this character")
        else:
            for i in people['starships']:
                url_starship = i
                list = read_api1(url_starship)
                print(list)


def main():

    data = read_api("https://swapi.dev/api/people/")
    people_starships_cost(data)

if __name__ == '__main__':
    main()