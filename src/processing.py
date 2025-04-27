from typing import List, Dict


def filter_by_state(data_operation: list[dict[str, any]], state='EXECUTED') -> list[dict[str, any]]:
    return list(filter(lambda x: str(x['state']) == state, data_operation))


def sort_by_date(date_list: list[dict[str, any]], ascending=True) -> list[dict[str, any]]:
    return sorted(date_list, key=lambda x: str(x.get('date')), reverse=ascending)


if __name__ == "__main__":
    data_operation = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                      {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                      {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                      {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
    date_list = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                 {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                 {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                 {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]
    print(filter_by_state(data_operation, state='EXECUTED'))
    print(sort_by_date(date_list, ascending=True))
