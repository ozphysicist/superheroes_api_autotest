from typing import Dict, List

from superhero_controller.superheroes import Superheroes

import asserts


def is_get_superheroes_response_status_is_ok(superheroes: Superheroes) -> None:
    response = superheroes.superheroes_get()
    asserts.assert_equal(
        200,
        response.status_code,
        f'Ожидаемый ответ от сервиса - 200, фактический - {response.status_code}',
    )


def get_superheroes(superheroes: Superheroes) -> List[Dict]:
    response = superheroes.superheroes_get()
    result = response.json()
    return result
