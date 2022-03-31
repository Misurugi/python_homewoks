# 1. Проверка данных
a = []
a.append(12)
a.append('gold')
a.append(5.4)
for x in a:
  print(type(x))

# 2. Сортировка списка
l = list(input("Введите элементы списка: "))
l[::2], l[1::2] = l[1::2], l[::2]
print(l)

# 3. Времена года
seasons = {'Зима': (1, 2, 12),
           'Весна': (3, 4, 5),
           'Лето': (6, 7, 8),
           'Осень': (9, 10, 11)}

month = int(input('Введите порядковый номер месяца: '))
for key in seasons.keys():
    if month in seasons[key]:
        print(key)

# 4. Рейтинг
i = int(input("Введите цифру своего рейтинга от 0 до 9: "))
items = [7, 6, 3, 5, 2]

# находим максимум в рейтинге
maxValue = max(items)

# находим последний индекс
lastIndex = -1
for element in items:
    if i == element:
        lastIndex = items.index(element)
if i > maxValue:
    items.insert(0, i)
elif lastIndex >= 0:
    items.insert(lastIndex +1, i)
else:
    items.append(i)
print(items)

#5. Список товаров

goods = []
i = 1
for i in range(1, 4):
    print(f"ВВедите информацию об {i}м товаре")
    nameGoods = input("Введите название товара: ")
    costGoods = input("Введите цену товара в рублях: ")
    measureGoods = input("Введите единицы измерения товара (шт./ед./упаковки): ")
    countGoods = input("Введите количество товара: ")
    goods.append((i, {"название": nameGoods, "стоимость": costGoods, "единицы измерения": measureGoods, "количество": countGoods}))
print(goods)

nameGoods = []
costGoods = []
measureGoods = []
countGoods = []

for i in goods:
    nameGoods.append(i[1].get("название"))
    costGoods.append(i[1].get("стоимость"))
    measureGoods.append(i[1].get("единицы измерения"))
    countGoods.append(i[1].get("количество"))

report = {
    "название": list(set(nameGoods)),
    "стоимость": list(set(costGoods)),
    "количество": list(set(countGoods)),
    "единицы измерения": list(set(measureGoods))
}

print(f"Отчет по списку товаров: \n{report}")