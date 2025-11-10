import pytest

from src.decorators import log


def test_log():
    @log()
    def my_function(x, y):
        return x + y

    with pytest.raises(
        TypeError, match="my_function error: unsupported operand type(s) for +: 'int' and 'str'. Inputs: (1, '2'),{}"
    ):
        my_function(1, "2")

    @log()
    def my_function(x, y):
        return x / y

    with pytest.raises(ZeroDivisionError, match="my_function error: division by zero. Inputs: (1, 0),{}"):
        my_function(1, 0)


def test_log(capsys):
    @log()
    def my_function(x, y):
        return x + y

    my_function(1, 2)
    captured = capsys.readouterr()
    assert captured.out == "my_function ok\n"
