import logging
from functools import wraps
from typing import Callable


def log(filename=None) -> any:
    """
    Декоратор log может логировать работу функции и ее результат как в файл,
    так и в консоль с использованием logging

    :param filename: Определяет имя файла в который будет передавать логи
    :return: возвращает результат работы декоратора
    """
    logging.basicConfig(
        level=logging.INFO,
        filename=filename,
        filemode="a",
        format="%(asctime)s %(levelname)s %(message)s",
        encoding="utf-8",
    )

    def decorator(func: Callable) -> any:
        @wraps(func)
        def wrapper(*args, **kwargs) -> any:
            try:
                result = func(*args, **kwargs)
                if filename:
                    logging.info(f"{func.__name__} ok")
                else:
                    print(f"{func.__name__} ok")
                return result
            except Exception as e:
                if filename:
                    logging.exception(f"{func.__name__} error: {type(e).__name__} Inputs: {args}, {kwargs}")
                else:
                    print(f"{func.__name__} error: {type(e).__name__} Inputs: {args}, {kwargs}")
                # raise e

        return wrapper

    return decorator


# @log(filename='mylog.txt')
# def num(x: int|float, y: int|float) -> int|float:
#     """
#     Функция деления на ноль
#     """
#     return x / y
#
#
# print(num(3, 0))
