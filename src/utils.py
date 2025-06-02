import json
import os
import logging
from config import BASE_DIR


logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(BASE_DIR + "/logs/utils.log", encoding="utf-8", mode="w")
file_formatter = logging.Formatter("%(asctime)s (%(filename)s).%(funcName)s %(levelname)s %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def correct_json_file(json_file):
    """Функция проверяет наличие файла с транзакциями и возвращает их"""
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


script_dir = os.path.dirname(os.path.abspath(__file__))
path_json_file = os.path.join(script_dir, "../data/operations.json")
print(correct_json_file(path_json_file))
