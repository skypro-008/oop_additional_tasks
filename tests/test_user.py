import pytest

from src.tasks import Task


def test_user_init(first_user, second_user):
    assert first_user.username == "user"
    assert first_user.email == "user@mail.ru"
    assert len(first_user.task_in_list) == 2

    assert first_user.users_count == 2
    assert second_user.users_count == 2

    assert first_user.all_tasks_count == 4
    assert second_user.all_tasks_count == 4


def test_user_task_list_property(first_user):
    assert first_user.task_list == ("Cдать домашку, Статус выполнения: Ожидает старта, Дата создания: 15.07.2025\n"
                                    "Cдать домашку, Статус выполнения: Ожидает старта, Дата создания: 15.07.2025\n")


def test_user_task_list_setter(first_user, task):
    assert len(first_user.task_in_list) == 2
    first_user.task_list = task
    assert len(first_user.task_in_list) == 3


def test_user_task_list_setter_error(first_user, task):
    with pytest.raises(TypeError):
        first_user.task_list = 1


def test_user_task_list_setter_periodic_task(first_user, task_periodic_1):
    first_user.task_list = task_periodic_1
    assert first_user.task_in_list[-1].description == "Купить книгу по кулинарии"


def test_user_str(first_user):
    assert str(first_user) == "Userov User, Email: user@mail.ru, Всего задач в списке: 2"


def test_middle_runtime(first_user, user_without_tasks):
    assert first_user.middle_task_runtime() == 45
    assert user_without_tasks.middle_task_runtime() == 0

def test_custom_exception(capsys, first_user):
    assert len(first_user.task_in_list) == 2

    task_add = Task("Cдать домашку", "Cдать домашку 15.1 по ООП", created_at="20.06.2025")
    first_user.task_list = task_add
    message = capsys.readouterr()
    assert message.out.strip().split("\n")[-2] == "Нельзя задать задачу с нулевым временем выполнения"
    assert message.out.strip().split("\n")[-1] == "Обработка добавления задачи завершена"

    task_add = Task("Cдать домашку", "Cдать домашку 15.1 по ООП", created_at="20.06.2025", run_time= 20)
    first_user.task_list = task_add
    message = capsys.readouterr()
    assert message.out.strip().split("\n")[-2] == "Задача добавлена успешно"
    assert message.out.strip().split("\n")[-1] == "Обработка добавления задачи завершена"


def test_task_iteration(task_iterator):
    iter(task_iterator)
    assert task_iterator.index == 0
    assert next(task_iterator).description == "Cдать домашку 15.1 по ООП"
    assert next(task_iterator).description == "Cдать домашку 15.2 по ООП"

    with pytest.raises(StopIteration):
        next(task_iterator)
