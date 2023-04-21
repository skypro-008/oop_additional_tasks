"""
Напишите класс Person2, представляющий человека, имеющий следующие атрибуты:

- __slots__ = ('name', 'age'): список атрибутов, доступных объекту.

Напишите класс Employee2, наследующийся от класса Person2, представляющий сотрудника, имеющий следующие атрибуты:

- __slots__ = ('salary',): список атрибутов, доступных объекту.

Напишите класс Manager2, наследующийся от класса Employee2, представляющий менеджера, имеющий следующие атрибуты:

- __slots__ = ('bonus', 'department'): список атрибутов, доступных объекту.
"""


class Person2:
    pass


person = Person2()
person.name = "John"
person.age = 30
person.salary = 5000  # raises AttributeError

employee = Employee2()
employee.name = "Jane"
employee.age = 25
employee.salary = 5000

manager = Manager2()
manager.name = "Bob"
manager.age = 40
manager.salary = 10000
manager.bonus = 5000
manager.department = "IT"
