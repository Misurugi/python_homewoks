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