from typing import Dict, List


def filter_by_state(old_list: List[Dict[str, str]], state: str = "EXECUTED") -> List[Dict[str, str]]:
    """Функция, которая принимает список словарей и опционально значение для ключа
    state (по умолчанию 'EXECUTED') и возвращает новый список словарей, содержащий только те словари, у которых ключ
    state соответствует указанному значению."""

    # Создание пустого списка, в который будут записываться словари, у которых ключ state
    # соответствует указанному значению
    new_list = []

    # Перебор словарей входящего списка
    for item in old_list:
        # Проверка ключа state на соответствие указанного значения
        if item.get("state") == state:
            # Создание списка, в который записываются словари для которых условие выполнено
            new_list.append(item)
    # Возврат созданного списка
    return new_list


def sort_by_date(list_of_dictionaries: List[Dict[str, str]], descending: bool = True) -> List[Dict[str, str]]:
    """Функция,  которая принимает список словарей и необязательный параметр, задающий порядок сортировки
    (по умолчанию — убывание) и возвращает новый список, отсортированный по дате (date)."""

    # Возврат отсортированного списка по дате
    return sorted(list_of_dictionaries, key=lambda x: x["date"], reverse=descending)
