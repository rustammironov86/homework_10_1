from typing import Union


def get_mask_card_number(card_number: Union[str]) -> Union[str]:
    """

    :param card_number: Функция маскирует полученый номер карты
    """
    len_card_number = 16
    if len(card_number) == len_card_number and card_number.isdigit():
        return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    else:
        return "Введен некорректный номер карты"


def get_mask_account(account_number: Union[str]) -> Union[str]:
    """

    :param account_number: Функция маскирует полученый номер счета
    """
    len_account_number = 20
    if len(account_number) == len_account_number and account_number.isdigit():
        return f"**{account_number[-4:]}"
    else:
        return "Введен некорректный номер счета"


if __name__ == "__main__":
    card_number = str(input("Введите номер карты:"))
    account_number = str(input("Введите номер счета:"))
    """Получаем номер карты и счета"""

    print(get_mask_card_number(card_number))
    print(get_mask_account(account_number))
