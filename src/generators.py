from typing import Any, Generator


def filter_by_currency(transactions_list_cur: list, currency: str) -> Generator[str | dict, None, None]:
    """
    Функция filter_by_currency принимает на вход список словарей, представляющих транзакции
    и возвращает итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной (например, USD).
    :param transactions_list_cur: список словарей, представляющих транзакции
    :param currency: валюта операций
    """
    if not transactions_list_cur:
        yield "Нет транзакций"
    for item_currency in transactions_list_cur:
        if item_currency.get("operationAmount", {}).get("currency", {}).get("code", {}) == currency:
            yield item_currency
        else:
            yield "Указанная валюта отсутствует"


transactions = [
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
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
]
usd_transactions = filter_by_currency(transactions, "USD")
for _ in range(5):
    print(next(usd_transactions))


def transaction_descriptions(transactions_list_descr: list) -> Generator[str, None, None]:
    """
    Функция transaction_descriptions принимает на вход список словарей, представляющих транзакции
    и возвращает описание каждой операции по очереди.
    :param transactions_list_descr: список словарей, представляющих транзакции
    """
    if not transactions_list_descr:
        yield "Нет транзакций"
    for item in transactions_list_descr:
        if "description" in item:
            yield str(item.get("description"))
        else:
            yield "Описание операции не найдено"


descriptions = transaction_descriptions(transactions)
for _ in range(5):
    print(next(descriptions))


def card_number_generator(start: int, stop: int) -> Generator[str, None]:
    """
    Функция использует генератор card_number_generator,
    который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX
    Генератор может сгенерировать номера карт в заданном диапазоне
    от 0000 0000 0000 0001 до 9999 9999 9999 9999.
    :param start: начало диапазона
    :param stop: конец диапазона
    """
    start_number = "0000000000000000"
    nums = (num for num in range(start, stop + 1))
    for num in nums:
        new_card_number = start_number[: -len(str(num))] + str(num)
        if len(new_card_number) == 16 and new_card_number.isdigit():
            yield f"{new_card_number[:4]} {new_card_number[4:8]} {new_card_number[8:12]} {new_card_number[12:]}"
        else:
            yield "Некорректный номер карты"


for card_number in card_number_generator(10, 12):
    print(card_number)
