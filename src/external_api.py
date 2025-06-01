import os

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")


def transactions_summ_currency(operation, code):
    """
    Функция принимает на вход транзакцию и возвращает
    сумму транзакции (amount) в рублях, тип данных — float.
    Если транзакция была в USD или EUR, происходит обращение
    к внешнему API для получения текущего курса валют
    и конвертации суммы операции в рубли.
    :param operation: список словарей транзакций из файла operations.json
    :param code: указание валюты
    :return: возвращает сумму транзакции (amount) в рублях
    """
    url = "https://api.apilayer.com/exchangerates_data/convert"

    operation_amount = operation.get("operationAmount", {})
    amount_ = operation_amount.get("amount")
    operation_currency = operation_amount.get("currency", {})
    operation_code = operation_currency.get("code")

    if not amount_ or not operation_currency or not operation_code:
        return 0
    if operation_code == code:
        return float(amount_)
    if operation_code not in ("USD", "EUR"):
        return 0

    params = {"to": code, "from": operation_code, "amount": amount_}
    headers = {"apikey": API_KEY}

    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        return f"Код ошибки {response.status_code}"

    result = response.json().get("result")
    return float(result)
