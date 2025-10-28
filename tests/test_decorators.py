import pytest

from src.decorators import log


def test_log():
    @log()
    def my_function(x, y):
        return x + y

    my_function(1, 2)
    assert "my_function ok"

    @log()
    def my_function(x, y):
        return x + y

    with pytest.raises(TypeError, match="my_function error:"):
        my_function(1, "2")


def test_log(capsys):
    @log()
    def my_function(x, y):
        return x + y

    my_function(1, 2)
    captured = capsys.readouterr()
    assert captured.out == "my_function ok\n"
