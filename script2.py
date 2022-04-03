from sys import argv
script2_name, first_param, second_param = argv
print("Имя скрипта: ", script2_name)
print("Начальное число: ", first_param)
print("Конечное число ", second_param)
minX = int(first_param)
maxX = int(second_param)

from itertools import count
for el in count(minX):
    if el > maxX:
        break
    else:
        print(el)
