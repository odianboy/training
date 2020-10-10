# -*- coding: utf-8 -*-

import os, time, shutil
import zipfile
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

# with zipfile.ZipFile('icons.zip', 'r') as zfile:
#     zfile.extractall()

# os.rename("icons/actions/bookmark-new.png", "icons_by_year/bookmark-new.png")  #перемешаем фото в другую папку

# def UnZipNew(path, patht):
#     f = zipfile.ZipFile(path, 'r')
#     for file in f.infolist():
#         d = file.date_time
#         gettime = "%s/%s/%s %s:%s" % (d[0], d[1], d[2], d[3], d[4])
#         f.extract(file, patht)
#         filep = os.path.join(patht, file.filename)
#         timearry = time.mktime(time.strptime(gettime, '%Y/%m/%d %H:%M'))
#         os.utime(filep, (timearry, timearry))
# UnZipNew('icons.zip','icons')


class Refact_Png:
    def __init__(self,file_name,path_to_foldes):
        self.file_name = file_name
        self.path_to_folder = path_to_foldes


    def UnZipNew(self,path, patht):
        f = zipfile.ZipFile(path, 'r')
        for file in f.infolist():
            d = file.date_time
            gettime = "%s/%s/%s %s:%s" % (d[0], d[1], d[2], d[3], d[4])
            f.extract(file, patht)
            filep = os.path.join(patht, file.filename)
            timearry = time.mktime(time.strptime(gettime, '%Y/%m/%d %H:%M'))
            os.utime(filep, (timearry, timearry))


    def open_file(self,name_new_file):
        self.name_new_file = name_new_file

        for dirpath, dirname, filenames in os.walk(self.file_name):  # прогулка по всем папка и файлам
            for file_png in filenames:
                full_file_path = os.path.join(dirpath, file_png)
                # secc = os.path.getctime(full_file_path)
                # print(time.gmtime(secc))
                (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(full_file_path)
                # print(str(time.gmtime(mtime)))
                self.creating_folders_year(str(time.gmtime(mtime)[0]))
                self.creating_folders_mon(str(time.gmtime(mtime)[1]))
                # os.rename("icons/actions/bookmark-new.png", "icons_by_year/bookmark-new.png")
                os.rename(full_file_path, self.name_new_file+'\\'+self.data +'\\'+self.mon +'\\' +file_png)

    def creating_folders_year(self,data):
        self.data = data
        check_file = os.path.exists(self.path_to_folder + self.data)
        if check_file == False:
            os.mkdir(self.path_to_folder + self.data)


    def creating_folders_mon(self,mon):
        self.mon = mon
        check_file = os.path.exists(self.path_to_folder + self.data + '\\' + self.mon)
        if check_file == False:
            os.mkdir(self.path_to_folder  + self.data + '\\'+ self.mon + '\\')







refact = Refact_Png('icons',"D:\Питон\skillbox\dz\9\icons_by_year\\")
refact.UnZipNew('icons.zip','icons')
refact.open_file('icons_by_year')


# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Основная функция должна брать параметром имя zip-файла и имя целевой папки.
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
