import pytest

from src.widget import mask_account_card, get_date


@pytest.mark.parametrize(
    "string_account_card, expected_account_card",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Visa Classic 68319824767376ab", "Некорректный номер!"),
        ("Visa Platinum 8990922113665229123", "Некорректный номер!"),
        ("Visa Gold 599941422842635", "Некорректный номер!"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Счет 35383033474447895", "Некорректный номер!"),
        ("Счет 73654108430135874305234", "Некорректный номер!"),
        ("Счет 73654108430135874ab", "Некорректный номер!"),
    ],
)
def test_mask_account_card(string_account_card: str, expected_account_card: str) -> None:
    assert mask_account_card(string_account_card) == expected_account_card


def test_get_date(right_date: str) -> None:
    assert get_date(right_date) == "11.03.2024"

    assert get_date("20243-11T02:26:18.671407") == "Некорректная дата!"
