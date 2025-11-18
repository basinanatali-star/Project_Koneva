import csv
import pandas as pd

from typing import List, Dict, Any


def transactions_csv(csv_file_path: str, delimiter: str = ";") -> List[Dict[str, Any]]:
    """Функция,которая принимает в качестве аргумента путь к CSV-файлу, считывает финансовые операции из CSV-файла
    и возвращает список словарей с данными о финансовых транзакциях."""

    csv_result = []

    try:
        # Открытие и чтение CSV-файла
        with open(csv_file_path, "r", encoding="utf-8") as file:
            csv_reader = csv.DictReader(file, delimiter=delimiter)

            # Преобразование информации из CSV-файла в список словарей с данными о финансовых транзакциях
            for row in csv_reader:
                csv_result.append(dict(row))

    # Проверка о наличии CSV-файла
    except FileNotFoundError:
        print(f"Ошибка: Файл '{csv_file_path}' не найден")
        return []

    # Проверка чтения CSV-файла
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return []

    return csv_result


def transactions_xlsx(xlsx_file_path: str) -> List[Dict[Any, Any]]:
    """Функция,которая принимает в качестве аргумента путь к XLSX-файлу, считывает финансовые операции из XLSX-файла
    и возвращает список словарей с данными о финансовых транзакциях."""
    try:
        # Открытие и чтение XLSX-файла
        xlsx_reader = pd.read_excel(xlsx_file_path)

        # Преобразование информации из XLSX-файла в список словарей с данными о финансовых транзакциях
        xlsx_result = xlsx_reader.to_dict(orient="records")

    # Проверка о наличии XLSX-файла
    except FileNotFoundError:
        print(f"Ошибка: Файл '{xlsx_file_path}' не найден")
        return []

    # Проверка чтения XLSX-файла
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return []

    return xlsx_result
