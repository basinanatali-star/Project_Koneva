import pytest

from src.regular_expressions import process_bank_search, process_bank_operations


test_data = [
    {
        "id": 863064926,
        "state": "EXECUTED",
        "date": "2019-12-08T22:46:21.935582",
        "operationAmount": {"amount": "41096.24", "currency": {"name": "USD", "code": "USD"}},
        "description": "Открытие вклада",
        "to": "Счет 90424923579946435907",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
]


def test_process_bank_search() -> None:

    with pytest.raises(TypeError) as f:
        process_bank_search("not a list", "Перевод организации")
        assert str(f.value) == "data должен быть списком"
    with pytest.raises(TypeError) as f:
        process_bank_search(test_data, 123)
        assert str(f.value) == "search должен быть строкой"

        assert process_bank_search(test_data, "Перевод с карты на счет") == []
        assert process_bank_search([], "Перевод организации") == []
        assert process_bank_search(test_data, "") == []

        expected = [
            {
                "id": 594226727,
                "state": "CANCELED",
                "date": "2018-09-12T21:27:25.241689",
                "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
                "description": "Перевод организации",
                "from": "Visa Platinum 1246377376343588",
                "to": "Счет 14211924144426031657",
            }
        ]
        result = process_bank_search(test_data, "Перевод организации")
        assert result == expected


def test_process_bank_operations() -> None:
    categories = ["Перевод организации", "Перевод с карты на счет", "Открытие вклада"]
    expected = {"Перевод организации": 1, "Перевод с карты на счет": 0, "Открытие вклада": 1}
    assert process_bank_operations(test_data, categories) == expected
    assert process_bank_operations([], categories) == {
        "Перевод организации": 0,
        "Перевод с карты на счет": 0,
        "Открытие вклада": 0,
    }
    assert process_bank_operations(test_data, []) == {}
