import pytest

from lesson1.bottle import Bottle


@pytest.fixture()
def bottle_red():
    return Bottle('Красная', 0.7)

def test_init_r(bottle_red):
    assert bottle_red.color == 'Красная'
    assert bottle_red.volume == 0.7


@pytest.fixture()
def bottle_white():
    return Bottle('Белая', 0.3)

def test_init_w(bottle_white):
    assert bottle_white.color == 'Белая'
    assert bottle_white.volume == 0.3


@pytest.fixture()
def bottle_black():
    return Bottle('Черная', 1.0)

def test_init_b(bottle_black):
    assert bottle_black.color == 'Черная'
    assert bottle_black.volume == 1.0

