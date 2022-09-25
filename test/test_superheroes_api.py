import asserts
import pytest
from pydantic import ValidationError

from superhero_controller.superheroes import Superheroes
from dataclass import Superhero
from utils import is_get_superheroes_response_status_is_ok, get_superheroes


#  фикстура, вызывающая экземпляр класса Superheroes
@pytest.fixture()
def superheroes() -> Superheroes:
    return Superheroes()


#  тест на проверку ответа от метода get superheroes
def test_get_superheros__is_ok(superheroes: Superheroes) -> None:
    is_get_superheroes_response_status_is_ok(superheroes=superheroes)


def test_get_superheroes_list(superheroes: Superheroes) -> None:
    # получаем список супергероев
    # с помощью, нотации типов мы валидируем, что получаем список
    superheroes_list = get_superheroes(superheroes=superheroes)
    # Так мы не знаем точных данных, которые должны получить,
    # то сравниваем, что записи в списке супергероев соответсвуют модели в сваггере.
    # Модель описана в dataclass.py c использованием pydantic,
    # который позволяет произвести валидацию данных на соответствие модели
    try:
        for superhero in superheroes_list:
            Superhero(**superhero)
    except ValidationError as error_message:
        message = error_message
    else:
        message = 'Success'
    asserts.assert_equal(
        'Success',
        message,
        f'Не пройдена валидация данных супергероев. Сообщение об ошибке - {message}',
    )
