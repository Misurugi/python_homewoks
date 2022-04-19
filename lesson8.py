#1. Date

class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        my_date = []

        for i in day_month_year.split():
            if i != '-': my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2022 >= year >= 0:
                    return f'All right'
                else:
                    return f'Неправильный год'
            else:
                return f'Неправильный месяц'
        else:
            return f'Неправильный день'

    def __str__(self):
        return f'Текущая дата {Data.extract(self.day_month_year)}'
dt = Data('15 - 15 - 2354')
print(dt)
print(Data.valid(11, 12, 2001))
print(Data.extract("11 - 46 - 2057"))

#2. Исключение

class NotZero(Exception):
    def __init__(self, txt):
        self.txt = txt

print("Введите 2 числа (числитель и знаменатель). Программа совершит магию и покажет итог деления двух чисел")

inp_data1 = int(input("Введите первое число: "))

inp_data2 = int(input("Введите второе число: "))

try:
   res = inp_data1/inp_data2

except ZeroDivisionError:
   print("Вы ноль ввели ноль, на ноль делить нельзя!")
except OwnError as err:
   print(err)
else:
   print(f"Все хорошо. Результат магии: {res:.2f}")

#3. OnlyCount

class Error:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):

        val = int(input('Введите значения и нажимайте Enter - '))
        self.my_list.append(val)
        while True:
            try:
                val = int(input('Введите значения и нажимайте Enter - '))
                self.my_list.append(val)
                print(f'Текущий список - {self.my_list} \n ')

            except ValueError:
                print("Вы ввели не число. Для выхода нажмите 'y' ")

                y_or_n = input(f'Хотите выйти? Y/N ')

                if y_or_n == 'n' or y_or_n == 'N':
                    print(try_except.my_input())
                elif y_or_n == 'y' or y_or_n == 'Y':
                    return f'Вы вышли'

                else:
                    return f'Вы вышли'



try_except = Error()
print(try_except.my_input())