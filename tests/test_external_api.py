from unittest.mock import patch

from src.external_api import transactions_summ_currency


def test_transactions_summ_currency(transactions_usd, currency_rub):
    """Тест для функции конвертации валюты из "USD" в "RUB" """
    with patch("requests.get") as mock_request:
        mock_request.return_value.status_code = 200
        mock_request.return_value.json.return_value = {"result": 500}

        assert transactions_summ_currency(transactions_usd[0], currency_rub) == 500

    with patch("requests.get") as mock_request:
        mock_request.return_value.status_code = 500
        mock_request.return_value.json.return_value = {"result": 300}

        assert transactions_summ_currency(transactions_usd[0], currency_rub) == "Код ошибки 500"

    assert transactions_summ_currency(transactions_usd[0], None) == "Код ошибки 429"
    assert transactions_summ_currency(transactions_usd[1], None) == 0
    assert transactions_summ_currency(transactions_usd[0], "USD") == 8221.37
    assert transactions_summ_currency(transactions_usd[2], "DRE") == 0
