#1. Создание матрицы
import numpy as np

class Matrix:
    def __init__(self, a):
        self.a = a
        print(f"Матрица: {a}")

    def __add__(self, other):
        return Matrix(self.a + other.a)

    def __str__(self):
        return " ".join([' '.join(map(str, row)) for row in self.a])


mx1 = Matrix(np.array([[2, 4, 5], [5, 8, 9], [10, 15, 18]]))
mx2 = Matrix(np.array([[4, 5, 8], [1, 2, 1], [20, 40, 10]]))
print("сумма матриц в одну строку:", (mx1 + mx2))

#2. Расчет одежды
from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    def __add__(self, other):
        return f'Сумма затраченной ткани равна: {(self.param / 6.5 + 0.5) + (2 * self.param + 0.3):.2f}'

class Coat(Clothes):
    def consumption(self):
        return f'Для пошива пальто нужно: {self.param / 6.5 + 0.5 :.2f} ткани'

    def abstract(self):
        return 'какая-то строчка'

class Costume(Clothes):
    def consumption(self):
        return f'Для пошива костюма нужно: {2 * self.param + 0.3 :.2f} ткани'

    def abstract(self):
        pass

coat = Coat(400)
costume = Costume(55)
print(coat.consumption())
print(costume.consumption())
print(coat + costume)

#3. Работа с органическими клетками
class Cell:
    def __init__(self, numbers_cell):
        self.numbers_cell = numbers_cell

    def __add__(self, other):
        self.s = self.numbers_cell + other.numbers_cell
        return self.s

    def __sub__(self, other):
        if self.numbers_cell - other.numbers_cell > 0:
            self.d = self.numbers_cell - other.numbers_cell
            return self.d
        else:
            print("Недопустимая операция")

    def __mul__(self, other):
        self.m = self.numbers_cell * other.numbers_cell
        return self.m

    def __truediv__(self, other):
        self.t = self.numbers_cell // other.numbers_cell
        return self.t

    def make_order(self, row):
        result = ''
        for i in range(int(self.numbers_cell / row)):
            result += '*' * row + '\n'
        result += '*' * (self.numbers_cell % row) + '\n'
        return result


c1 = Cell(45)
c2 = Cell(40)
print("Количество ячеек в клетке после сложения:", c1 + c2)
print("Количество ячеек в клетке после вычитания:", c1 - c2)
print("Количество ячеек в клетке после умножения:", c1 * c2)
print("Количество ячеек в клетке после деления:", (c1 / c2))
print(c1.make_order(9))

