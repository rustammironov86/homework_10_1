import json
import os


def correct_json_file(json_file):
    """Функция проверяет наличие файла с транзакциями и возвращает их"""
    try:
        with open(json_file, encoding="utf-8") as file:
            file_json = json.load(file)
            return file_json
    except FileNotFoundError:
        print("Файл не найден")
        return []
    except json.JSONDecodeError:
        print("Ошибка декодирования JSON")
        return []
    except Exception as e:
        print(f"Произошла ошибка: {e}")


script_dir = os.path.dirname(os.path.abspath(__file__))
path_json_file = os.path.join(script_dir, "../data/operations.json")
print(correct_json_file(path_json_file))
