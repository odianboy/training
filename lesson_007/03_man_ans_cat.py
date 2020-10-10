# -*- coding: utf-8 -*-

from random import randint

# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.

# TODO здесь ваш код

# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)
from termcolor import cprint


# class Man:
#     def __init__(self, name):
#         self.name = name
#         self.fullness = 50
#         self.food = 50
#         self.money = 0
#
#     def __str__(self):
#         return "Я - {}, сытость {}, еды осталось {}, денег осталось {}".format(
#             self.name, self.fullness, self.food, self.money)
#
#     def eat(self):
#         if self.food >= 10:
#             cprint("{} поел".format(self.name), color="yellow")
#             self.fullness += 10
#             self.food -= 10
#         else:
#             cprint("{} нет еды".format(self.name), color="red")
#
#     def work(self):
#         cprint("{} сходил на работу".format(self.name), color="blue")
#         self.money += 50
#         self.fullness -= 10
#
#     def play_DOTA(self):
#         cprint("{} играл в доту целый день".format(self.name), color="green")
#         self.fullness -= 10
#
#     def shopping(self):
#         if self.money >= 50:
#             cprint("{} сходил в магазин за едой".format(self.name), color="magenta")
#             self.money -= 50
#             self.food += 50
#         else:
#             cprint("{} деньги кончились!".format(self.name), color="red")
#
#     def act(self):
#         if self.fullness <= 0:
#             cprint("{} умер...".format(self.name), color="red")
#             return
#
#         dice = randint(1, 6)
#         if self.fullness < 20:
#             self.eat()
#         elif self.food < 10:
#             self.shopping()
#         elif self.money < 50:
#             self.work()
#         elif dice == 1:
#             self.work()
#         elif dice == 2:
#             self.eat()
#         else:
#             self.play_DOTA()
#
#
# vasya = Man(name="Вася")
# for day in range(1, 366):
#     print("========== день {} ==========".format(day))
#     vasya.act()
#     print(vasya)


# class Man:
#     def __init__(self, name):
#         self.name = name
#         self.fullness = 50
#         self.house = None
#
#     def __str__(self):
#         return "Я - {}, сытость {}".format(
#             self.name, self.fullness)
#
#     def eat(self):
#         if self.house.food >= 10:
#             cprint("{} поел".format(self.name), color="yellow")
#             self.fullness += 10
#             self.house.food -= 10
#         else:
#             cprint("{} нет еды".format(self.name), color="red")
#
#     def work(self):
#         cprint("{} сходил на работу".format(self.name), color="blue")
#         self.house.money += 50
#         self.fullness -= 10
#
#     def watch_MTV(self):
#         cprint("{} смотрел MTV целый день".format(self.name), color="green")
#         self.fullness -= 10
#
#     def shopping(self):
#         if self.house.money >= 50:
#             cprint("{} сходил в магазин за едой".format(self.name), color="magenta")
#             self.house.money -= 50
#             self.house.food += 50
#         else:
#             cprint("{} деньги кончились!".format(self.name), color="red")
#
#     def go_into_the_house(self, house):
#         self.house = house
#         cprint("{} Вьехал в дом".format(self.name), color="cyan")
#         self.fullness -= 10
#
#     def act(self):
#         if self.fullness <= 0:
#             cprint("{} умер...".format(self.name), color="red")
#             return
#
#         dice = randint(1, 6)
#         if self.fullness < 20:
#             self.eat()
#         elif self.house.food < 10:
#             self.shopping()
#         elif self.house.money < 50:
#             self.work()
#         elif dice == 1:
#             self.work()
#         elif dice == 2:
#             self.eat()
#         else:
#             self.watch_MTV()
#
#
# class House:
#     def __init__(self):
#         self.food = 10
#         self.money = 50
#
#     def __str__(self):
#         return "В доме еды осталось {}, денег осталось {}".format(
#             self.food, self.money)
#
#
# citizens = [
#     Man(name="Бивис"),
#     Man(name="Батхед"),
#     Man(name="Кенни")
# ]
#
#
# my_sweet_house = House()
# for citizen in citizens:
#     citizen.go_into_the_house(house=my_sweet_house)
#
#
# for day in range(1, 366):
#     print("========== день {} ==========".format(day))
#     for citizen in citizens:
#         citizen.act()
#     print("========== в конце дня ========== ")
#     for citizen in citizens:
#         print(citizen)
#     print(my_sweet_house)


# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.

class Man:
    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return "Я - {}, сытость {}".format(
            self.name, self.fullness)

    def eat(self):
        if self.house.food >= 10:
            cprint("{} поел".format(self.name), color="yellow")
            self.fullness += 10
            self.house.food -= 10
        else:
            cprint("{} нет еды".format(self.name), color="red")

    def work(self):
        cprint("{} сходил на работу".format(self.name), color="blue")
        self.house.money += 150
        self.fullness -= 10

    def watch_MTV(self):
        cprint("{} смотрел MTV целый день".format(self.name), color="green")
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 50:
            cprint("{} сходил в магазин за едой".format(self.name), color="magenta")
            self.house.money -= 50
            self.house.food += 50
        else:
            cprint("{} деньги кончились!".format(self.name), color="red")

    def go_into_the_house(self, house):
        self.house = house
        cprint("{} Вьехал в дом".format(self.name), color="cyan")
        self.fullness -= 10

    def pick_up_a_cat(self, house):
        cat.house = house
        cprint("{} теперь обрёл семью и дом!".format(cat.name), color="red")
        cat.fullness += 20

    def buy_food_the_cat(self):
        if self.house.food_bowl <= 20:
            self.house.food_bowl += 50
            cprint("{} сходил в магазин за кошачьем кормом".format(self.name), color="blue")
            self.house.money -= 50
        else:
            cprint("{} нет еды".format(cat.name), color="red")

    def clean_the_house(self):
        if self.house.mud <= 10:
            self.house.mud -= 100
            cprint("{} убрал в доме за котом".format(self.name), color="blue")
            self.fullness -= 20

    def act(self):
        if self.fullness <= 0:
            cprint("{} умер...".format(self.name), color="red")
            return

        dice = randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif self.house.food < 10:
            self.shopping()
        elif self.house.money < 50:
            self.work()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.watch_MTV()


class House:
    def __init__(self):
        self.food = 10
        self.money = 50
        self.mud = 10
        self.food_bowl = 50

    def __str__(self):
        return "В доме еды осталось {}, денег осталось {}, в доме грязи {}, еда для кота {}".format(
            self.food, self.money, self.mud, self.food_bowl)


class Cat:
    def __init__(self, name):
        self.name = name
        self.fullness = 20
        self.house = None

    def __str__(self):
        return "Кот по кличке {}, сытость {}".format(self.name, self.fullness)

    def cat_eating(self):
        if self.fullness <= 10:
            self.fullness += 50
            cprint("{} покушал".format(self.name), color="red")
            self.house.food_bowl -= 10

    def cat_sleep(self):
        cprint("{} спит...".format(self.name), color="red")
        self.fullness -= 10

    def cat_tears_wallpaper(self):
        cprint("{} подрал обои".format(self.name), color="red")
        self.fullness -= 10
        self.house.mud += 5

    def act_cat(self):
        if self.fullness <= 0:
            cprint("{} умер..".format(self.name), color="red")
        choice = randint(1, 5)
        if self.fullness <= 10:
            self.cat_eating()
        if choice == 2:
            self.cat_tears_wallpaper()
        if choice == 3:
            self.cat_sleep()


cat = Cat(name="Барсик")

citizens = [
    Man(name="Бивис"),
    # Man(name="Батхед"),
    # Man(name="Кенни")
]

animals = [cat]

my_sweet_house = House()
for citizen in citizens:
    citizen.go_into_the_house(house=my_sweet_house), citizen.pick_up_a_cat(house=my_sweet_house)

for day in range(1, 21):
    print("========== день {} ==========".format(day))
    for citizen in citizens:
        citizen.act()
    for animal in animals:
        animal.act_cat()
    print("========== в конце дня ========== ")
    for citizen in citizens:
        print(citizen)
    for animal in animals:
        print(animal)
    print(my_sweet_house)


# cat = Cat(name="Барсик")
# for day in range(1, 366):
#     print("========== день {} ==========".format(day))
#     cat.act_cat()
#     print(cat)



