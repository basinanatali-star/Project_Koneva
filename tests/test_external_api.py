import pytest
import os

from unittest.mock import Mock
from unittest.mock import patch

from src.external_api import convert_to_rub


def test_convert_to_rub() -> None:
    """Тест для транзакции в рублях (без конвертации)"""

    assert convert_to_rub({"amount": 100.0, "currency": "RUB"}) == 100
    with pytest.raises(ValueError) as err:
        convert_to_rub({"amount": 100.0, "currency": "GBP"})
        assert str(err.value) == ValueError("Неподдерживаемая валюта")


@patch("requests.get")
@patch.dict(os.environ, {"API_KEY": "test_api_key"})
def test_convert_usd_transaction_success(mock_requests_get) -> None:
    """Тест успешной конвертации USD в RUB"""
    # Мокаем ответ API
    mock_response = Mock()
    mock_response.json.return_value = {"success": True, "result": 7500.0}  # 100 USD = 7500 RUB
    mock_response.raise_for_status = Mock()
    mock_requests_get.return_value = mock_response

    result = convert_to_rub({"amount": 100.0, "currency": "USD"})

    # Проверяем результат
    assert result == 7500.0
    assert isinstance(result, float)

    mock_requests_get.assert_called_once()
    call_args = mock_requests_get.call_args

    assert call_args[0][0] == "https://api.apilayer.com/exchangerates_data/convert"
    assert call_args[1]["headers"]["apikey"] == "test_api_key"
    assert call_args[1]["params"]["amount"] == 100.0
    assert call_args[1]["params"]["from"] == "USD"
    assert call_args[1]["params"]["to"] == "RUB"
