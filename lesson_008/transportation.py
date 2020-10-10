import random
from termcolor import cprint


class Road:

    def __init__(self, start, end, distance):
        self.start = start
        self.end = end
        self.distance = distance


class Warehouse:
    """Склад"""

    def __init__(self, name, content=0):  # content - это содержимое склада
        self.name = name
        self.content = content
        self.road_out = None
        self.queue_in = []  # количество грузовиков, которые въехали
        self.queue_out = []     # количество грузовиков, которые выехали

    def __str__(self):
        return "Склад {} груза {}".format(self.name, self.content)

    def set_road_out(self, road):
        """Дорога которая ведет со склада"""
        self.road_out = road

    def truck_arrived(self, truck):
        """Прибытие грузовика"""
        self.queue_in.append(truck)
        truck.place = self
        print("{} прибыл грузовик {}".format(self.name, truck))

    def get_next_truck(self):
        """Погрузчик мог выбрать следующий грузовик, из очереди"""
        if self.queue_in:
            truck = self.queue_in.pop()
            return truck

    def truck_ready(self, truck):
        """Погрузчик посылает сообщегние складу, о том что он загрузизил уже грузовик"""
        self.queue_out.append(truck)    # добавили очередь на выход
        print("{} грузовик готов {}".format(self.name, truck))

    def act(self):
        """Позволяет сотрудникам склада, выпускать/запускать грузовики"""
        while self.queue_out:   # До тех пор пока у нас не пустая очередь на выход, даем грузовику указания, езжай ты туда-то
            truck = self.queue_out.pop()
            truck.go_to(road=self.road_out)


class Vehicle:  # Машина
    fuel_rate = 0  # Скорость потребеления топливо в час
    total_fuel = 0  # максимальное затраченное топливо

    def __init__(self, model):
        self.model = model
        self.fuel = 0   # Топливо

    def __str__(self):
        return "{} топлива {}".format(self.model, self.fuel)

    def tank_up(self):
        """Загрузиться"""
        self.fuel += 1000
        Vehicle.total_fuel += 1000
        print("{} заправился".format(self.model))

    def act(self):
        if self.fuel <= 10:  # если топливо осталось меньше 10
            self.tank_up() # надо заправится
            return False
        return True


class Truck(Vehicle):  # Грузовик
    fuel_rate = 50
    dead_time = 0

    def __init__(self, model, body_space=1000):  # body_space, ёмкость грузовика
        super().__init__(model=model)   # Подтягиваем базовый класс
        self.body_space = body_space
        self.cargo = 0  # Сколько он может везти груза
        self.velocity = 100  # Скорость
        self.place = None   # где он сейчас находится
        self.distance_to_target = 0     # сколько ему осталось до точки

    def __str__(self):
        res = super().__str__()
        return res + " груза {}".format(self.cargo)

    def ride(self):
        """Ехать по дороге"""
        self.fuel -= self.fuel_rate
        if self.distance_to_target > self.velocity:     # если расстояние до цели осталось больше чем его скорость
            self.distance_to_target -= self.velocity    # он еще едет, расстояние уменьшилось
            print("{} едет по дороге, осталось {}".format(self.model, self.distance_to_target))
        else:
            self.place.end.truck_arrived(self)
            print("{} доехал".format(self.model))

    def go_to(self, road):
        """Выехать на дорогу со склада"""
        self.place = road
        self.distance_to_target = road.distance
        print("{} выехал в путь".format(self.model))

    def act(self):
        """Что делать грузовику в данный момент времени"""
        if super().act():
            if isinstance(self.place, Road):  # если мое место является дорогой
                self.ride()     # то я еду
            else:
                Truck.dead_time += 1


class AutoLoader(Vehicle):  # Погрузчик
    fuel_rate = 30
    dead_time = 0

    def __init__(self, model, bucket_capacity=100, warehouse=None, role="loader"):
        # bucket_capacity - ёмкость ковша, warehouse - к чему он привязан (Склад), role - роль загрузка/погрузка
        super().__init__(model=model)
        self.bucket_capacity = bucket_capacity
        self.warehouse = warehouse
        self.role = role
        self.truck = None   # текущий грузовик который он загружает

    def __str__(self):
        res = super().__str__()
        return res + " грузим {}".format(self.truck)

    def act(self):
        if super().act():
            if self.truck is None:
                self.truck = self.warehouse.get_next_truck()  # Дай мне следующий грузовик который надо обрабатывать
                if self.truck is None:
                    print("{} нет грузовиков для работы".format(self.model))
                    AutoLoader.dead_time += 1
                print("{} взял в работу {}".format(self.model, self.truck))
            elif self.role == "loader":
                self.load()
            else:
                self.unload()

    def load(self):
        """Загрузка"""
        if self.warehouse.content == 0:
            print("{} на складе ничего нет!".format(self.model))
            if self.truck:
                self.warehouse.truck_ready(self.truck)
                self.truck = None
                return
        self.fuel -= self.fuel_rate
        truck_cargo_rest = self.truck.body_space - self.truck.cargo     # свободное место в грузовике
        if truck_cargo_rest >= self.bucket_capacity:    # если объема осталось больше чем у нас загружает ковш
            cargo = self.bucket_capacity
        else:
            cargo = truck_cargo_rest
        if self.warehouse.content < cargo:
            cargo = self.warehouse.content
            # self.warehouse.content -= self.bucket_capacity  # взяли ковш со склада и перегрузили в грузовик
            # self.truck.cargo += self.bucket_capacity
            self.warehouse.content -= cargo  # возьмем остаток
            self.truck.cargo += cargo    # положим столько, сколько взяли со склада
            print("{} грузил {}".format(self.model, self.truck))
        if self.truck.cargo == self.truck.body_space:
            self.warehouse.truck_ready(self.truck)  # грузовик загружен
            self.truck = None   # простаивает

    def unload(self):
        """Разгрузка"""
        self.fuel -= self.fuel_rate
        if self.truck.cargo >= self.bucket_capacity:
            self.truck.cargo -= self.bucket_capacity
            self.warehouse.content += self.bucket_capacity
        else:
            self.truck.cargo -= self.truck.cargo    # выгружаем с машины
            self.warehouse.content += self.truck.cargo  # пополняем склад
            print("{} разгружал {}".format(self.model, self.truck))
        if self.truck.cargo == 0:   # грузовик разгрузили
            self.warehouse.truck_ready(self.truck)
            self.truck = None


TOTAL_CARGO = 100000  # груза на складе

moscow = Warehouse(name="Москва", content=TOTAL_CARGO)
piter = Warehouse(name="Питер", content=0)

moscow_piter = Road(start=moscow, end=piter, distance=715)
piter_moscow = Road(start=piter, end=moscow, distance=780)

moscow.set_road_out(moscow_piter)
piter.set_road_out(piter_moscow)

loader_1 = AutoLoader(model="Bobcat", bucket_capacity=1000, warehouse=moscow, role="loader")
loader_2 = AutoLoader(model="lonking", bucket_capacity=500, warehouse=piter, role="unloader")

trucks = []
for number in range(10):
    truck = Truck(model="КАМАЗ # {}".format(number), body_space=5000)
    moscow.truck_arrived(truck)
    trucks.append(truck)


hour = 0

while piter.content < TOTAL_CARGO:  # До тех пор пока содержимое питерского склада меньше груза которого нужно перевезти
    hour += 1
    cprint("--------------- Час {} -----------------".format(hour), color="red")
    for truck in trucks:
        truck.act()
    loader_1.act()
    loader_2.act()
    moscow.act()
    piter.act()
    for truck in trucks:
        cprint(truck, color="cyan")
    cprint(loader_1, color="cyan")
    cprint(loader_2, color="cyan")
    cprint(moscow, color="cyan")
    cprint(piter, color="cyan")


cprint("Всего затраченно топлива {}".format(Vehicle.total_fuel), color="yellow")
cprint("Общий простой грузовиков {}".format(Truck.dead_time), color="yellow")
cprint("Общий простой погрузчиков {}".format(AutoLoader.dead_time), color="yellow")