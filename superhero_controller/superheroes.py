from typing import Dict

import requests


class Superheroes:
    def __init__(self) -> None:
        self.host = 'https://superhero.qa-test.csssr.com'

    def superheroes_get(self) -> requests.Response:
        url = f'{self.host}/superheroes'
        response = requests.get(url=url)
        return response

    def superheroes_post(self, dto: Dict) -> requests.Response:
        url = f'{self.host}/superheroes'
        responce = requests.post(url=url, json=dto)
        return responce

    def superheroes_id_get(self, id: int) -> requests.Response:
        url = f'{self.host}/superheroes/{id}'
        responce = requests.get(url=url)
        return responce

    def superheroes_id_put(self, id: int) -> requests.Response:
        url = f'{self.host}/superheroes/{id}'
        responce = requests.put(url=url)
        return responce

    def superheroes_id_delete(self) -> requests.Response:
        url = f'{self.host}/superheroes/{id}'
        responce = requests.delete(url=url)
        return responce
