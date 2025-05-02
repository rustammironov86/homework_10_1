from typing import Any, Dict, List


def filter_by_state(data_operation: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """
    Функция фильтрует выполненные и отмененные банковские операции
    :param data_operation: Получает список словарей с данными операций
    :param state: Получает вид операции в виде строки
    :return: Возвращает новый список словарей содержащий значение state
    """
    return list(filter(lambda x: str(x["state"]) == state, data_operation))


def sort_by_date(date_list: List[Dict[str, Any]], reverse: bool = True) -> List[Dict[str, Any]]:
    """
    Функция сортирует банковские операции по дате
    :param date_list: Получает список словарей с данными операций
    :param reverse: Задает порядок сортировки (по умолчанию — убывание)
    :return: Возвращает новый список, отсортированный по дате date
    """
    return sorted(date_list, key=lambda x: str(x.get("date")), reverse=reverse)


if __name__ == "__main__":
    data_operation = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    date_list = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    print(filter_by_state(data_operation, state="EXECUTED"))
    print(sort_by_date(date_list, reverse=True))
