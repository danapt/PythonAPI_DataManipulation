"""
List all of the flying vehicles sorted by cargo capacity in ascending order

"""

from urllib.request import Request, urlopen
from json import loads
import operator



def get_api(url):

    results = []
    while url != None:

        req = Request(url, None, {
            'User-agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'
        })
        data = loads(urlopen(req).read().decode("utf-8"))
        results.extend(data['results'])
        url = data['next']
        #print(results)

    return results

def put_data_in_dictionary(data):

    dict = {}
    i = 0
    for starship in data:
        if starship['cargo_capacity'] == 'unknown':
            starship['cargo_capacity'] = '0'
        i = int(starship['cargo_capacity'])
        dict.setdefault(starship['name'],[])
        dict[starship['name']].append(i)

    return dict

def sort_ascending(dict):

    sorted_dict= sorted(dict.items(), key=lambda kv:kv[1])

    for key in sorted_dict:
        print (key)


def main():

    data = get_api("https://swapi.dev/api/starships/")
    dict = put_data_in_dictionary(data)
    sort_ascending(dict)

if __name__ == "__main__":
    main()