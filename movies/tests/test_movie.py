# Create your tests here.
import json
from unittest import mock

from django.test import TestCase
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIClient

from movies.helpers import (
    get_films_people_dict, get_movies_data
)
from movies.tests.mock_data import (
    FILMS, MOVIE_DATA, PEOPLE,
    PEOPLE_FILM_MAP
)

client = APIClient()


class MoviesTestCases(TestCase):
    def test_movies(self):
        response = client.get(
            reverse('movie_list', ))
        self.assertEqual(
            response.status_code, status.HTTP_200_OK,
            'It should return 200 with movie list'
        )


class MovieHelperTest(TestCase):

    @mock.patch(
        'movies.helpers.ghibli_api_get_helper',
        return_value=PEOPLE
    )
    def test_get_films(self, *args):
        """
        Test whether the people function is removing
        duplicate people in film or not as we have copy some people
        multiple time
        """
        response = get_films_people_dict()
        movie_id = '2baf70d1-42bb-4437-b551-e5fed5a87abe'
        # Length of return people objects in film should be same
        # even data is duplicate
        self.assertEqual(
            len(response.get(movie_id)),
            len(PEOPLE_FILM_MAP.get(movie_id)),
            'Return result should be equal to mocked api'
        )

    @mock.patch(
        'movies.helpers.ghibli_api_get_helper',
        return_value=FILMS
    )
    @mock.patch(
        'movies.helpers.get_films_people_dict',
        return_value=PEOPLE_FILM_MAP
    )
    def test_get_movies_data(self, people_map, film_fun):
        response = get_movies_data()
        film_fun.assert_called_with('films')
        people_map.assert_called_with()
        self.assertEqual(json.dumps(response), json.dumps(MOVIE_DATA))
