from datetime import datetime

import pytest


def test_periodic_task_init(task_periodic_1):
    assert task_periodic_1.name == "Купить книгу"
    assert task_periodic_1.description == "Купить книгу по кулинарии"
    assert task_periodic_1.start_date == "23.07.2025"
    assert task_periodic_1.end_date == "23.07.2025"
    assert task_periodic_1.status == "Ожидает старта"
    assert task_periodic_1.created_at == datetime.now().strftime("%d.%m.%Y")
    assert task_periodic_1.run_time == 60
    assert task_periodic_1.frequency == "Ежедневная"


def test_periodic_task_add(task_periodic_1, task_periodic_2):
    assert task_periodic_1 + task_periodic_2 == 90


def test_periodic_task_add_error(task_periodic_1):
    with pytest.raises(TypeError):
        _ = task_periodic_1 + 1
