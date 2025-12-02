from src.utils import load_transactions
from src.transactions import transactions_csv, transactions_xlsx
from src.processing import filter_by_state, sort_by_date
from src.regular_expressions import process_bank_search
from src.widget import get_date, mask_account_card


# вывод описания
print("""Привет! Добро пожаловать в программу работы с банковскими транзакциями. Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла\n2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла\n""")

# Получаем значение о номере пункта от пользователя
user_number = input("Пользователь: ")
number = int(user_number)
if number == 1:
    print("Для обработки выбран JSON-файл\n")
    result = load_transactions("data/operations.json")
elif number == 2:
    result = transactions_csv("data/transactions.csv")
    print("Для обработки выбран CSV-файл\n")
elif number == 3:
    result = transactions_xlsx("data/transactions_excel.xlsx")
    print("Для обработки выбран XLSX-файл\n")
else:
    print("Введите верный номер пункта\n")

print("Введите статус, по которому необходимо выполнить фильтрацию."
      "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")

# Получаем значение о статусе фильтрации от пользователя
user_status = input("Пользователь: ")
if str(user_status) != "EXECUTED" or str(user_status) != "CANCELED" or str(user_status) != "PENDING":
    print(f'Статус операции "{str(user_status)}" недоступен\n'
          f'Введите статус, по которому необходимо выполнить фильтрацию.\n'
          f'Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING')
user_status = input("Пользователь: ")
if user_status.upper() == "EXECUTED":
    result_sorted = filter_by_state(result, "EXECUTED")
    print('Операции отфильтрованы по статусу "EXECUTED"')
    print(result_sorted)
elif user_status.upper() == "CANCELED":
    result_sorted = filter_by_state(result, "CANCELED")
    print('Операции отфильтрованы по статусу "CANCELED"')
    print(result_sorted)
elif user_status.upper() == "PENDING":
    result_sorted = filter_by_state(result, "PENDING")
    print('Операции отфильтрованы по статусу "PENDING"')
    print(result_sorted)

# Получаем значение о статусе сортировки по дате от пользователя
print("Отсортировать операции по дате? Да/Нет")
user_sorted_data = input("Пользователь: ")
if user_sorted_data.lower() == "нет":
    result_sorted_data = result_sorted
    print(result_sorted_data)
else:
    # Получаем значение о статусе сортировки по возрастанию или по убыванию от пользователя
    print("Отсортировать по возрастанию или по убыванию?")
    user_sorted_descending = input("Пользователь: ")
    if user_sorted_data.lower() == "да" and user_sorted_descending.lower() == "по убыванию":
        result_sorted_data = sort_by_date(result_sorted, True)
        print(result_sorted_data)
    elif user_sorted_data.lower() == "да" and user_sorted_descending.lower() == "по возрастанию":
        result_sorted_data = sort_by_date(result_sorted, False)
        print(result_sorted_data)

# Получаем значение о выводе только рублевых значений от пользователя
print("Выводить только рублевые транзакции? Да/Нет")
user_transaction = input("Пользователь: ").lower()
if user_transaction == "да" and (number == 3 or number == 2):
    result_transaction = [op for op in result_sorted_data if op["currency_code"] == "RUB"]
elif user_transaction == "да" and number == 1:
    result_transaction = [op for op in result_sorted_data if op["operationAmount"]["currency"].get("code") == "RUB"]
else:
    result_transaction = result_sorted_data
print(result_transaction)

# Получаем значения о статусе фильтрации по определенному слову от пользователя и о количестве банковских операций
print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
user_filter = input("Пользователь: ")
if user_filter.lower() == "нет":
    print("Распечатываю итоговый список транзакций...")
    total_operations = len(result_transaction)
    result_filter = result_transaction
    print(f"Всего банковских операций в выборке: {total_operations}\n")
elif user_filter.lower() == "да":
    print("Распечатываю итоговый список транзакций...")
    result_filter = process_bank_search(result_transaction, "Перевод")
    total_operations = len(result_filter)
    print(f"Всего банковских операций в выборке: {total_operations}\n")
else:
    print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")

for transaction in result_filter:
    print(f"{get_date(transaction['date'])} {transaction['description']}")

    from_account = transaction.get('from')
    if not from_account or str(from_account).lower() == 'nan':
        print(f"{mask_account_card(transaction['to'])}")
    else:
        print(f"{mask_account_card(from_account)} -> {mask_account_card(transaction['to'])}")

    operation_Amount = transaction.get('operationAmount')
    if operation_Amount:
        print(f"Сумма: {operation_Amount['amount']} "
              f"{operation_Amount['currency']['name']}\n")
    else:
        print(f"Сумма: {transaction['amount']} "
              f"{transaction['currency_code']}\n")
