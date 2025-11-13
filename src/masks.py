import logging
import os

logger = logging.getLogger('masks')
logger.setLevel(logging.INFO)

os.makedirs('logs', exist_ok=True)

file_handler = logging.FileHandler('logs/masks.log', encoding="utf-8", mode='w')
file_formatter = logging.Formatter('%(asctime)s - %(filename)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Функция, которая маскирует номер банковской карты"""

    logger.info(f'Запрос ввода номера карты: {card_number}')

    # Проверка номера банковской карты на корректность ее длины
    if len(card_number) != 16:
        logger.error('Некорректная длина номера карты')
        raise ValueError("Проверьте правильность ввода номера карты. Он должен содержать 16 цифр!")

    # Формирование маски номера банковской карты в формате ХХХХ ХХ** **** ХХХХ, Где Х - это цифра номера.
    mask_card = card_number[:4] + " " + card_number[4:6] + "**" + " " + "****" + " " + card_number[-4:]

    logger.info(f'Успешно сгенерирована маска карты: {mask_card}')
    return mask_card


def get_mask_account(account_number: str) -> str:
    """Функция, которая маскирует номер банковского счета"""

    logger.info(f'Запрос ввода номера счета: {account_number}')

    # Проверка номера банковского счета на корректность его длины
    if len(account_number) != 20:
        logger.error('Некорректная длина номера счета')
        raise ValueError("Проверьте правильность ввода номера счета. Он должен содержать 20 цифр!")

    # Формирование маски номера банковского счета в формате **ХХХХ, Где Х - это цифра номера.
    mask_account = "**" + account_number[-4:]

    logger.info(f'Успешно сгенерирована маска счета: {mask_account}')
    return mask_account
