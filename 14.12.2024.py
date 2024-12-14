#Задача №1
#найти наиболее частое число
#Дан список целых чисел. Напишите программу, которая находит наиболее часто встречающееся число в списке
# Пример списка целых чисел
s = [1, 2, 3, 2, 3, 3, 4, 5, 6, 2, 3]
# Инициализируем переменные для хранения наиболее часто встречающегося числа и его частоты
number = None
max_count = 0
# Проходим по всем элементам списка
for i in s:
    # Подсчитываем количество вхождений текущего числа в списке
    count = s.count(i)
    # Если количество вхождений больше текущего максимума, обновляем наиболее часто встречающееся число
    if count > max_count:
        number = i
        max_count = count
# Выводим результат
print(f"Наиболее часто встречающееся число: {number}")
print(f"Повторяется раз: {max_count}")

#Задача №2
#найти все уникальные пары, сумма которых равна заданному числу
#дан список целых чисел и целевое число target. Напишите программу, которая находит все уникальные пары чисел из списка, сумма которых равна target.
#Входные данные: [1, 2, 3, 4, 5], target = 5
#Выходные данные: [(1, 4), (2, 3)]
# Входные данные
s = [1, 2, 3, 4, 5]
target = 5
# Список для хранения уникальных пар
s1 = []
# Проходим по всем возможным парам чисел
for i in range(len(s)):
    for j in range(i + 1, len(s)):
        if s[i] + s[j] == target:
            # Добавляем пару в список, чтобы она была уникальной
            s1.append((s[i], s[j]))
# Выводим результат
print("Уникальные пары чисел, сумма которых равна", target, ":", s1)

#Задача №3
#повернуть список на k шагов
#Дан список и целое число k. Напишите программу, которая поворачивает список на k шагов вправо.
#Входные данные: [1, 2, 3, 4, 5], k = 2
#Выходные данные: [4, 5, 1, 2, 3]
s = [1, 2, 3, 4, 5]
k = 2
# Поворачиваем список на k шагов вправо
k = k % len(s)  # На всякий случай, если k больше длины списка
s1 = s[-k:] + s[:-k]
# Выводим результат
print(s1)

#Задача №4
#сжать список, оставив только первые вхождения одинаковых элементов
#Дан список, содержащий повторяющиеся элементы. Напишите программу, которая сжимает список, оставляя только первые вхождения одинаковых элементов.
#Входные данные: [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5]
#Выходные данные: [1, 2, 3, 4, 5]
#Входные данные
l = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5]
result = []
for i in l:
    if i not in result:
      result.append(i)
# Вывод результата
print(result)

#Задача №5
#найти пересечение двух списков
#Даны два списка. Напишите программу, которая находит пересечение этих списков (то есть элементы, которые присутствуют в обоих списках).
#Входные данные:
#[1, 2, 3, 4, 5]
#[3, 4, 5, 6, 7]
#Выходные данные: [3, 4, 5]
#Входные данные
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
x = []
for i in list1:
    if i in list2 and i not in x:
     x.append(i)
#Вывод результата
print(x)
