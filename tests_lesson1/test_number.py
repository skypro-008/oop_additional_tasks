import pytest

from lesson1.number import Number


@pytest.fixture()
def number_7():
    return Number(7)

def test_init(number_7):
    assert number_7.value == 7

def test_get(number_7):
    assert number_7.get() == 7

def test_add(number_7):
    number_7.add(3)
    assert number_7.value  == 10

def test_subtract(number_7):
    number_7.add(3)
    number_7.subtract(5)
    assert number_7.value  == 5
