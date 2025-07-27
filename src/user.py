from src.exceptions import ZeroRunTimeTask
from src.tasks import Task


class User:
    username: str
    email: str
    first_name: str
    last_name: str
    task_list: list
    users_count = 0
    all_tasks_count = 0

    def __init__(self, username, email, first_name, last_name, task_list=None):
        self.username = username
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.__task_list = task_list if task_list else []
        User.users_count += 1
        User.all_tasks_count += len(task_list) if task_list else 0

    def __str__(self):
        return f"{self.last_name} {self.first_name}, Email: {self.email}, Всего задач в списке: {len(self.__task_list)}"


    @property
    def task_list(self):
        task_str = ""
        for task in self.__task_list:
            task_str += f"{str(task)}\n"
        return task_str

    @task_list.setter
    def task_list(self, task: Task):
        if isinstance(task, Task):
            try:
                if task.run_time == 0:
                    raise ZeroRunTimeTask("Нельзя задать задачу с нулевым временем выполнения")
            except ZeroRunTimeTask as e:
                print(str(e))
            else:
                self.__task_list.append(task)
                User.all_tasks_count += 1
                print("Задача добавлена успешно")
            finally:
                print("Обработка добавления задачи завершена")
        else:
            raise TypeError

    @property
    def task_in_list(self):
        return self.__task_list

    def middle_task_runtime(self):
        try:
            return sum([task.run_time for task in self.__task_list]) / len(self.__task_list)
        except ZeroDivisionError:
            return 0


if __name__ == "__main__":
    task1 = Task("Cдать домашку 1", "Cдать домашку 14.1 по ООП", run_time=40)
    task2 = Task("Cдать домашку 2", "Cдать домашку 14.2 по ООП")
    task3 = Task("Cдать домашку 3", "Cдать домашку 15.1 по ООП")
    task4 = Task("Cдать домашку 4", "Cдать домашку 15.2 по ООП")

    user1 = User("I_Ivan",
                 "I_Ivan@mail.ru",
                 "Иван",
                 "Иванов",
                 [task1, task2, task3, task4])

    print(user1.username)
    print(user1.email)
    print(user1.first_name)
    print(user1.last_name)
    print(user1.task_list)

    print(user1.users_count)
    print(User.all_tasks_count)
    print(user1.task_list)

    print(user1)

    print(user1.middle_task_runtime())

    task5 = Task("Cдать домашку 5", "Cдать домашку 16.1 по ООП", run_time=40)
    user1.task_list = task5

    print(user1)

    print(user1.middle_task_runtime())
