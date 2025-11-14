import os
import requests

from typing import Dict, Any
from dotenv import load_dotenv


def convert_to_rub(transaction: Dict[str, Any]) -> float:
    """функцию, которая принимает на вход транзакцию и возвращает сумму транзакции (amount) в рублях,
    тип данных — float. Если транзакция была в USD или EUR, происходит обращение к внешнему API
    для получения текущего курса валют и конвертации суммы операции в рубли."""

    amount = transaction["amount"]
    currency = transaction["currency"]

    if currency == "RUB":
        return amount

    if currency not in ["USD", "EUR"]:
        raise ValueError("Неподдерживаемая валюта")

    # URL-адрес и метод запроса
    api_url = "https://api.apilayer.com/exchangerates_data/convert"

    # Загрузка переменных из .env-файла
    load_dotenv()
    headers = {"apikey": os.getenv("API_KEY")}
    # Параметры для конвертации
    params = {"amount": amount, "from": currency, "to": "RUB"}
    # Отправка GET - запроса к API
    response = requests.get(api_url, headers=headers, params=params)
    response.raise_for_status()
    data = response.json()
    # Получение результата
    if data.get("success", False):
        amount_rub = data["result"]
        return float(amount_rub)
    else:
        raise ValueError("Ошибка конвертации валюты")
