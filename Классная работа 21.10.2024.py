# Задача №1
#Чётность и кратность числа
#Программа должна принимать целое число и проверять чётное ли это число (с помощью %) и является ли оно кратным 5. В зависимости от результата программа должна выводить соответствующие сообщения.

a = int(input("Введите целое число: "))
if a % 2 == 0:
  print("Чётное число")
else:
  print("Нечётное число")
if a % 5 == 0:
  print("Кратное 5")
else:
  print("Некратное 5")

#Задача №2
#Калькулятор расхода топлива
#напишите программу, которая принимает количество литров топлива, стоимость за литр и пройденное расстояние. Программа должна рассчитать и вывести сколько было потрачено денег на топливо и расход топлива на 100 км.

a = float(input("Введите количество литров топлива: "))
b = float(input("Введите стоимость литра топлива: "))
c = float(input("Введите пройденное расстояние: "))
print("Сколько было потрачено денег на топливо:", a*b)
print("Расход топлива на 100 км:" , (a / c)*100)

#Задача №3
#Калькулятор налогов
#напишите программу, которая принимает доход пользователя и рассчитывает сумму налога, используя следующие условия - если доход меньше 10 000 то налог 5%, если доход от 10 000 до 50 000 то налог 10%,
#если доход выше 50 000 налог 15%

a = float(input("Введите доход пользователя: "))
if a <= 10000:
  b = a * 0.05
  print("Налог: :", b)
elif  10000 <= a <= 50000:
  b = a * 0.1
  print("Налог: :", b)
elif a > 50000:
  b = a * 0.15
  print("Налог: :", b)
else:
  print("Неправильный ввод")

#Задача #4
#Конвертер валют
#Программа должна принимать сумму в рублях и конвертировать её в доллары или евро в зависимости от выбора пользователя. Курсы валют можно задать статически.

a = float(input("Введите сумму в рублях: "))
operation = input("Выберите валюту конвертирования (доллары/евро): ")
if operation == "доллары":
  print("Количество долларов:", a / 96.55)
elif operation == "евро":
  print("Количество евро:", a / 104.45)
else:
  print("Неправильный выбор")

# Задача #5
#Калькулятор BMI
#напиши программу, которая принимает рост в метрах и вес в килограммах пользователя и вычисляет индекс массы тела (BMI). Выведи соответствующую категорию: недостаточный вес, норма, избыточный вес или ожирение.
a = float(input("Введите рост в метрах: "))
b = float(input("Введите вес в килограммах: "))
BMI = b / (a ** 2)
if BMI <= 18.5:
    print("Недостаточный вес")
elif 18.5 < BMI <= 25:
    print("Норма")
elif 25 > BMI <= 30:
    print("Избыточный вес")
elif 30 < BMI <= 40:
    print("Ожирение")
else:
  print("Неправильный ввод")

# Задача №6
#расчёт оценки по результатам теста
#программа принимает количество правильных ответов на тесте и общее количество вопросов. Рассчитывает процент правильных ответов и выводит оценку - менее 50% неудовлетворительно, от 50% до 70% удовлетворительно.

a = int(input("Введите количество правильных ответов: "))
b = int(input("Введите общее количество вопросов: "))
if (a / b) * 100 <=50:
    print("Неудовлетворительно")
elif 50 < (a / b) * 100 <= 70:
    print("Удовлетворительно")
else:
  print("Отлично")

#Задача #7
#Нужно отгадать пароль, чтобы спасти принцессу. Есть 3 подсказки. Первая цифра пароля делится на 4. Вторая цифра пароля чётная. Пароль должен быть больше 50 или меньше 100, но не равен 75.
#Используйте условные операторы if elif else, а также логические операторы для проверки всех условий.

# Запрашиваем у пользователя пароль
password = int(input("Введите пароль: "))

# Извлекаем первую и вторую цифры пароля
first_digit = password // 10  # Первая цифра
second_digit = password % 10  # Вторая цифра

# Проверяем условия
if first_digit % 4 == 0 and second_digit % 2 == 0 and (50 < password < 100) and password != 75:
    print("Пароль правильный! Принцесса спасена!")
else:
    print("Пароль неверный. Попробуйте снова.")
