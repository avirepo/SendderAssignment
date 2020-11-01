import json
from datetime import datetime

import cachetools.func
import urllib3

BASE_URL = 'https://ghibliapi.herokuapp.com/'
http = urllib3.PoolManager()


class People:
    """
    Meta class for keeping records of peoples as people object need
    to put in set to each film should contain only single entry of
    one people by overriding _eq__ and __hash__ function using
    people id we can achieve this by default set behaviour
    """

    def __init__(self, **kwargs):
        self.people_id = kwargs.get('id')
        self.name = kwargs.get('name')
        self.gender = kwargs.get('gender')
        self.age = kwargs.get('age')
        self.hair_color = kwargs.get('hair_color')
        self.species = kwargs.get('species')

    def __eq__(self, other):
        return self.people_id == other.people_id

    def __hash__(self):
        return hash(self.people_id)

    def __repr__(self):
        return json.dumps(self.to_dict())

    def __str__(self):
        return self.name

    def to_dict(self):
        return {
            'people_id': self.people_id,
            'name': self.name,
            'gender': self.gender,
            'age': self.age,
            'hair_color': self.hair_color,
            'species': self.species,
        }


def ghibli_api_get_helper(path):
    res = http.request('GET', f'{BASE_URL}{path}')
    return json.loads(res.data.decode('utf-8'))


def get_films_people_dict():
    peoples = ghibli_api_get_helper('people')
    films_people_dict = {}
    for people in peoples:
        films = people.get('films')
        for film in films:
            film_id = film.partition(f'{BASE_URL}films/')[2]
            # Get empty or existing set for the people belong to
            # the provided film id
            entry = films_people_dict.get(film_id, set())
            entry.add(People(**people))
            # save set
            films_people_dict[film_id] = entry
    return {
        key: list(value) for key, value in films_people_dict.items()
    }


@cachetools.func.ttl_cache(ttl=60)
def get_movies_data():
    print('Refreshing cache with latest call at', datetime.now())
    films_people_map = get_films_people_dict()
    films = ghibli_api_get_helper('films')
    for film in films:
        film['people'] = list(
            map(lambda ele: str(ele),
                films_people_map.get(
                    film.get('id'), ['No one watched'])
                )
        )

    return films
