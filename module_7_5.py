import os
import time

directory = r'C:\Users\Юлия\PycharmProjects\NewProject\module_7' # текущая директория

for file in os.walk(directory): # обход каталог, путь к которому указывает переменная directory
    print(file)
filepath = os.path.join(directory) # формирование полного пути к файлам
print(filepath)
filetime = os.path.getmtime(directory)
formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime)) # время последнего изменения файла
print(formatted_time)
filesize = os.path.getsize(directory) # получение размера файла
print(filesize)
parent_dir = os.path.dirname(directory) # получение родительской директории файла
print(parent_dir)

print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения:'
      f'{formatted_time}, Родительская директория: {parent_dir}')
