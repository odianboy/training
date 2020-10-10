# -*- coding: utf-8 -*-
import zipfile
import os, shutil
from pprint import pprint
from os import startfile

import time as tm

# Нужно написать скрипт для упорядочивания фотографий (вообще любых файлов)
# Скрипт должен разложить файлы из одной папки по годам и месяцам в другую.
# Например, так:
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg
#
# Входные параметры основной функции: папка для сканирования, целевая папка.
# Имена файлов в процессе работы скрипта не менять, год и месяц взять из времени создания файла.
# Обработчик файлов делать в обьектном стиле - на классах.
#
# Файлы для работы взять из архива icons.zip - раззиповать проводником в папку icons перед написанием кода.
# Имя целевой папки - icons_by_year (тогда она не попадет в коммит)
#
# Пригодятся функции:
#   os.walk
#   os.path.dirname
#   os.path.join
#   os.path.normpath
#   os.path.getmtime
#   time.gmtime
#   os.makedirs
#   shutil.copy2
#
# Чтение документации/гугла по функциям - приветствуется. Как и поиск альтернативных вариантов :)
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

# TODO здесь ваш код

# file_name = 'C:\\Users\\Anton\\PycharmProjects\\untitled\\lesson_009\\icons'
#
# for dirpath, dirnames, filenames in os.walk(file_name):
#     for file in filenames:
#         full_file_path = os.path.join(dirpath, file)
#         secs = os.path.getmtime(full_file_path)
#         file_time = time.gmtime(secs)
#
# new = os.getcwd() + '\\icons_by_year'
# os.makedirs(new)

# dirname = 'C:\\Users\\Anton\\PycharmProjects\\untitled\\lesson_009\\icons'
# try:
#     newdir = 'C:\\Users\\Anton\\PycharmProjects\\untitled\\lesson_009\\icons_by_year'
#     OrignNewDir = newdir
# except:
#     newdir = dirname
#
#
# def image_sort(dirname, newdir, recur=0):
#     if not recur:
#         print('Сортировка началась...')
#     else:
#         print(f'Соритровка началась в {dirname}')
#         if not newdir:
#             newdir = dirname
#
#         imagelist = []
#
#         if os.path.isdir(dirname):
#             for x in os.listdir(dirname):
#                 absx = dirname + os.sep + x
#                 if os.path.isfile(absx):
#                     imagelist.append(absx)
#                 else:
#                     image_sort(absx, newdir + os.sep + x, recur=1)
#             for name in imagelist:
#                 try:
#                     file_date = time.localtime(os.stat(name).st_mtime)
#                 except EnvironmentError as error:
#                     print(f'seems error: {error} with ', name, '/n')
#                     continue
#
#                 imdir = '%s--%02d--%02d' % (file_date.tm_year, file_date.tm_mon, file_date.tm_mday)
#                 imdir = os.path.join(OrignNewDir, imdir)
#
#                 if os.path.split(dirname)[-1] == os.path.split(imdir)[-1]:
#                     continue
#                 elif not os.path.exists(imdir):
#                     print(f'Создаем папку {imdir}')
#                     os.makedirs(imdir)
#
#
#                 head, tail = os.path.split(name)
#                 replica = os.path.join(imdir, tail)
#                 if os.path.isfile(replica):
#                     to_ext = '.JPG'
#                     if to_ext[0] != '.':
#                         to_ext = '.'+to_ext
#                     root, ext = os.path.splitext(tail)
#                     print('Переименовывание', tail, 'к', root+'_1'+ext)
#                     path_orig = os.path.join(head, tail)
#                     path_new = os.path.join(head, root+'_1'+to_ext)
#                     os.rename(path_orig, path_new)
#                     imagelist.append(path_new)
#                 else:
#                     try:
#                         print(f'\n MOVE {name}, {imdir}')
#                         move(name, imdir)
#                     except EnvironmentError:
#                         print('\n Error with'+ name)
#
#         if not recur:
#             for root, dirs, files in os.walk(dirname):
#                 if not files:
#                     for name in dirs:
#                         os.rmdir(os.path.join(root, name))
#
#             print('Сортировка выполненна!')
#
#
# image_sort(dirname, newdir)
#
path = 'C:\\Users\\Anton\\PycharmProjects\\untitled\\lesson_009\\icons'
dict_year = {}
# os.startfile(path)


def get_time(path):
    path_normalized = os.path.normpath(path)
    for dirpath, dirnames, filenames in os.walk(path_normalized):
        for file in filenames:
            full_file_path = os.path.join(dirpath, file)
            stat = os.stat(full_file_path)
            time = stat.st_mtime
            file_time = tm.gmtime(time)

            if file_time[0] in dict_year:
                if file_time[1] in dict_year[file_time[0]]:
                    dict_year[file_time[0]][file_time[1]].append(full_file_path)
                else:
                    dict_year[file_time[0]][file_time[1]] = [full_file_path]
            else:
                dict_year[file_time[0]] = {file_time[1]: [full_file_path]}

            # newdir = os.getcwd() + '\\icons_by_year'
            # os.makedirs(newdir)

            newdir = 'C:\\Users\\Anton\\PycharmProjects\\untitled\\lesson_009\\icons_by_year'
            shutil.copy2(path, newdir)


get_time(path=path)


# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Основная функция должна брать параметром имя zip-файла и имя целевой папки.
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
