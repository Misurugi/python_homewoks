#1. Светофор
import time
class TrafficLight:
     TrafficLight_color1 = "red"
     TrafficLight_color2 = "yellow"
     TrafficLight_color3 = "green"

     def running (self):
         print(f"Переключаем светофор:")

tr = TrafficLight()
tr.running()
print(tr.TrafficLight_color1)
time.sleep(7)
print(tr.TrafficLight_color2)
time.sleep(2)
print(tr.TrafficLight_color3)

#2. Дорога

class Road:
     road_lenght = None
     road_wight = None

     def asphalt (self):
         asf = (road_lenght * road_wight * 25 * i)//1000
         print(f"Масса асфальта, необходимого для покрытия дороги, составляет: {asf} тонн")

rd = Road()
road_lenght = int(input("Введите длину дороги, м: "))
road_wight = int(input("Введите ширину дороги, м: "))
i = int(input("Введите толщину планируемого асфальтового покрытия дороги, см: "))
rd.asphalt()

#3. Worker

class Worker:
     def set_data(self, name, surname, position, income):
         self.name = name
         self.surname = surname
         self.position = position
         self.income = income
     def get_data(self):
         self.income2 = self.income["wage"] + self.income["bonus"]
         print (self.name, self.surname, self.income2)
class position(Worker):
     def __init__(self, name, surname, position, income):
         self.set_data(name, surname, position, income)
         self.get_data()

worker1 = position("Brus", "Wayne", "Detectiv", income = {"wage":1500, "bonus":5000})
worker2 = position("Cat", "Woman", "Crime", income = {"wage":15400, "bonus":15000})

#4. Car

class Car:
    def car_data(self, speed, color, name, is_police):
        self.speed = int(speed)
        self.color = color
        self.name = name
        self.is_police = is_police

    def car_go(self):
        print("Машина поехала")

    def car_stop(self):
        print("Машина остановилась")

    def car_turn(self,diretcion=None):
        self.direction = diretcion
        print(f"Машина повернула: {diretcion}")

    def show_speed(self, speed=None):
        speed = self.speed
        print(f"Cкорость машины составляет, км/ч: {speed}")
    def car_decription(self):
        print(f"Марка: {self.name}, Цвет: {self.color}, Скорость: {self.speed}")

class TownCar (Car):
    def __init__(self, speed, color, name, is_police):
        self.car_data(speed, color, name, is_police)
        self.car_decription()
        self.car_go()
        self.car_stop()
        self.car_turn()
    def show_speed(self, speed=None):
        speed = self.speed
        if speed >= 60:
           print("Превышение скорости")
        else:
           print(f"Cкорость машины составляет, км/ч: {speed}")
class WorkCar (Car):
    def __init__(self, speed, color, name, is_police):
        self.car_data(speed, color, name, is_police)
        self.car_decription()
        self.car_go()
        self.car_stop()
        self.car_turn()
    def show_speed(self, speed=None):
        speed = self.speed
        if speed > 40:
           print("Превышение скорости")
        else:
           print(f"Cкорость машины составляет, км/ч: {speed}")
class SportCar (Car):
    def __init__(self, speed, color, name, is_police):
        self.car_data(speed, color, name, is_police)
        self.car_decription()
        self.car_go()
        self.car_stop()
        self.car_turn("Налево")
        self.show_speed()
class PoliceCar (Car):
    def __init__(self, speed, color, name, is_police):
        self.car_data(speed, color, name, is_police)
        self.car_decription()
        self.car_go()
        self.car_stop()
        self.car_turn("Направо")
        self.show_speed()

"""""
#c = Car()
#c.car_data(230, 'red', 'Viron', True)
#c.car_go()
#c.car_stop()
#c.car_turn()
#c.show_speed()
#c.car_decription()
"""""
tc = TownCar (60, "yellow", "taxi", True)
tc.show_speed()

wc = WorkCar (60, "green", "VW", True)
wc.show_speed()

sc = SportCar (250, "gold", "Lamborghini", True)

pc = PoliceCar (120, "black", "ford", True)


#5. Stationery

class Stationery:
    def title(self, name):
        self.name = name

    def draw(self, name):
        print(f'Запуск отрисовки {self.name}')

class Pen(Stationery):
    def __init__(self, name):
        self.title(name)
    def draw(self, name=None):
        print(f'{self.name} используется для письма')

class Pencil(Stationery):
    def __init__(self, name):
        self.title(name)
    def draw(self, name=None):
        print(f'Тут будет рисунок {self.name}ом')

class Handle(Stationery):
    def __init__(self, name):
        self.title(name)
    def draw(self, name=None):
        print(f'{self.name} используется для выделения текста')

p = Pen ("Ручка")
p.draw()

pc = Pencil ("Каранадаш")
pc.draw()

h = Handle ("Маркер")
h.draw()