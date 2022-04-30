"""
Which character has the most associated films? When was the first and last of their films released?
author : Daniel Apetri

"""
from urllib.request import Request, urlopen
from json import loads
import operator

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
    results = ""
    i = 0
    while url != None:
        req = Request(url, None, {
            'User-agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'
        })
        data = loads(urlopen(req).read().decode("utf-8"))
        results = results + (data['release_date'])
        if url:
            break

    #print(results)
    return results

def character_in_films(data):

    #i will add the data of names and films in this dictionary
    films = {}
    for characters in data:
        films.setdefault(characters['name'],[])
        films[characters['name']].append(characters['films'])

    #print(films)
    return films

def most_films(films):
    #calculate the person who has the most films associated
    max = 0
    for pers in films:
        temp = len(pers['films'])
        if max < temp:
            max = temp
            name = pers['name']
    print('number of films',max)
    print('name of the character',name)

    return name

def release(name):

    data = read_api("https://swapi.dev/api/people/")
    film2 = ""
    film1 = ""

    for person in data:
        if person['name'] == name:
            if ('1') in person['films']:
                person['films'][0] = person['films']
            else:
                film1 = person['films'][0]
                film2 = person['films'][len(person['films']) - 1]



    f = read_api1(film1)
    f2 = read_api1(film2)

    print(f)
    print(f2)

def main():

    data = read_api("https://swapi.dev/api/people/")

    str = most_films(data)
    release(str)

if __name__ == '__main__':
    main()