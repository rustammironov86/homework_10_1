import pytest

from src.masks import get_mask_account, get_mask_card_number

"""Импортируем необходимые функции и pytest"""


@pytest.mark.parametrize(
    "string_card, expected_card",
    [
        ("1596837868705199", "1596 83** **** 5199"),
        ("159683786870519914", "Введен некорректный номер карты"),
        ("15968378687051", "Введен некорректный номер карты"),
        ("15968378687051ab", "Введен некорректный номер карты"),
    ],
)
def test_get_mask_card_number(string_card: str, expected_card: str) -> None:
    """
    Функция для тестирования работы get_mask_card_number с использованием параметризации
    :param string_card: Из кортеджа берутся варианты номера карты(корректный,
    более длинный/короткий/с символами вместо цифр)
    :param expected_card: Правильный вывод данных маски для сравнения
    """
    assert get_mask_card_number(string_card) == expected_card


@pytest.mark.parametrize(
    "string_account, expected_account",
    [
        ("35383033474447895560", "**5560"),
        ("35383033474447895560123", "Введен некорректный номер счета"),
        ("35383033474447895", "Введен некорректный номер счета"),
        ("353830334744478955ab", "Введен некорректный номер счета"),
    ],
)
def test_get_mask_account(string_account: str, expected_account: str) -> None:
    """
    Функция для тестирования работы get_mask_account с использованием параметризации
    :param string_account: Из кортеджа берутся варианты номера счета(корректный,
    более длинный/короткий/с символами вместо цифр)
    :param expected_account: Правильный вывод данных маски для сравнения
    """
    assert get_mask_account(string_account) == expected_account
