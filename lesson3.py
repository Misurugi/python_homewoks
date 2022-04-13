#№1. Функция с делением
def my_segm():
    arg_1 = int(input("Введите первое число: "))
    arg_2 = int(input("Введите второе число: "))

    if arg_2 == 0:
        print("На ноль делить нельзя!")
        arg_3 = int(input("Введите второе число: "))
        segm = arg_1 / arg_3
    else:
        segm = arg_1 / arg_2
    return segm
print(my_segm())

#№1_1 Функция с делением
def my_segm(arg_1, arg_2):
    if arg_2 == 0:
        print("На ноль делить нельзя!")
        arg_3 = int(input("Введите второе число: "))
        segm = arg_1 / arg_3
    else:
        segm = arg_1 / arg_2
    return segm
print(my_segm(8,2))


#№2 Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя
def my_contact(name, surname, year_of_birth, city, email, phone):
    print(f"name - {name}; surname - {surname}; year_of_birth - {year_of_birth}; city - {city}; email - {email}; phone -{phone}")
my_contact(name="Саша", surname="Амосов", year_of_birth="1985", city="Екатеринбург", email="s.v.d@list.ru", phone="89120359728")

#№4 Функция, выполняющая возведение числа в степень
def my_func(arg_1, arg_2):
    if arg_1 < 0 and arg_2 > 0:
        print("Первое число доложно быть целым положительными\nВторое число должно быть целым отрицательным")
    else:
        s = arg_1 ** arg_2
    return s
print(my_func(8,-10))

#3 Из первого ДЗ
b = input("Введите число:  ")
c = b*2
d = b*3
summ = int(b) + int(c) + int(d)
print(summ)

# 5. Программа запрашивает у пользователя строку чисел, разделённых пробелом
add = True
while add:
     x = input('Введи значения через проблел: ').split()
     new_list = list(map(int, x))
     print(sum(new_list))
     break


# 6, 7. функция принимающая латинские слова, возвращая их в регистр с заглавной большой буквой
def int_func(*args):
    return args
print(int_func("one, two, three".title()))