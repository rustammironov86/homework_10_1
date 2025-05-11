from datetime import datetime
from typing import Union

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(payment_details: Union[str]) -> Union[str]:
    """
    Функция обрабатывать информацию как о картах, так и о счетах
    :param payment_details: Полученные реквизиты карты или счета в виде строки
    :return: Функция возвращает строку с наименованием и замаскированным номером
    """
    if len([num_length for num_length in payment_details if num_length.isdigit()]) == 20:
        return f"{payment_details[:-20]}{get_mask_account(payment_details[-20:])}"
    elif len([num_length for num_length in payment_details if num_length.isdigit()]) == 16:
        return f"{payment_details[:-16]}{get_mask_card_number(payment_details[-16:])}"
    else:
        return "Некорректный номер!"


def get_date(date_time_info: Union[str]) -> Union[str]:
    """
    Функция время и дату в формате ISO 8601 в виде строки,
    возвращает в формате "ДД.ММ.ГГГГ"

    """
    try:
        date_info = datetime.fromisoformat(date_time_info)
        return date_info.strftime("%d.%m.%Y")
    except ValueError:
        return "Некорректная дата!"
