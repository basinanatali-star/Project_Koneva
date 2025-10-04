import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number() -> None:
    assert get_mask_card_number('1234567890123456') == "1234 56** **** 3456"
    assert get_mask_card_number('1234567890987654') == "1234 56** **** 7654"
    with pytest.raises(ValueError) as err:
        get_mask_card_number('1234567890')
        assert str(err.value) == "Проверьте правильность ввода номера карты. Он должен содержать 16 цифр!"
    with pytest.raises(ValueError) as err:
        get_mask_card_number('123456789012345678')
        assert str(err.value) == "Проверьте правильность ввода номера карты. Он должен содержать 16 цифр!"
        with pytest.raises(ValueError) as err:
            get_mask_card_number('')
            assert str(err.value) == "Проверьте правильность ввода номера карты. Он должен содержать 16 цифр!"


def test_get_mask_account() -> None:
    assert get_mask_account('12345678901234567890') == "**7890"
    assert get_mask_account('15975385265435795145') == "**5145"
    with pytest.raises(ValueError) as err:
        get_mask_account('1234567890')
        assert str(err.value) == "Проверьте правильность ввода номера счета. Он должен содержать 20 цифр!"
    with pytest.raises(ValueError) as err:
        get_mask_account('1234567890123456789078')
        assert str(err.value) == "Проверьте правильность ввода номера счета. Он должен содержать 20 цифр!"
