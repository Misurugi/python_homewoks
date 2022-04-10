#1. Создание файла
new = open("file1.txt", 'a')
content = input("Введите текст: ")
new.write(content)
new.close()

#2. Чтение содержимого файла
file2 = open("file2.txt", 'r')
i = 0
for line in file2:
    i += 1
    l = len(line.split())
    print(f"Строка {i}, количество слов: {l}, содержание: {line}")
file2.close()

#3. Чтение содержимого файла
key = []
value = []
with open("file3.txt", 'r+', encoding='utf-8') as file3:
    data = [line.split() for line in file3.readlines()]
for i in data:
    key.append(i[0])
for i in data:
    value.append(i[1])

value2 = [int(x) for x in value]
value3 = []
for x in value2:
    if x < 100000:
        value3.append(x)
print(key)
print(value)

list2 = dict(zip(key, value2))
# я не понимаю каким образом вывести необходимые значения словаря с условиями ЗП ниже определенного показателя. при попытке использовать условие x < 100000 вылетает ошибка что value не числовое значние.




#4.
#with open("file4.txt", 'r', encoding='utf-8') as file4:
 #   data2 = [line.split("-") for line in file4.readlines()]


#    l1 = file4.readline()
 #   l2 = file4.readline()
  #  l3 = file4.readline()
   # l4 = file4.readline()

#if l1 == 'One - 1':
 #   l1new = 'Один - 1'
 #   print(l1new)

#if l2 == 'Two — 2':
 #   l2new = 'Два - 2'
  #  print(l2new)

#if l3 == 'Three — 3':
 #   l3new = 'Три - 3'
  #  print(l3new)

#if l4 == 'Four — 4':
 #   l4new = 'Четыре - 4'
  #  print(l4new)

# с подобной логикой получается заменить только последнюю строку, остальные не записываются.

#5. Добавление чисел
with open('file5.txt', 'r+') as file:
    file.write(input('Введите числа через пробел: '))

    print(l)

