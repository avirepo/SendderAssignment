FILMS = [
    {
        "id": "2baf70d1-42bb-4437-b551-e5fed5a87abe",
        "title": "Castle in the Sky",
        "description": "The orphan Sheeta inherited a mysterious ",
        "director": "Hayao Miyazaki",
        "producer": "Isao Takahata",
        "release_date": "1986",
        "rt_score": "95",
        "people": [
            "https://ghibliapi.herokuapp.com/people/"
        ],
        "species": [
            "https://ghibliapi.herokuapp.com/species/af3910a6-429f"
            "-4c74-9ad5-dfe1c4aa04f2"
        ],
        "locations": [
            "https://ghibliapi.herokuapp.com/locations/"
        ],
        "vehicles": [
            "https://ghibliapi.herokuapp.com/vehicles/"
        ],
        "url": "https://ghibliapi.herokuapp.com/films/2baf70d1-42bb"
               "-4437-b551-e5fed5a87abe"
    }
]

PEOPLE = [
    {
        "id": "fe93adf2-2f3a-4ec4-9f68-5422f1b87c01",
        "name": "Pazu",
        "gender": "Male",
        "age": "13",
        "eye_color": "Black",
        "hair_color": "Brown",
        "films": [
            "https://ghibliapi.herokuapp.com/films/2baf70d1-42bb"
            "-4437-b551-e5fed5a87abe",
            "https://ghibliapi.herokuapp.com/films/2baf70d1-42bb"
            "-4437-b551-e5fed5a87abe"
        ],
        "species": "https://ghibliapi.herokuapp.com/species"
                   "/af3910a6-429f-4c74-9ad5-dfe1c4aa04f2",
        "url": "https://ghibliapi.herokuapp.com/people/fe93adf2"
               "-2f3a-4ec4-9f68-5422f1b87c01"
    },
    {
        "id": "598f7048-74ff-41e0-92ef-87dc1ad980a9",
        "name": "Lusheeta Toel Ul Laputa",
        "gender": "Female",
        "age": "13",
        "eye_color": "Black",
        "hair_color": "Black",
        "films": [
            "https://ghibliapi.herokuapp.com/films/2baf70d1-42bb"
            "-4437-b551-e5fed5a87abe"
        ],
        "species": "https://ghibliapi.herokuapp.com/species"
                   "/af3910a6-429f-4c74-9ad5-dfe1c4aa04f2",
        "url": "https://ghibliapi.herokuapp.com/people/598f7048"
               "-74ff-41e0-92ef-87dc1ad980a9"
    }
]

PEOPLE_FILM_MAP = {
    '2baf70d1-42bb-4437-b551-e5fed5a87abe': [{
        "people_id":
            "598f7048-74ff-41e0-92ef-87dc1ad980a9",
        "name": "Lusheeta "
                "Toel Ul "
                "Laputa",
        "gender": "Female",
        "age": "13",
        "hair_color": "Black",
        "species": "https://ghibliapi.herokuapp.com/species"
                   "/af3910a6-429f-4c74-9ad5-dfe1c4aa04f2"
    },
        {
            "people_id": "fe93adf2-2f3a-4ec4-9f68-5422f1b87c01",
            "name": "Pazu",
            "gender": "Male",
            "age": "13",
            "hair_color": "Brown",
            "species": "https://ghibliapi.herokuapp.com/species"
                       "/af3910a6-429f-4c74-9ad5-dfe1c4aa04f2"
        }
    ]
}

MOVIE_DATA = [
    {
        'id': '2baf70d1-42bb-4437-b551-e5fed5a87abe',
        'title': 'Castle in the Sky',
        'description': 'The orphan Sheeta inherited a '
                       'mysterious ',
        'director': 'Hayao Miyazaki',
        'producer': 'Isao Takahata', 'release_date': '1986',
        'rt_score': '95', 'people': [
        "{'people_id': '598f7048-74ff-41e0-92ef-87dc1ad980a9', "
        "'name': 'Lusheeta Toel Ul Laputa', 'gender': 'Female', "
        "'age': '13', 'hair_color': 'Black', 'species': "
        "'https://ghibliapi.herokuapp.com/species/af3910a6-429f"
        "-4c74-9ad5-dfe1c4aa04f2'}",
        "{'people_id': 'fe93adf2-2f3a-4ec4-9f68-5422f1b87c01', "
        "'name': 'Pazu', 'gender': 'Male', 'age': '13', "
        "'hair_color': 'Brown', 'species': "
        "'https://ghibliapi.herokuapp.com/species/af3910a6-429f"
        "-4c74-9ad5-dfe1c4aa04f2'}"
    ],
        'species': [
            'https://ghibliapi.herokuapp.com/species'
            '/af3910a6-429f-4c74-9ad5-dfe1c4aa04f2'],
        'locations': [
            'https://ghibliapi.herokuapp.com/locations/'],
        'vehicles': [
            'https://ghibliapi.herokuapp.com/vehicles/'],
        'url': 'https://ghibliapi.herokuapp.com/films/2baf70d1-42bb'
               '-4437-b551-e5fed5a87abe'
    }
]
