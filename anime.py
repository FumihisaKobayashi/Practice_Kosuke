import requests
from pprint import pprint

URL = "http://api.moemoe.tokyo/anime/v1/master/2020"

def get_anime_list():
    r = requests.get(URL)
    return r.json()

if __name__ == "__main__":
    pprint(get_anime_list())
