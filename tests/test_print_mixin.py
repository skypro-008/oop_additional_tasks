from datetime import datetime


def test_print_mixin_task(capsys, task):
    message = capsys.readouterr()
    assert message.out.strip() == "Task(Cдать домашку, Cдать домашку 15.1 по ООП, Ожидает старта, 20.06.2025)"


def test_print_mixin_periodic_task(capsys, task_periodic_1):
    message = capsys.readouterr()
    assert message.out.strip() == (f"PeriodicTask(Купить книгу, Купить книгу по кулинарии, "
                                   f"Ожидает старта, {datetime.now().strftime("%d.%m.%Y")})")


def test_print_mixin_deadline_task(capsys, task_deadline_1):
    message = capsys.readouterr()
    assert (message.out.strip() == (f"DeadlineTask(Купить учебник, Купить учебник по программированию, "
                                    f"Ожидает старта, {datetime.now().strftime("%d.%m.%Y")})"))
