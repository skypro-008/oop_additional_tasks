"""
Напишите класс Car, представляющий машину, имеющий следующие свойства:

- бренд
- модель
- год выпуска

Так как данный класс используется в большом каталоге, его необходимо оптимизировать и создать класс, который использует коллекции slots

Сравните скорость работы двух классов: с коллекциями slots и без них. Для этого каждому классу напишите метод get_set_del, 
в котором происходит получение, присваивание и удаление значения.
"""


class Car:
    brand: str
    model: str
    year: int

    def __init__(self, brand: str, model: str, year: int) -> None:
        self.brand = brand
        self.model = model
        self.year = year

    def get_set_del(self) -> None:
        self.year += 1
        del self.brand
        self.brand = "Toyota"


class CarSlots:
    brand: str
    model: str
    year: int
    __slots__ = ("brand", "model", "year")

    def __init__(self, brand: str, model: str, year: int) -> None:
        self.brand = brand
        self.model = model
        self.year = year

    def get_set_del(self) -> None:
        self.year += 1
        del self.brand
        self.brand = "Toyota"


car = Car('Toyota', 'Corolla', 2022)
car_slots = Car('Toyota', 'Crown', 1990)

import timeit

t1 = timeit.timeit(car.get_set_del)
t2 = timeit.timeit(car_slots.get_set_del)
print((t1-t2)/t1*100)
print(t1)
print(t2)
