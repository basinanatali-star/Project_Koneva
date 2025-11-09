import json
import os
import tempfile
import pytest

from src.utils import load_transactions


def test_load_transactions() -> None:

    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        temp_file = f.name
    try:
        result = load_transactions(temp_file)
        assert result == []
        assert isinstance(result, list)
    finally:
        os.unlink(temp_file)


    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        test_data: list = []
        json.dump(test_data, f)
        temp_file = f.name
    try:
        result = load_transactions(temp_file)
        assert result == []
        assert isinstance(result, list)
    finally:
        os.unlink(temp_file)

    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        test_data = [
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "operationAmount": {
                        "amount": "9824.07",
                        "currency": {
                            "name": "USD",
                            "code": "USD"
                        }
                    },
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702"
                },
                {
                    "id": 587085106,
                    "state": "EXECUTED",
                    "date": "2018-03-23T10:45:06.972075",
                    "operationAmount": {
                        "amount": "48223.05",
                        "currency": {
                            "name": "руб.",
                            "code": "RUB"
                        }
                    },
                    "description": "Открытие вклада",
                    "to": "Счет 41421565395219882431"
                }
            ]
        json.dump(test_data, f)
        temp_file = f.name
    try:
        result = load_transactions(temp_file)
        assert result == test_data
    finally:
            os.unlink(temp_file)
