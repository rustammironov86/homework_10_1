from datetime import datetime
from typing import Any, Dict, List


def filter_by_state(data_operation: List[Dict], state: str = "EXECUTED") -> List[Dict[str, Any]] | str:
    """
    Функция фильтрует выполненные и отмененные банковские операции
    :param data_operation: Получает список словарей с данными операций
    :param state: Получает вид операции в виде строки
    :return: Возвращает новый список словарей содержащий значение state
    """
    if any(data_state.get("state") == state for data_state in data_operation):
        return list(filter(lambda x: str(x["state"]) == state, data_operation))
    return "Некорректная операция!"


def sort_by_date(date_list: List[Dict[str, Any]], reverse: bool = True) -> List[Dict[str, Any]] | str:
    """
    Функция сортирует банковские операции по дате
    :param date_list: Получает список словарей с данными операций
    :param reverse: Задает порядок сортировки (по умолчанию — убывание)
    :return: Возвращает новый список, отсортированный по дате date
    """
    try:
        return sorted(date_list, key=lambda x: datetime.strptime(x["date"], "%Y-%m-%dT%H:%M:%S.%f"), reverse=reverse)
    except ValueError:
        return "Некорректная дата!"
