import pytest

import calc

def test_add_empty_string():
    assert calc.add("") == 0

def test_add_single_number():
    assert calc.add("1") == 1

def test_add_two_numbers():
    assert calc.add("1,2") == 3

def test_add_multiple_numbers():
    assert calc.add("1,2,3") == 6

def test_add_newline_between_numbers():
    assert calc.add("1\n2,3") == 6

def test_add_invalid_newline_raises():
    with pytest.raises(NotImplementedError):
        calc.add("1,\n")

def test_add_negative_number_raises():
    with pytest.raises(NotImplementedError):
        calc.add("1,-2")

def test_add_delimeter():
    assert calc.add("//;\n1;2") == 3

def test_add_empty_delimeter():
    assert calc.add("//\n1;2") == 3

def test_get_number_list_negative_number_raises():
    with pytest.raises(NotImplementedError):
        calc.get_number_list("-1,1",",")

def test_get_number_list_multiple_negative_number_raises():
    with pytest.raises(NotImplementedError) as ex:
        calc.get_number_list("-1,-2",",")
        msg = ex.value
        numbers = msg.replace(calc.NEGATIVE_NUMBER_MESSAGE, '')
        assert numbers == "-1,-2"