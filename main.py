import sys

from src.utils import load_transactions
from src.transactions import transactions_csv, transactions_xlsx
from src.processing import filter_by_state, sort_by_date
from src.regular_expressions import process_bank_search
from src.widget import get_date, mask_account_card
from src.generators import filter_by_currency


# вывод описания
print(
    """Привет! Добро пожаловать в программу работы с банковскими транзакциями. Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла\n2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла\n"""
)

# Получаем значение о номере пункта от пользователя
user_number = input("Пользователь: ")
number = int(user_number)
if number == 1:
    print("Для обработки выбран JSON-файл\n")
    result = load_transactions("data/operations.json")
elif number == 2:
    print("Для обработки выбран CSV-файл\n")
    result = transactions_csv("data/transactions.csv")
elif number == 3:
    print("Для обработки выбран XLSX-файл\n")
    result = transactions_xlsx("data/transactions_excel.xlsx")
else:
    print("Вы ввели не верный пункт меню.\n")
    sys.exit()

print(
    "\nВведите статус, по которому необходимо выполнить фильтрацию."
    "Доступные для фильтрации статусы: EXECUTED, CANCELED, PENDING"
)

# Получаем значение о статусе фильтрации от пользователя
user_status = input("Пользователь: ")
if user_status.upper() == "EXECUTED":
    result_sorted = filter_by_state(result, "EXECUTED")
    print('Операции отфильтрованы по статусу "EXECUTED"\n')
elif user_status.upper() == "CANCELED":
    result_sorted = filter_by_state(result, "CANCELED")
    print('Операции отфильтрованы по статусу "CANCELED"\n')
elif user_status.upper() == "PENDING":
    result_sorted = filter_by_state(result, "PENDING")
    print('Операции отфильтрованы по статусу "PENDING"\n')
else:
    print(f'Статус операции "{str(user_status)}" недоступен\n')
    sys.exit()

# Получаем значение о статусе сортировки по дате от пользователя
print("Отсортировать операции по дате? Да/Нет")
user_sorted_data = input("Пользователь: ")

if user_sorted_data.lower() not in ["нет", "да"]:
    print("Вы ввели не верный ответ.\n")
    sys.exit()

if user_sorted_data.lower() == "нет":
    result_sorted_data = result_sorted
else:
    # Получаем значение о статусе сортировки по возрастанию или по убыванию от пользователя
    print("Отсортировать по возрастанию или по убыванию?")
    user_sorted_descending = input("Пользователь: ")

    if user_sorted_descending.lower() not in ["по возрастанию", "по убыванию"]:
        print("Вы ввели не верный ответ.\n")
        sys.exit()

    if user_sorted_data.lower() == "да" and user_sorted_descending.lower() == "по убыванию":
        result_sorted_data = sort_by_date(result_sorted, True)
    else:
        result_sorted_data = sort_by_date(result_sorted, False)

# Получаем значение о выводе только рублевых значений от пользователя
print("Выводить только рублевые транзакции? Да/Нет")
user_transaction = input("Пользователь: ")

if user_transaction.lower() not in ["нет", "да"]:
    print("Вы ввели не верный ответ.\n")
    sys.exit()

if user_transaction.lower() == "нет":
    result_transaction = result_sorted_data
else:
    result_transaction = list(filter_by_currency(result_sorted_data, "RUB"))
    print(result_transaction)


# Получаем значения о статусе фильтрации по определенному слову от пользователя и о количестве банковских операций
print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
user_filter = input("Пользователь: ")

if user_filter.lower() not in ["нет", "да"]:
    print("Вы ввели не верный ответ.\n")
    sys.exit()

if user_filter.lower() == "да":
    keyword = input("Введите слово из описания транзакций для поиска: ")
    result_filter = process_bank_search(result_transaction, keyword.lower())
else:
    result_filter = result_transaction
print("Распечатываю итоговый список транзакций...")
total_operations = len(result_filter)
print(f"Всего банковских операций в выборке: {total_operations}\n")
if total_operations > 0:
    for transaction in result_filter:
        print(f"{get_date(transaction['date'])} {transaction['description']}")

        from_account = transaction.get("from")
        if not from_account or str(from_account).lower() == "nan":
            print(f"{mask_account_card(transaction['to'])}")
        else:
            print(f"{mask_account_card(from_account)} -> {mask_account_card(transaction['to'])}")

        operation_Amount = transaction.get("operationAmount")
        if operation_Amount:
            print(f"Сумма: {operation_Amount['amount']} " f"{operation_Amount['currency']['name']}\n")
        else:
            print(f"Сумма: {transaction['amount']} " f"{transaction['currency_code']}\n")
else:
    print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
