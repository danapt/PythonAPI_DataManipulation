"""
How many distinct starships are associated with Darth Vader and Luke Skywalker?
author: Daniel Apetri

"""

from urllib.request import Request, urlopen
from json import loads


def read_api(url):

    #get the data from the api in a list named results
    results = []
    while url != None:
        req = Request(url, None, {
            'User-agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'
        })
        data = loads(urlopen(req).read().decode("utf-8"))
        results.extend(data['results'])
        url = data['next']

    return results


def num_starships_associated(result):

    res = []

    for people in result:
        if people['name'] == "Luke Skywalker":
            res = people['starships']
        elif people['name'] == 'Darth Vader':
            res = res + people['starships']

    print (res)
    print ("the number of ships associated with Luke Skywalker and Darth Vader are : ", len(res))


def main():

    results = read_api('https://swapi.dev/api/people')
    num_starships_associated(results)

if __name__ == '__main__':
    main()