import re

from collections import Counter


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """Функция, которая принимает список словарей с данными о банковских операциях и строку поиска,
    а возвращает список словарей, у которых в описании есть данная строка."""

    if not data or not search:
        return []

    if not isinstance(data, list):
        raise TypeError("data должен быть списком")

    if not isinstance(search, str):
        raise TypeError("search должен быть строкой")

    pattern = re.compile(re.escape(search), flags=re.IGNORECASE)

    # Создание пустого списка, в который будут записываться словари, у которых есть строка поиска
    new_data = []

    # Перебор словарей входящего списка
    for operation in data:
        # Проверка ключа state на соответствие указанного значения
        description = operation.get("description")
        if isinstance(description, str) and pattern.search(description):
            new_data.append(operation)
    return new_data


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """Функция, которая принимает список словарей с данными о банковских операциях и список категорий операций,
    а возвращает словарь, в котором ключи — это названия категорий,
    а значения — это количество операций в каждой категории."""

    # Перебор словарей входящего списка и создание нового списка, состоящего из названий категорий
    descriptions = [operation.get("description") for operation in data]
    # Создание словаря для подсчета элементов в списке
    counted = Counter(descriptions)
    # Возвращение словаря только с нужными категориями
    result = {category: counted.get(category, 0) for category in categories}
    return result
