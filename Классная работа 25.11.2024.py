#Задача №1
#Незакрашенный квадрат
# Размер квадрата
size = 5
# Используем цикл для создания строк
for i in range(size):
    for j in range(size):
        # Печатаем * на краях, а внутри - пробел
        if i == 0 or i == size - 1 or j == 0 or j == size - 1:
            print("*", end="")
        else:
            print(" ", end="")
    # Переход на новую строку после каждого ряда
    print()
print()

#Задача №2
#Закрашенный квадрат
# Размер квадрата
size = 5
# Используем цикл для создания строк
for i in range(size):
    for j in range(size):
        print("*", end="")  # Печатаем символ * для заполнения квадрата
    print()  # Переход на новую строку после каждого ряда

#Задача №3
#Равнобедренный треугольник незакрашенный
# Высота треугольника
height = 5
# Используем цикл для создания строк
for i in range(1, height + 1):
#Печатаем пробелы для выравнивания
    for j in range(height - i):
        print(" ", end="")  # Печатаем пробелы для выравнивания
    # Печатаем символы * для границ треугольника
    for j in range(2 * i - 1):
        # Печатаем # на краях
        if j == 0 or j == 2 * i - 2 or i == height:
            print("*", end="")
        else:
            print(" ", end="")
    # Переход на новую строку после каждого ряда
    print()

#Задача №4
#Равнобедренный треугольник закрашенный
# Высота треугольника
height = 5
# Используем цикл для создания строк
for i in range(1, height + 1):
    # Печатаем пробелы для выравнивания
    for j in range(height - i):
        print(" ", end="")  # Печатаем пробелы для выравнивания
    # Печатаем символы * для треугольника
    for j in range(2 * i - 1):
        print("*", end="")
    # Переход на новую строку после каждого ряда
    print()

#Задача №5
#Незакрашенный прямоугольный треугольник
# Высота треугольника
height = 5
# Рисуем треугольник
for i in range(1, height + 1):
    if i == 1 or i == height:  # Первый и последний ряды полностью заполнены
        print('*' * i)
    else:  # Внутренние ряды содержат звездочку в начале и в конце
        print('*' + ' ' * (i - 2) + '*')

#Задача №6
#Закрашенный прямоугольный треугольник
# Высота треугольника
height = 5
# Используем цикл для создания строк
for i in range(1, height + 1):
    # Печатаем нужное количество символов * для каждой строки
    for j in range(i):
        print("*", end="")
    # Переход на новую строку после каждого ряда
    print()
print()

#Задача №7
#Равнобедренный треугольник развернутый вниз незакрашенный
# Высота треугольника
height = 5
# Используем цикл для создания строк
for i in range(height, 0, -1):
    # Печатаем пробелы для выравнивания
    for j in range(height - i):
        print(" ", end="")  # Печатаем пробелы для выравнивания
    # Печатаем символы * для границ треугольника
    for j in range(2 * i - 1):
        # Печатаем символы * только на краях
        if j == 0 or j == 2 * i - 2 or i == height:
            print("*", end="")
        else:
            print(" ", end="")
    # Переход на новую строку после каждого ряда
    print()

#Задача №8
#Равнобедренный треугольник развернутый вниз закрашенный
# Высота треугольника
height = 5
# Используем цикл для создания строк
for i in range(height, 0, -1):
    # Печатаем пробелы для выравнивания
    for j in range(height - i):
        print(" ", end="")  # Печатаем пробелы для выравнивания
    # Печатаем символы * для треугольника
    for j in range(2 * i - 1):
        print("*", end="")
    # Переход на новую строку после каждого ряда
    print()


