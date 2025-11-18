import os

from unittest.mock import Mock, patch
from src.transactions import transactions_csv, transactions_xlsx


@patch("builtins.open", side_effect=FileNotFoundError)
def test_transactions_csv_file_not_found(mock_file: str) -> None:
    result = transactions_csv("missing.csv")
    assert result == []


@patch("builtins.open", new_callable=Mock, read_data="invalid data")
def test_transactions_csv_read_error(mock_file: str) -> None:
    with patch("csv.DictReader", side_effect=Exception("Ошибка при чтении файла")):
        result = transactions_csv("dummy.csv")
        assert result == []


def test_transactions_csv_ordered_keys() -> None:
    project_root = os.path.dirname(os.path.dirname(__file__))
    csv_file_path = os.path.join(project_root, "data", "transactions.csv")
    result = transactions_csv(csv_file_path)

    assert isinstance(result, list)

    expected_keys = {"id", "state", "date", "amount", "currency_name", "currency_code", "from", "to", "description"}

    for i, transaction in enumerate(result):
        assert isinstance(transaction, dict), f"Транзакция {i} должна быть словарем"

    missing_keys = expected_keys - set(transaction.keys())
    assert not missing_keys, f"В транзакции {i} отсутствуют ключи: {missing_keys}"


@patch("pandas.read_excel", side_effect=FileNotFoundError)
def test_transactions_xlsx_file_not_found(mock_read_excel: str) -> None:
    result = transactions_xlsx("missing.csv")
    assert result == []


@patch("pandas.read_excel", side_effect=Exception("Ошибка при чтении файла"))
def test_transactions_xlsx_read_error(mock_read_excel: str) -> None:
    result = transactions_xlsx("dummy.csv")
    assert result == []


def test_transactions_xlsx_ordered_keys() -> None:
    project_root = os.path.dirname(os.path.dirname(__file__))
    xlsx_file_path = os.path.join(project_root, "data", "transactions_excel.xlsx")
    result = transactions_xlsx(xlsx_file_path)

    assert isinstance(result, list)

    expected_keys = {"id", "state", "date", "amount", "currency_name", "currency_code", "from", "to", "description"}

    for i, transaction in enumerate(result):
        assert isinstance(transaction, dict), f"Транзакция {i} должна быть словарем"

    missing_keys = expected_keys - set(transaction.keys())
    assert not missing_keys, f"В транзакции {i} отсутствуют ключи: {missing_keys}"
