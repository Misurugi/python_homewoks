#1. Скрипт 1 содержится в файле Script

# 2. вывести элементы исходного списка, значения которых больше предыдущего элемента
my_list1 = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result_list = [el for el, el2 in zip(my_list1[1:], my_list1[:-1]) if el > el2]
print(result_list)

#3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Решите задание в одну строку
list = [i for i in range (20, 240) if i % 20 == 0 or i % 21 == 0]
print(list)

#4. Определите элементы списка, не имеющие повторений
my_list2 = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result_list2 = [el for el, el2 in zip(my_list2[1:], my_list2[:-1]) if el != el2]
print(result_list2)

#5. Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти чётные числа от 100 до 1000 (включая границы). Нужно получить результат вычисления произведения всех элементов списка
own_list = [i for i in range(100, 1001, 2)]
print(sum(own_list))

from functools import reduce
own_list = [i for i in range(100, 1001, 2)]
print(reduce(lambda x, y: x * y, own_list))

#6. Скрипты в файлах Script2, Script3

#7.
from math import factorial
def in_fact(agr_1):
  N = factorial (agr_1)
  return N
print(in_fact(5))