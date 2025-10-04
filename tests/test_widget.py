import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "cart_number, result",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Мир 3538303347444789", "Мир 3538 30** **** 4789"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)


def test_mask_account_card(cart_number: str, result: str) -> None:
    assert mask_account_card(cart_number) == result
    with pytest.raises(ValueError) as err:
        mask_account_card('MasterCard 59994142284263')
        assert str(err.value) == ValueError(
            "Проверьте правильность ввода номера счета. Он должен содержать 16 цифр!")
    with pytest.raises(ValueError) as err:
        mask_account_card('Счет 123456789012345678')
        assert str(err.value) == ValueError(
            "Проверьте правильность ввода номера счета. Он должен содержать 20 цифр!")
    with pytest.raises(ValueError) as err:
        mask_account_card('Мир 73654108430135874305')
        assert str(err.value) == ValueError(
            "Проверьте правильность ввода номера счета. Он должен содержать 16 цифр!")
    with pytest.raises(ValueError) as err:
        mask_account_card('Счет 9876543210123456789078')
        assert str(err.value) == ValueError(
            "Проверьте правильность ввода номера счета. Он должен содержать 20 цифр!")


def test_get_date() -> None:
    assert get_date("2019-07-03T18:35:29.512364") == "03.07.2019"
    assert get_date("2025-12-27T18:35:29.512364") == "27.12.2025"
    assert get_date("2009-09-09") == "09.09.2009"
    with (pytest.raises(IndexError)) as err:
        get_date("")
        assert str(err.value) == IndexError("Error input data")
