"""
List the names of all planets sorted by (one list each)
●	diameter in ascending order
●	population in descending order

author: Daniel Apetri
"""
from urllib.request import Request, urlopen
from json import loads
import operator

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

def sort_by_population(data):

    i =[]
    count =0
    num_population = 0
    for population in data:
        #check if population['population'] == 'unknown' and replace with 0
        if population['population'] == 'unknown':
            population['population'] = '0'
        num_population = int(population['population'])
        i.extend([num_population],)
        count += 1

    print (i)
    print ("number of planets",count)

def sort_by_diameter(data):

    i = []
    count = 0
    num_diameter = 0
    for diameter in data:
        if diameter['diameter'] == 'unknown':
            diameter['diameter'] = '0'
        num_diameter = int(diameter['diameter'])
        i.extend([num_diameter],)
        count += 1

    print (i)
    print(count)

def sort_by_diameter1(data):

    dict = {}
    i = 0

    for diameter in data:
        if diameter['diameter'] == 'unknown':
            diameter['diameter'] = '0'
        i= int(diameter['diameter'])
        dict.setdefault(diameter['name'],[])
        dict[diameter['name']].append(i)
    return dict

def sort_by_population1(data):


    dict = {}
    i = 0
    for population in data:
        if population['population'] == 'unknown':
            population['population'] = '0'
        i= int(population['population'])
        dict.setdefault(population['name'],[])
        dict[population['name']].append(i)
    return dict

def sort_ascending(dict):

    count = 0

    sorted_dict = sorted(dict.items(), key=lambda kv: kv[1])

    for key, value in sorted_dict:
        print(key, value)
        count+=1

    print("number of planets", count)



def main():

    results = read_api("https://swapi.dev/api/planets/")
    #print (results)
    #sort_by_population(results)
    #sort_by_diameter(results)
    dictionary = sort_by_population1(results)
    dictionary1 = sort_by_diameter1(results)
    sort_ascending(dictionary)
    sort_ascending(dictionary1)

if __name__ == '__main__':
    main()