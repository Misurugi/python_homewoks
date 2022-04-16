from sys import argv
script_name, first_param, second_param, third_param = argv
print("Имя скрипта: ", script_name)
print("Ставка сотрудника в час, руб: ", first_param)
print("Количество отработанных часов, часы: ", second_param)
print("Размер премии, руб: ", third_param)
x = int(first_param)
y = int(second_param)
z = int(third_param)

result = (x * y) + z
print(result)
