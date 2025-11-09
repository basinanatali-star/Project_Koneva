import json
import os

from typing import List, Dict, Any


def load_transactions(file_path: str) -> List[Dict[str, Any]]:
    """Функция,которая принимает на вход путь до JSON-файла
    и возвращает список словарей с данными о финансовых транзакциях."""

    # Проверка, что JSON-файл существует
    if not os.path.exists(file_path):
        return []

    # Открытие и чтение файла с удалением пробельных символов
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read().strip()

    # Проверка, что файл пустой
    if not content:
        return []

    # Преобразование JSON-строки в объект Python
    data = json.loads(content)

    # Проверка, что данные являются списком
    if isinstance(data, list):
        return data
    else:
        return []
