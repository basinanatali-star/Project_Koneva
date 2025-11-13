import json
import os
import logging

from typing import List, Dict, Any

logger = logging.getLogger('masks')
logger.setLevel(logging.INFO)

os.makedirs('logs', exist_ok=True)

file_handler = logging.FileHandler('logs/utils.log', encoding="utf-8", mode='w')
file_formatter = logging.Formatter('%(asctime)s - %(filename)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def load_transactions(file_path: str) -> List[Dict[str, Any]]:
    """Функция,которая принимает на вход путь до JSON-файла
    и возвращает список словарей с данными о финансовых транзакциях."""

    # Проверка, что JSON-файл существует
    if not os.path.exists(file_path):
        logger.error('JSON-файл не существует')
        return []

    logger.info(f'Открытие и чтение файла: {file_path}')
    # Открытие и чтение файла с удалением пробельных символов
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read().strip()

    # Проверка, что файл пустой
    if not content:
        logger.error('Файл пустой')
        return []

    # Преобразование JSON-строки в объект Python
    data = json.loads(content)

    # Проверка, что данные являются списком
    if isinstance(data, list):
        logger.info(f'Данные являются списком: {data}')
        return data
    else:
        logger.error('Данные не являются списком')
        return []
