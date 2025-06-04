import json
import csv
import pandas as pd


import logging
from config import BASE_DIR


logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(BASE_DIR + "/logs/utils.log", encoding="utf-8", mode="w")
file_formatter = logging.Formatter("%(asctime)s (%(filename)s).%(funcName)s %(levelname)s %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def correct_json_file(json_file):
    """Функция проверяет наличие файла JSON с транзакциями и возвращает их"""
    try:
        logger.debug("Выполняется обращение к файлу с транзакциями")
        with open(json_file, encoding="utf-8") as file:
            file_json = json.load(file)
            return file_json
    except FileNotFoundError:
        logger.error("Файл не найден")
        print("Файл не найден")
        return []
    except json.JSONDecodeError:
        logger.error("Ошибка декодирования")
        print("Ошибка декодирования JSON")
        return []
    except Exception as e:
        logger.error(f"Произошла ошибка: {e}")
        print(f"Произошла ошибка: {e}")


def open_transaction_xlsx_file(transaction_xlsx):
    """Функция проверяет наличие файла XLSX с транзакциями и возвращает их"""
    try:
        df = pd.read_excel(transaction_xlsx, engine="openpyxl")
        transaction_xlsx_list_dict = df.to_dict(orient="records")
        return transaction_xlsx_list_dict
    except Exception as ex:
        return f"Код ошибки {ex}"


def open_transaction_csv_file(transaction_csv):
    """Функция проверяет наличие файла CSV с транзакциями и возвращает их"""
    try:
        with open(transaction_csv, encoding="utf-8", newline="") as csv_file:
            reader_csv = csv.DictReader(csv_file, delimiter=";")
            transaction_csv_list_dict = list(reader_csv)
            return transaction_csv_list_dict
    except Exception as ex:
        return f"Код ошибки {ex}"


# script_dir = os.path.dirname(os.path.abspath(__file__))
# path_json_file = os.path.join(script_dir, "../data/operations.json")
# print(correct_json_file(path_json_file))
#
# script_dir = os.path.dirname(os.path.abspath(__file__))
# path_xlsx_file = os.path.join(script_dir, "../data/transactions_excel.xlsx")
# print(open_transaction_xlsx_file(path_xlsx_file))
#
#
# script_dir = os.path.dirname(os.path.abspath(__file__))
# path_csv_file = os.path.join(script_dir, "../data/transactions.csv")
# print(open_transaction_csv_file(path_csv_file))
