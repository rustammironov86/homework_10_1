import csv
import json
from unittest import mock
from unittest.mock import mock_open, patch

import pandas as pd

from src.utils import correct_json_file, open_transaction_xlsx_file, open_transaction_csv_file


@mock.patch("json.load", side_effect=json.JSONDecodeError("Expecting value", "", 0))
def test_json_decode_error(mock_json_load):
    result = correct_json_file("error_path.json")
    assert result == []


@mock.patch("builtins.open", side_effect=FileNotFoundError)
def test_file_not_found(mock_open):
    result = correct_json_file("fake_path.json")
    assert result == []


def test_correct_json(correct_path_json):
    with open(correct_path_json, encoding="utf-8") as file:
        data = json.load(file)
    assert correct_json_file(correct_path_json) == data


def test_open_transaction_xlsx_file(correct_path_xlsx):
    df = pd.read_excel(correct_path_xlsx, engine="openpyxl")
    transaction_xlsx_list_dict = df.to_dict(orient="records")
    assert str(open_transaction_xlsx_file(correct_path_xlsx)) == str(transaction_xlsx_list_dict)


def test_open_transaction_csv_file(correct_path_csv):
    with open(correct_path_csv, encoding="utf-8", newline="") as csv_file:
        reader_csv = csv.DictReader(csv_file, delimiter=";")
        transaction_csv_list_dict = list(reader_csv)
    assert open_transaction_csv_file(correct_path_csv) == transaction_csv_list_dict


@patch("os.path.isfile", return_value=True)
@patch("builtins.open", new_callable=mock_open, read_data="{'key': 'value')")
def test_correct_json_file(mock_open, mock_isfile):
    file = "test_file.json"
    result = correct_json_file(file)
    assert result == []
