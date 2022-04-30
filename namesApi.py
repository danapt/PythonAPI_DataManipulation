from urllib.request import Request, urlopen
from json import loads
import ssl


def open_readApi(results):

    url = "https://swapi.dev/api/people"
    while url != None:
        req = Request(url, None, {
            'User-agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'
            })
    data = loads(urlopen(req).read().decode("utf-8"))
    results.append(data['results'])
    url = data['next']

    print(len(results))
    print (results)
    return results


def count_names(results):

    list = []
    count = 0
    for i in results:
        if ('name' == i):
            list = list.append(i+1)
            count +=1
    print(count)
    print (list)






def main():

    results = []
    open_readApi(results)
    count_names(results)


if __name__ == "__main__":
        main()
