import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


def test_filter_by_currency(transactions_generator_test: list) -> None:
    """
    Функция test_filter_by_currency проверяет работу с указанной валютой
    и несоответствующей валютой или ее отсутствия
    :param transactions_generator_test: фикстура подтягивается из conftest.py
    """
    result = list(filter_by_currency(transactions_generator_test, "USD"))
    expected = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        "Указанная валюта отсутствует",
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        "Указанная валюта отсутствует",
    ]
    assert result == expected

    def test_empty_list_by_currency(transactions_generator_test_empty: list) -> None:
        """
        Функция test_empty_list_by_currency проверяет работу с пустым списком транзакций
        :param transactions_generator_test_empty: фикстура подтягивается из conftest.py
        """
        result = list(filter_by_currency(transactions_generator_test_empty, "USD"))
        assert result == ["Нет транзакций"]


@pytest.mark.parametrize(
    "expected_descriptions",
    [
        [
            "Перевод организации",
            "Перевод со счета на счет",
            "Перевод со счета на счет",
            "Перевод с карты на карту",
            "Описание операции не найдено",
        ],
    ],
)
def test_transaction_descriptions(transactions_generator_test: list, expected_descriptions: list) -> None:
    """
    Функция test_transaction_descriptions проверяет корректность
    вывода описания каждой операции по очереди также и отсутствие описания
    :param transactions_generator_test: фикстура подтягивается из conftest.py
    :param expected_descriptions: использует параметризацию в качестве сравнения
    """
    result = list(transaction_descriptions(transactions_generator_test))
    assert result == expected_descriptions


def test_empty_transaction_descriptions(transactions_generator_test_empty: list) -> None:
    """
    Функция test_empty_transaction_descriptions проверяет работу с пустым списком транзакций
    :param transactions_generator_test_empty: фикстура подтягивается из conftest.py
    """
    result = list(transaction_descriptions(transactions_generator_test_empty))
    assert result == ["Нет транзакций"]


@pytest.mark.parametrize(
    "start, end, first_number, end_number",
    {
        (1, 4, "0000 0000 0000 0001", "0000 0000 0000 0004"),
        (15, 30, "0000 0000 0000 0015", "0000 0000 0000 0030"),
        (5956132884514579, 5956132884514589, "5956 1328 8451 4579", "5956 1328 8451 4589"),
    },
)
def test_card_number(start: int, end: int, first_number: str, end_number: str) -> None:
    """
    Функция test_card_number, проверяет корректность форматирования номеров карт
    в формате XXXX XXXX XXXX XXXX
    :param start: начало диапазона
    :param end: конец диапазона
    :param first_number: первая карта в диапазоне
    :param end_number: последняя карта в диапазоне
    """
    result = list(card_number_generator(start, end))
    assert result[0] == first_number
    assert result[-1] == end_number
    assert len(result) == end - start + 1
