from sys import argv
script3_name, first_param, second_param = argv
print("Имя скрипта: ", script3_name)
print("Введите элементы цикла: ", first_param)
print("Введите количество повторений в цикле: ", second_param)

from itertools import cycle
maxX = int(second_param)
c = 0

for el in cycle(first_param):
    if c > maxX:
        break
    print(el)
    c += 1
