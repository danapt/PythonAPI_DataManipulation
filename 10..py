"""
What what is the producer’s name who has been involved the greatest number of films?
author Daniel Apetri

"""

from urllib.request import Request, urlopen
from json import loads


# read data from the api and added to a list
def read_api(url):
    films = []
    while url != None:
        req = Request(url, None, {
            'User-agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'
        })
        data = loads(urlopen(req).read().decode("utf-8"))
        films.extend(data['results'])
        url = data['next']

    return films


def producer_name(data):
    count = 1
    max = 0
    producers_list = []
    for films in data:
        producers_list.extend(films['producer'].split(','))

    producers_list.sort()
    print(producers_list)
    for i in range(len(producers_list) - 1):
        if producers_list[i] in producers_list[i + 1]:
            count += 1
        if max < count:
            max = count
            name = producers_list[i]
    print("the producer who is involved in the greatest number of films is : ", name, "and the number is :", max)


def main():
    """call the function read_api to get all the data from the url = https://swapi.co/api/films/ and put it in a list
    """
    films = read_api("https://swapi.dev/api/films/")
    # function to find the producers name that is involved in the most films
    producer_name(films)


if __name__ == '__main__':
    main()
