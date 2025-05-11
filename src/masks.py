from typing import Union


def get_mask_card_number(card_number: Union[str]) -> Union[str]:
    """
    Функция маскирует полученный номер карты
    :param card_number: Получаем номер карты в виде числа
    :return: Возвращает замаскированный номер карты в виде маски
    """
    len_card_number = 16
    if len(card_number) == len_card_number and card_number.isdigit():
        return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    else:
        return "Введен некорректный номер карты"


def get_mask_account(account_number: Union[str]) -> Union[str]:
    """
    Функция маскирует полученный номер счета
    :param account_number: Получаем номер счета в виде числа
    :return: Возвращает замаскированный номер счета в виде маски
    """
    len_account_number = 20
    if len(account_number) == len_account_number and account_number.isdigit():
        return f"**{account_number[-4:]}"
    else:
        return "Введен некорректный номер счета"
