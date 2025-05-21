

from src.decorators import log


def test_log_sum() -> None:
    """
    Тест проверяет деление двух чисел
    """
    @log(filename='mylog.txt')
    def num(x: int|float, y: int|float) -> int|float:
        return x / y

    result = num(8, 4)
    assert result == 2.0


def test_log_zero() -> None:
    """
    Функция проверяет деление на ноль
    """
    @log(filename='mylog.txt')
    def num(x: int|float, y: int|float) -> int|float:
        return x / y

    result = num(8, 0)
    assert result is None


@log(filename='mylog.txt')
def multiplier_ok(x: int|float, y: int|float) -> int|float:
    """
    Функция проверяет вывод сообщения о правильной работе
    """
    return x * y


def test_log_ok_mess(capsys) -> None:
    multiplier_ok(3, 5)
    captured = capsys.readouterr()
    assert captured.out == "multiplier_ok ok\n"


@log(filename='mylog.txt')
def log_zero_divide_mess(x: int|float, y: int|float) -> int|float:
    """
    Функция проверяет вывод сообщения об ошибке с указанием параметров
    :param x:
    :param y:
    :return:
    """
    return x / y


def test_log_zero_mess(capsys) -> None:
    log_zero_divide_mess(3, 0)
    captured = capsys.readouterr()
    assert captured.out == "log_zero_divide_mess error: ZeroDivisionError Inputs: (3, 0), {}\n"
