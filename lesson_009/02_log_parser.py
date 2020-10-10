# -*- coding: utf-8 -*-
import os
from pprint import pprint

# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

# TODO здесь ваш код

file_name = 'events.txt'


class Logparser:

    def __init__(self, analyze_name, file_result):
        self.analyze_name = analyze_name
        self.file_result = file_result

    def read_file(self):
        with open(self.analyze_name, 'r') as file:
            for line in file:
                if 'NOK' in line:
                    file_add = open(self.file_result, 'a', encoding='utf8')
                    file_add.write(line[:-16] + ']' + '\n')
                    file_add.close()


logrun = Logparser(analyze_name=file_name, file_result='nok_file')
logrun.read_file()




# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828


class Hours(Logparser):

    def read_file(self):
        with open(self.analyze_name, 'r') as file:
            for line in file:
                if 'NOK' in line:
                    file_add = open(self.file_result, 'a', encoding='utf8')
                    file_add.write('[' + line[12:17] + ']' + '\n')
                    file_add.close()

#
# hours = Hours(analyze_name=file_name, file_result='nok_file')
# hours.read_file()


class Month(Logparser):

    def read_file(self):
        with open(self.analyze_name, 'r') as file:
            for line in file:
                if 'NOK' in line:
                    file_add = open(self.file_result, 'a', encoding='utf8')
                    file_add.write('[' + line[6:11] + ']' + '\n')
                    file_add.close()


# month = Month(analyze_name=file_name, file_result='nok_file')
# month.read_file()


class Year(Logparser):

    def read_file(self):
        with open(self.analyze_name, 'r') as file:
            for line in file:
                if 'NOK' in line:
                    file_add = open(self.file_result, 'a', encoding='utf8')
                    file_add.write(line[0:5] + ']' + '\n')
                    file_add.close()


# year = Year(analyze_name=file_name, file_result='nok_file')
# year.read_file()
