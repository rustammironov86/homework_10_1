from typing import Union
import logging
from config import BASE_DIR


logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(BASE_DIR + "/logs/masks.log", encoding="utf-8", mode="w")
file_formatter = logging.Formatter("%(asctime)s (%(filename)s).%(funcName)s %(levelname)s %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: Union[str]) -> Union[str]:
    """
    Функция маскирует полученный номер карты
    :param card_number: Получаем номер карты в виде числа
    :return: Возвращает замаскированный номер карты в виде маски
    """
    len_card_number = 16
    if len(card_number) == len_card_number and card_number.isdigit():
        logger.debug("Функция маскирует полученный номер карты")
        return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    else:
        logger.error("Введен некорректный номер карты")
        return "Введен некорректный номер карты"


def get_mask_account(account_number: Union[str]) -> Union[str]:
    """
    Функция маскирует полученный номер счета
    :param account_number: Получаем номер счета в виде числа
    :return: Возвращает замаскированный номер счета в виде маски
    """
    len_account_number = 20
    if len(account_number) == len_account_number and account_number.isdigit():
        logger.debug("Функция маскирует полученный номер счета")
        return f"**{account_number[-4:]}"
    else:
        logger.error("Введен некорректный номер счета")
        return "Введен некорректный номер счета"
