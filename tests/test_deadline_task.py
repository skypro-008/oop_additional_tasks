from datetime import datetime

import pytest


def test_deadline_task_init(task_deadline_1):
    assert task_deadline_1.name == "Купить учебник"
    assert task_deadline_1.description == "Купить учебник по программированию"
    assert task_deadline_1.deadline == "30.07.2025"
    assert task_deadline_1.status == "Ожидает старта"
    assert task_deadline_1.created_at == datetime.now().strftime("%d.%m.%Y")
    assert task_deadline_1.run_time == 60


def test_deadline_task_add(task_deadline_1, task_deadline_2):
    assert task_deadline_1 + task_deadline_2 == 180


def test_deadline_task_add_error(task_deadline_1):
    with pytest.raises(TypeError):
        _ = task_deadline_1 + 1
