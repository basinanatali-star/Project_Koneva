def get_mask_card_number(card_number: int) -> str:
    """Функция, которая маскирует номер банковской карты"""

    # Преобразование числа в строку
    card_number_str = str(card_number)

    # Проверка номера банковской карты на корректность ее длины
    if len(card_number_str) != 16:
        raise ValueError("Проверьте правильность ввода номера карты. Он должен содержать 16 цифр!")

    # Формирование маски номера банковской карты в формате ХХХХ ХХ** **** ХХХХ, Где Х - это цифра номера.
    mask_card = card_number_str[:4] + " " + card_number_str[4:6] + "**" + " " + "****" + " " + card_number_str[-4:]
    return mask_card


def get_mask_account(account_number: int) -> str:
    """Функция, которая маскирует номер банковского счета"""

    # Преобразование числа в строку
    account_number_str = str(account_number)

    # Проверка номера банковского счета на корректность его длины
    if len(account_number_str) != 20:
        raise ValueError("Проверьте правильность ввода номера счета. Он должен содержать 20 цифр!")

    # Формирование маски номера банковского счета в формате **ХХХХ, Где Х - это цифра номера.
    mask_account = "**" + account_number_str[-4:]
    return mask_account
