#Задача №1
#написать программу, которая вычисляет сумму всех чисел от 1 до заданного пользователем числа N.
# Ввод числа N от пользователя
N = int(input("Введите число N: "))

# Инициализация переменной для хранения суммы
total_sum = 0

# Проход по числам от 1 до N с использованием цикла for
for i in range(1, N + 1):
    total_sum += i  # Добавляем текущее число к сумме
# Выводим результат
print("Сумма чисел от 1 до N равна: ", total_sum, end="")
print(" (", end="")
for i in range(1, N + 1):
    print(f"{i}+", end="")
print("\b)")

#Задача №2
#напишите таблицу умножения для числа N от 1 до 10
# Ввод числа N от пользователя
N = int(input("Введите число N: "))

# Цикл для вывода таблицы умножения от 1 до 10
for i in range(1, 11):
    print(N, "*", i, "=", N * i, end=" / ")
    i += 1
print()

#Задача №3
#напишите программу, которая выводит числа от 1 до N в обратном порядке
# Ввод числа N от пользователя
N = int(input("Введите число N: "))

# Цикл для вывода чисел от N до 1
for i in range(N, 0, -1):
    print(i)

#Задача №4
#выведите все чётные числа от 1 до N
# Ввод числа N от пользователя
N = int(input("Введите число N: "))

# Цикл для вывода четных чисел от 1 до N
for i in range(2, N + 1, 2):
    print(i)

#Задача №5
#запросите строку S и число N. Выведите строку S повторенную N раз
# Запрос строки S и числа N от пользователя
S = input("Введите строку S: ")
N = int(input("Введите число N: "))

# Цикл для вывода строки S, повторенной N раз
for i in range(N):
    print(S, end="")  #Используем end='' для того, чтобы не добавлять лишние новые строки
    print()

#Задача №6
#посчитайте сумму всех чётных чисел от 1 до N
# Ввод числа N от пользователя
N = int(input("Введите число N: "))
# Инициализация переменной для хранения суммы
a = 0
for i in range(2, N + 1, 2):  # Начинаем с 2 и идём с шагом 2
    a += i
print(f"{a} (", end="")
for i in range(2, N +1, 2):
    print(f"{i}+", end="")
print("\b)")

#Задача №7
#рассчитайте факториал числа N
# Ввод числа N от пользователя
N = int(input("Введите число N: "))

# Инициализация переменной для хранения суммы
a = 1

# Проход по числам от 1 до N с использованием цикла for
for i in range(1, N + 1):
    a *= i  # Добавляем текущее число к сумме
# Выводим результат
print("Факториал чисел от 1 до N равен: ", f"{a} (", end="")
for i in range(1, N +1):
    print(f"{i}*", end="")
print("\b)")

#Задача №8
#выведите цифры заданного числа N в обратном порядке
N = int(input("Введите число N: "))
# Определяем количество цифр в числе
num_digits = len(str(N))  # Можно также вычислить вручную, но это простой способ
for i in range(num_digits):
        digit = N % 10  # Получаем последнюю цифру
        print(digit, end='')  # Выводим цифру без перехода на новую строку
        N //= 10  # Удаляем последнюю цифру из числа
print()

#Задача №9
#определите сколько цифр в числе N
N = int(input("Введите число N: "))  # Ввод числа
count = 0  # Счётчик цифр
# Проходим по числу с делением на 10
for i in range(100):  # Предел 100 достаточен для большинства чисел
    if N == 0:  # Если число стало 0, прекращаем цикл
        break
    N = N // 10  # Убираем последнюю цифру
    count += 1  # Увеличиваем счётчик
print(count)

#Задача №10
#посчитайте сумму всех цифр числа N
N = int(input("Введите число N: "))  # Ввод числа
sum_digits = 0  # Сумма цифр
# Проверяем, что число положительное или ноль
if N == 0:
    sum_digits = 0  # Для числа 0 сумма цифр = 0
else:
    for _ in range(len(str(abs(N)))):  # Прокручиваем цикл по количеству цифр в числе
        sum_digits += N % 10  # Добавляем последнюю цифру
        N = N // 10  # Убираем последнюю цифру
print(sum_digits)



