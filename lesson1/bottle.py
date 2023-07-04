"""
Создай класс Bottle (бутылка) c полями

- Цвет (color) - строка
- Объем (volume) - число с плавающей точкой

Создай три экземпляра

- Красную 0.7
- Белую 0.3
- Черную 1,0
"""


class Bottle:

    def __init__(self, color, volume):
        self.color = str(color)
        self.volume = float(volume)


bottle_1 = Bottle("Красная", 0.7)
bottle_2 = Bottle("Белая", 0.3)
bottle_3 = Bottle("Черная", 1.0)

print(bottle_1.color, bottle_1.volume)  # Красная 0.7
print(bottle_2.color, bottle_2.volume)  # Белая 0.3
print(bottle_3.color, bottle_3.volume)  # Черная 1.0
