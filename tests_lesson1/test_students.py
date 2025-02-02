import pytest

from lesson1.students import Student


@pytest.fixture()
def student_alisa():
    return Student('Алиса', 3)

def test_init_(student_alisa):
    assert student_alisa.name == 'Алиса'
    assert student_alisa.course  == 3


@pytest.fixture()
def student_margarita():
    return Student('Маргарита', 2)

def test_init(student_margarita):
    assert student_margarita.name == 'Маргарита'
    assert student_margarita.course  == 2