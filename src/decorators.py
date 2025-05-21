import logging
from functools import wraps
from typing import Callable


def log(func: Callable) -> any:
    """
    Декоратор log может логировать работу функции и ее результат как в файл,
    так и в консоль с использованием logging

    :param func: функция, которая будет использовать декоратор
    :return: возвращает результат работы декоратора
    """
    logging.basicConfig(
        level=logging.INFO,
        filename="decorators.log",
        filemode="a",
        format="%(asctime)s %(levelname)s %(message)s",
        encoding="utf-8",
    )

    @wraps(func)
    def wrapper(*args: tuple, **kwargs: dict) -> any:
        try:
            result = func(*args, **kwargs)
            logging.info(f"{func.__name__} ok")
            print(f"{func.__name__} ok")
            return result
        except Exception as e:
            logging.exception(f"{func.__name__} error: {type(e).__name__} Inputs: {args}, {kwargs}")
            print(f"{func.__name__} error: {type(e).__name__} Inputs: {args}, {kwargs}")

    return wrapper


@log
def num(x: int|float, y: int|float) -> int|float:
    """
    Функция деления на ноль
    """
    return x / y


print(num(3, 0))
