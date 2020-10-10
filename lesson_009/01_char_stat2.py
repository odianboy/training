# -*- coding: utf-8 -*-

# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

import zipfile


class Chatterer:

    def __init__(self, file_name, name_txt):
        self.file_name = file_name
        self.name_txt = name_txt
        self.all_letters = {}
        self.file = []

    def unzip(self):
        with zipfile.ZipFile(self.file_name, 'r') as zfile:
            zfile.extractall()

    def open(self):
        self.unzip()
        with open(self.name_txt, 'r', encoding='cp1251') as file:
            for text in file:
                self.open()
                self.file.append(text)

    def dict_letters(self):
        for text in self.file:
            for letter in text:
                if letter.isalpha():
                    self.all_letters[letter] = 0

    def counting(self):
        self.dict_letters()
        self.sum_alpha = 0
        for text in self.file:
            for letter in text:
                for counting in self.all_letters:
                    if letter == counting:
                        self.all_letters[letter] += 1
        for sum in self.all_letters:
            self.sum_alpha += self.all_letters[sum]

    def tabl(self):
        print('+-------------+--------------+')
        print('|   буква     |    частота   |')
        print('+-------------+--------------+')
        for keys in self.all_letters:
            if len(str(self.all_letters[keys])) == 1:
                print('|     ', keys, '     |    ', self.all_letters[keys], '       |')
            if len(str(self.all_letters[keys])) == 2:
                print('|     ', keys, '     |    ', self.all_letters[keys], '      |')
            if len(str(self.all_letters[keys])) == 3:
                print('|     ',keys , '     |    ', self.all_letters[keys],'     |')
            if len(str(self.all_letters[keys])) == 4:
                print('|     ',keys , '     |    ', self.all_letters[keys],'    |')
            if len(str(self.all_letters[keys])) == 5:
                print('|     ', keys, '     |    ', self.all_letters[keys], '   |')
            if len(str(self.all_letters[keys])) == 6:
                print('|     ', keys, '     |    ', self.all_letters[keys], '  |')
            print('|.............|..............|')
        print('|    итого    |  ',self.sum_alpha, '   | ')
        print('+-------------+--------------+')





cha = Chatterer('python_snippets/voyna-i-mir.txt.zip','voyna-i-mir.txt')
cha.counting()
cha.tabl()
# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
