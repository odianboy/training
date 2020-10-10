# -*- coding: utf-8 -*-

from termcolor import cprint
from random import randint

######################################################## Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умрает от депресии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.


class House:
    total_food = 0

    def __init__(self):
        self.amount_money = 100
        self.amount_food = 50
        self.amount_mud = 0
        self.food_the_cat = 30

    def __str__(self):
        return "Количество денег в тумбочке {}, еды в холодильнике {}, грязи в доме {}, корм для котика {}".format(
            self.amount_money, self.amount_food, self.amount_mud, self.food_the_cat)


class Husband:
    total_earnings = 0

    def __init__(self, name):
        self.name = name
        self.fullness = 30
        self.happy = 100

    def __str__(self):
        return "Я {}, сытость {}, счастья {}".format(self.name, self.fullness, self.happy)

    def act(self):
        self.fullness -= 10
        if self.fullness == 0:
            cprint("{} умер от голода".format(self.name), color="red")
            return
        elif self.happy <= 10:
            cprint("{} умер от депресси".format(self.name), color="red")
            return
        if self.fullness <= 30:
            self.eat()
        if self.happy <= 90:
            self.gaming()
            self.pet_the_cat()
        else:
            self.work()

    def eat(self):
        self.fullness += 30
        home.amount_food -= 30
        home.amount_mud += 5
        home.total_food += 30
        cprint("{} покушал".format(self.name), color="blue")

    def work(self):
        self.fullness -= 10
        home.amount_money += 150
        serge.total_earnings += 150
        cprint("{} сходил на работу".format(self.name), color="blue")

    def gaming(self):
        self.happy += 20
        cprint("{} поиграл в WOT".format(self.name), color="blue")

    def pet_the_cat(self):
        self.happy += 5
        cprint("{} погладил котика".format(self.name), color="magenta")


class Wife(Husband):
    total_coat = 0

    def __init__(self, name):
        super().__init__(name=name)
        # self.name = name
        # self.fullness = 30
        # self.happy = 100

    def __str__(self):
        return super().__str__()
        # return "Я {}, сытость {}, счастья {}".format(self.name, self.fullness, self.happy)

    def act(self):
        self.fullness -= 10
        if self.fullness == 0:
            cprint("{} умерла от голода".format(self.name), color="red")
            return
        elif self.happy <= 10:
            cprint("{} умерла от депресси".format(self.name), color="red")
            return
        if self.fullness <= 30:
            self.eat()
        if self.happy <= 90:
            self.buy_fur_coat()
            self.pet_the_cat()
        if home.amount_mud >= 100:
            self.clean_house()
        elif home.amount_mud >= 90:
            self.happy -= 10
            serge.happy -= 10
        if home.amount_food <= 120:
            self.shopping()
        if home.food_the_cat <= 90:
            self.buy_cat_food()

    def eat(self):
        self.fullness += 30
        home.amount_food -= 30
        home.amount_mud += 5
        home.total_food += 30
        cprint("{} покушала".format(self.name), color="yellow")

    def shopping(self):
        self.fullness -= 10
        home.amount_money -= 60
        home.amount_food += 60
        cprint("{} купила продуктов".format(self.name), color="yellow")

    def buy_cat_food(self):
        home.amount_money -= 30
        home.food_the_cat += 30
        cprint("{} купила корм для котика".format(self.name), color="yellow")

    def buy_fur_coat(self):
        self.fullness -= 10
        home.amount_money -= 350
        self.happy += 60
        masha.total_coat += 1
        cprint("{} купила себе шубу".format(self.name), color="yellow")

    def clean_house(self):
        home.amount_mud -= 100
        cprint("{}, убралась в доме".format(self.name), color="yellow")
        self.fullness -= 10


class Cat:

    def __init__(self, name):
        self.name = name
        self.fullness = 30

    def __str__(self):
        return "Меня зовут {}, Сытость {}".format(self.name, self.fullness)

    def act(self):
        choice = randint(1, 3)
        self.fullness -= 10
        if self.fullness <= 0:
            cprint("{} котик умер от голода...".format(self.name), color="red")
            if home.food_the_cat >= 30:
                if self.fullness <= 30:
                    self.eat()
            if choice == 2:
                self.sleep()
            elif choice == 1:
                self.soil()

    def eat(self):
        home.food_the_cat -= 10
        self.fullness += 20
        cprint("{} покушал".format(self.name), color="green")

    def sleep(self):
        self.fullness -= 10
        cprint("{} спит...".format(self.name), color="green")

    def soil(self):
        self.fullness -= 10
        home.amount_mud += 5
        cprint("{} погрыз обои".format(self.name), color="green")


class Child(Husband):

    def __init__(self, name):
        self.fullness = 10
        self.happy = 100
        super().__init__(name=name)

    def __str__(self):
        return super().__str__()

    def act(self):
        if self.fullness == 0:
            cprint("{} умер...".format(self.name), color="red")
        if self.fullness <= 10:
            self.eat()
        else:
            self.sleep()

    def eat(self):
        home.amount_food -= 10
        self.fullness += 10
        cprint("{} покушал".format(self.name), color="blue")

    def sleep(self):
        cprint("{} спит...".format(self.name), color="blue")


home = House()
serge = Husband(name='Сережа')
masha = Wife(name='Маша')
kolya = Child(name='Коля')
# barsik = Cat(name="Барсик")

cats = [
    Cat(name="Мурзик"),
    Cat(name="Барсик"),
    Cat(name="Тимоша")

]

for day in range(365):
    cprint('================== День {} =================='.format(day), color='red')
    serge.act()
    masha.act()
    kolya.act()
    for cat in cats:
        cat.act()
    # barsik.act()
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(kolya, color='cyan')
    for cat in cats:
        cprint(cat, color="cyan")
    # cprint(barsik, color='cyan')
    cprint(home, color='cyan')

cprint("Всего было заработано денег {}, съеденно еды {}, купленно шуб {}".format(serge.total_earnings, home.total_food,
                                                                                 masha.total_coat), color="magenta")
# TODO после реализации первой части - отдать на проверку учителю

######################################################## Часть вторая
#
# После подтверждения учителем первой части надо
# отщепить ветку develop и в ней начать добавлять котов в модель семьи
#
# Кот может:
#   есть,
#   спать,
#   драть обои
#
# Люди могут:
#   гладить кота (растет степень счастья на 5 пунктов)
#
# В доме добавляется:
#   еда для кота (в начале - 30)
#
# У кота есть имя и степень сытости (в начале - 30)
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Еда для кота покупается за деньги: за 10 денег 10 еды.
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов


# class Cat:
#
#     def __init__(self, name):
#         self.name = name
#         self.fullness = 30
#
#     def __str__(self):
#         return "Меян зовут {}, Сытость {}".format(self.name, self.fullness)
#
#     def act(self):
#         self.fullness -= 10
#         choice = randint(1, 3)
#         if self.fullness == 0:
#             cprint("{} котик умер от голода...".format(self.name), color="red")
#         if self.fullness <= 10:
#             self.eat()
#         if choice == 2:
#             self.sleep()
#         elif choice == 1:
#             self.soil()
#
#     def eat(self):
#         home.food_the_cat -= 10
#         self.fullness += 20
#         cprint("{} покушал".format(self.name), color="green")
#
#     def sleep(self):
#         self.fullness -= 10
#         cprint("{} спит...".format(self.name), color="green")
#
#     def soil(self):
#         self.fullness -= 10
#         home.amount_mud += 5
#         cprint("{} погрыз обои".format(self.name), color="green")
#
#
# barsik = Cat(name="Барсик")

######################################################## Часть вторая бис
#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья  - не меняется, всегда ==100 ;)

# class Child(Husband):
#
#     def __init__(self, name):
#         self.fullness = 10
#         self.happy = 100
#         super().__init__(name=name)
#
#     def __str__(self):
#         return super().__str__()
#
#     def act(self):
#         if self.fullness == 0:
#             cprint("{} умер...".format(self.name), color="red")
#         if self.fullness <= 10:
#             self.eat()
#
#     def eat(self):
#         home.amount_food -= 10
#         self.fullness += 10
#         cprint("{} покушал".format(self.name), color="blue")
#
#     def sleep(self):
#         cprint("{} спит...".format(self.name), color="blue")


# TODO после реализации второй части - отдать на проверку учителем две ветки


######################################################## Часть третья
#
# после подтверждения учителем второй части (обоих веток)
# влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.


# home = House()
# serge = Husband(name='Сережа')
# masha = Wife(name='Маша')
# kolya = Child(name='Коля')
# murzik = Cat(name='Мурзик')
#
# for day in range(365):
#     cprint('================== День {} =================='.format(day), color='red')
#     serge.act()
#     masha.act()
#     kolya.act()
#     murzik.act()
#     cprint(serge, color='cyan')
#     cprint(masha, color='cyan')
#     cprint(kolya, color='cyan')
#     cprint(murzik, color='cyan')


# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')

