import pytest

from calc import add

def test_add_empty_string():
    assert add("") == 0

def test_add_single_number():
    assert add("1") == 1

def test_add_two_numbers():
    assert add("1,2") == 3

def test_add_multiple_numbers():
    assert add("1,2,3") == 6

def test_add_newline_between_numbers():
    assert add("1\n2,3") == 6

def test_add_invalid_newline():
    with pytest.raises(NotImplementedError):
        add("1,\n")

def test_delimeter():
    assert add("//;\n1;2") == 3

def test_empty_delimeter():
    assert add("//\n1;2") == 3

def test_newline_delimeter():
    assert add("//\n\n1;2") == 3