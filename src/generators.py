from typing import Dict, Iterator, List


def filter_by_currency(list_transactions: List[Dict], currency_code: str) -> Iterator[Dict]:
    """Функция, которая принимает на вход список словарей, представляющих транзакции возвращает итератор,
    который поочередно выдает транзакции, где валюта операции соответствует заданной."""
    for transaction in list_transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency_code:
            yield transaction


def transaction_descriptions(card_transactions: List[Dict]) -> Iterator[None]:
    """Генератор, который принимает список словарей с транзакциями
    и возвращает описание каждой операции по очереди."""
    for transaction in card_transactions:
        if transaction["description"]:
            x = transaction.get("description")
            yield x


def card_number_generator(start: str, stop: str) -> Iterator[str]:
    """Генератор номеров банковских карт в формате XXXX XXXX XXXX XXXX.
    Принимает начальное и конечное значения диапазона в текстовом формате."""

    # Преобразование номера в целые числа для работы с диапазоном
    start_num = int(start.replace(" ", ""))
    stop_num = int(stop.replace(" ", ""))

    for number in range(start_num, stop_num + 1):
        # Форматирование номера в 16-значный номер с ведущими нулями
        formatted_number = f"{number:016d}"
        yield f"{formatted_number[:4]} {formatted_number[4:8]} {formatted_number[8:12]} {formatted_number[12:16]}"
