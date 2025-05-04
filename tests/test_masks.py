import pytest

from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize('string_card, expected_card', [
    ('1596837868705199', '1596 83** **** 5199'),
    ('159683786870519914', 'Введен некорректный номер карты'),
    ('15968378687051', 'Введен некорректный номер карты'),
    ('15968378687051ab', 'Введен некорректный номер карты'),

])
def test_get_mask_card_number(string_card, expected_card):
    assert get_mask_card_number(string_card) == expected_card

@pytest.mark.parametrize('string_account, expected_account', [
    ('35383033474447895560', '**5560'),
    ('35383033474447895560123', 'Введен некорректный номер счета'),
    ('35383033474447895', 'Введен некорректный номер счета'),
    ('353830334744478955ab', 'Введен некорректный номер счета'),

])
def test_get_mask_account(string_account, expected_account):
    assert get_mask_account(string_account) == expected_account