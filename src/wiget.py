from datetime import datetime
from typing import Union

from masks import get_mask_account, get_mask_card_number


def mask_account_card(payment_details: Union[str]) -> Union[str]:
    """
    Функция обрабатывать информацию как о картах, так и о счетах
    :param payment_details: Полученые реквизиты карты или счета
    :return: Функция возвращает строку с наименованием и замаскированным номером
    """
    if len(payment_details) == 25:
        return f"{payment_details[:-20]}{get_mask_account(payment_details[-20:])}"
    else:
        return f"{payment_details[:-16]}{get_mask_card_number(payment_details[-16:])}"


def get_date(date_time_info: Union[str]) -> Union[str]:
    """
    Функция время и дату в формате ISO 8601,
    возвращает в формате "ДД.ММ.ГГГГ"

    """
    try:
        date_info = datetime.fromisoformat(date_time_info)
        return date_info.strftime("%d.%m.%Y")
    except ValueError:
        return "Некорректная дата!"


if __name__ == "__main__":
    payment_details = str(input("Введите платежные реквизиты:"))
    """Получаем платежные реквизиты карты или счета"""
    date_time_info = str(input("Введите дату и время в формате ISO 8601:"))
    """Получаем строку с датой и временем в формате ISO 8601"""

    print(mask_account_card(payment_details))
    print(get_date(date_time_info))
