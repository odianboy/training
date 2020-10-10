# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())

# TODO здесь ваш код

class Water:
    def __init__(self):
        pass

    def __str__(self):
        return "Вода"

    def __add__(self, other):
        if type(other) == Air:
            return Storm()


class Air:
    def __init__(self):
        pass

    def __str__(self):
        return "Воздух"

    def __add__(self, other):
        if type(other) == Fire:
            return Lightning()
        if type(other) == Earth:
            return Dust()


class Fire:
    def __init__(self):
        pass

    def __str__(self):
        return "Огонь"

    def __add__(self, other):
        if type(other) == Water:
            return Steam()
        if type(other) == Earth:
            return Lava()


class Earth:
    def __init__(self):
        pass

    def __str__(self):
        return "Земля"

    def __add__(self, other):
        if type(other) == Water:
            return Mud()


class Molecule:
    def __init__(self):
        pass

    def __str__(self):
        return "Молекула"

    def __add__(self, other):
        if type(other) == Atom:
            return Cosmos()


class Atom:
    def __init__(self):
        pass

    def __str__(self):
        return "Атом"


class Storm:
    def __init__(self):
        pass

    def __str__(self):
        return "Шторм"


class Steam:
    def __init__(self):
        pass

    def __str__(self):
        return "Пар"


class Mud:
    def __init__(self):
        pass

    def __str__(self):
        return "Грязь"


class Lightning:
    def __init__(self):
        pass

    def __str__(self):
        return "Молния"


class Dust:
    def __init__(self):
        pass

    def __str__(self):
        return "Песок"


class Lava:
    def __init__(self):
        pass

    def __str__(self):
        return "Лава"


class Cosmos:
    def __init__(self):
        pass

    def __str__(self):
        return "Космос"
# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.


print(Water(), "+", Air(), "=", Water() + Air())
print(Fire(), "+", Water(), "=", Fire() + Water())
print(Earth(), "+", Water(), "=", Earth() + Water())
print(Air(), "+", Fire(), "=", Air() + Fire())
print(Air(), "+", Earth(), "=", Air() + Earth())
print(Fire(), "+", Earth(), "=", Fire() + Earth())
print(Molecule(), "+", Atom(), "=", Molecule() + Atom())
