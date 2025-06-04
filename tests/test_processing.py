from typing import Dict, List

from src.processing import filter_by_state, sort_by_date

"""Импортируем аннотацию и функции из processing.py"""


def test_filter_by_state_executed(filter_processing_state_date: List[Dict], state: str = "EXECUTED") -> None:
    """
    Функция тестирует модуль processing на параметр state="EXECUTED"
    :param filter_processing_state_date: Фикстура подтягивается из conftest.py в виде списка словарей
    :param state: на тесте state="EXECUTED"
    """
    assert filter_by_state(filter_processing_state_date, state="EXECUTED") == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_filter_by_state_canceled(filter_processing_state_date: List[Dict], state: str = "CANCELED") -> None:
    """
    Функция тестирует модуль processing на параметр state="CANCELED"
    :param filter_processing_state_date: Фикстура подтягивается из conftest.py в виде списка словарей
    :param state: на тесте state="CANCELED"
    """
    assert filter_by_state(filter_processing_state_date, state="CANCELED") == [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


def test_filter_by_state_empty(filter_processing_state_date: List[Dict], state: str = "") -> None:
    """
    Функция тестирует модуль processing на параметр state = рандомные значения
    :param filter_processing_state_date: Фикстура подтягивается из conftest.py в виде списка словарей
    :param state: на тесте state = любые некорректные значения, как пустая строка или набор символов
    """
    assert filter_by_state(filter_processing_state_date, state="") == "Некорректная операция!"


def test_filter_by_date_true(filter_processing_state_date: List[Dict], reverse: bool = True) -> None:
    """
    Функция проверяет сортировку по умолчанию по убыванию (reverse=True)
    :param filter_processing_state_date: Фикстура подтягивается из conftest.py в виде списка словарей
    :param reverse: reverse=True
    """
    assert sort_by_date(filter_processing_state_date, reverse=True) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_filter_by_date_false(filter_processing_state_date: List[Dict], reverse: bool = True) -> None:
    """
    Функция проверяет сортировку по умолчанию по убыванию (reverse=False)
    :param filter_processing_state_date: Фикстура подтягивается из conftest.py в виде списка словарей
    :param reverse: reverse=False
    """
    assert sort_by_date(filter_processing_state_date, reverse=False) == [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]


def test_filter_by_date_empty(filter_processing_date_empty: List[Dict], reverse: bool = True) -> None:
    """
    Функция проверяет корректность введенных данных даты
    :param filter_processing_date_empty: Фикстура подтягивается из conftest.py в виде списка словарей
    :param reverse: reverse=False что не имеет значения,
    если есть некорректные даты Try/except выведут ошибку
    """
    assert sort_by_date(filter_processing_date_empty, reverse=False) == "Некорректная дата!"
