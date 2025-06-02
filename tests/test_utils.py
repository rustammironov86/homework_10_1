import json
from unittest import mock
from unittest.mock import mock_open, patch

from src.utils import correct_json_file


@mock.patch("json.load", side_effect=json.JSONDecodeError("Expecting value", "", 0))
def test_json_decode_error(mock_json_load):
    result = correct_json_file("error_path.json")
    assert result == []


@mock.patch("builtins.open", side_effect=FileNotFoundError)
def test_file_not_found(mock_open):
    result = correct_json_file("fake_path.json")
    assert result == []


def test_correct_json(correct_path):
    with open(correct_path, encoding="utf-8") as file:
        data = json.load(file)
    assert correct_json_file(correct_path) == data


@patch("os.path.isfile", return_value=True)
@patch("builtins.open", new_callable=mock_open, read_data="{'key': 'value')")
def test_correct_json_file(mock_open, mock_isfile):
    file = "test_file.json"
    result = correct_json_file(file)
    assert result == []
