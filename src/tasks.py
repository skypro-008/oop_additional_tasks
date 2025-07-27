from datetime import datetime

from src.base_task import BaseTask
from src.print_mixin import PrintMixin


class Task(BaseTask, PrintMixin):
    name: str
    description: str
    status: str
    created_at: str
    run_time: int

    def __init__(self, name, description, status="Ожидает старта", created_at=None, run_time=0):
        self.name = name
        self.description = description
        self.status = status
        self.__created_at = created_at if created_at else datetime.today().strftime("%d.%m.%Y")
        if run_time >= 0:
            self.run_time = run_time
        else:
            raise ValueError("Задачу с отрицательным временем выполнения создать нельзя")
        self.run_time = run_time
        super().__init__()

    def __str__(self):
        return f"{self.name}, Статус выполнения: {self.status}, Дата создания: {self.created_at}"

    def __add__(self, other):
        if type(other) is Task:
            return self.run_time + other.run_time
        raise TypeError

    @classmethod
    def new_task(cls, name, description, status="Ожидает старта", created_at=None, run_time=0):
        return cls(name, description, status, created_at, run_time)

    @property
    def created_at(self):
        return self.__created_at

    @created_at.setter
    def created_at(self, new_date: str):
        if datetime.strptime(new_date, "%d.%m.%Y").date() < datetime.now().date():
            print("Нельзя изменить дату создания на дату из прошлого")
            return
        self.__created_at = new_date

if __name__ == "__main__":
    task1 = Task("Cдать домашку", "Cдать домашку по ООП", run_time=60)

    print(task1.name)
    print(task1.description)
    print(task1.status)
    print(task1.created_at)

    task2 = Task("Купить билеты", "Купить билеты на самолет", run_time=30)

    print(task2.name)
    print(task2.description)
    print(task2.status)
    print(task2.created_at)

    task2.created_at = "10.07.2025"
    print(task2.created_at)
    task2.created_at = "10.08.2025"
    print(task2.created_at)

    print(task1 + task2)
    # print(task1 + 3)
