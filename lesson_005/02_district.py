# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

# TODO здесь ваш код
from pprint import pprint
from lesson_005.district.central_street.house1 import room1 as sh1_1, room2 as sh1_2
from lesson_005.district.central_street.house2 import room1 as sh2_1, room2 as sh2_2

from lesson_005.district.soviet_street.house1 import room1 as sv1_1, room2 as sv1_2
from lesson_005.district.soviet_street.house2 import room1 as sv2_1, room2 as sv2_2

dict_house = ", ".join(sh1_1.folks), ", ".join(sh1_2.folks), ", ".join(sh2_1.folks), ", ".join(sh2_2.folks),\
             ", ".join(sv1_1.folks), ", ".join(sv1_2.folks), ", ".join(sv2_1.folks), ", ".join(sv2_2.folks)

pprint(dict_house)