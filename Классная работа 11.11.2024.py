#Задача #1
#Таблица умножения с ограничением
#напишите программу, которая выводит таблицу умножения для числа, которое вводит пользователь. Выводите результаты по одному и завершайте цикл while, если произведение больше 50.
#Добавьте break, чтобы завершить цикл если произведение больше 50.

# Ввод числа от пользователя
num = int(input("Введите число для таблицы умножения: "))

# Начинаем цикл с умножения на 1
i = 1

# Используем цикл while для вывода таблицы умножения
while True:
    result = num * i
    print(f"{num} * {i} = {result}")

    # Проверяем, если произведение больше 50
    if result > 50:
        break  # Завершаем цикл, если произведение больше 50

    # Увеличиваем i для следующего умножения
    i += 1

#Задача #2
#Числовой ряд с пропусками
#напишите программу, которая выводит числа от 1 до 50, но пропускает числа, которые делятся на 3, с помощью continue. Если число делится на 7, программа завершает цикл с помощью break.

# Начальное значение
i = 1

# Цикл while для чисел от 1 до 50
while i <= 50:
    if i % 3 == 0:
        i += 1  # Увеличиваем i, чтобы пропустить текущее число
        continue  # Пропускаем числа, которые делятся на 3
    if i % 7 == 0:
        break  # Завершаем цикл, если число делится на 7
    print(i)  # Выводим число
    i += 1  # Увеличиваем i на 1

#Задача #3
#Банковский счёт
#напишите программу на python самыми простыми командами и с помощью цикла while для имитации банковского счёта, который начинается с 1000 единиц.
#Пользователь может снимать деньги с помощью команды "снять" и указывать сумму. Если на счёте не хватает денег для снятия, программа выводит сообщение об ошибке и переходит к следующей итерации с помощью continue.
#Если баланс стал отрицательным, цикл завершается с помощью break. Проверяйте текущий баланс перед каждым снятием.

# Начальный баланс на счете
balance = 1000

# Цикл продолжается, пока баланс не станет отрицательным
while True:
    # Запрашиваем команду у пользователя
    command = input("Введите команду (снять <сумма> или 'выход' для завершения): ").strip().lower()

    if command == "выход":
        print("Выход из программы.")
        break  # Завершаем программу

    # Если команда начинается с "снять"
    if command.startswith("снять"):
        try:
            # Извлекаем сумму из команды
            amount = float(command.split()[1])

            # Проверка, хватает ли денег на счете
            if amount > balance:
                print("Ошибка: недостаточно средств для снятия.")
                continue  # Переходим к следующей итерации цикла

            # Снимаем деньги с баланса
            balance -= amount
            print(f"Вы сняли {amount} единиц. Текущий баланс: {balance} единиц.")

            # Если баланс стал отрицательным, завершаем цикл
            if balance < 0:
                print("Баланс стал отрицательным. Программа завершена.")
                break  # Выход из цикла

        except (IndexError, ValueError):
            print("Ошибка: введите команду в правильном формате, например 'снять 100'.")

    else:
        print("Неверная команда. Попробуйте еще раз.")

#Задача #4
#Сумма чисел, кратных 5
#Пользователь вводит число, состоящее из пяти чисел. Проверить каждое число, является ли оно кратно 5, если да, посчитать сумму этих чисел.

# Запрашиваем у пользователя ввод числа
number = int(input("Введите число из пяти цифр: "))

# Инициализируем переменные
sum_of_multiples_of_5 = 0
count = 0  # Счётчик цифр

# Проверяем, что число состоит из 5 цифр
if number < 10000 or number > 99999:
    print("Ошибка: число должно состоять из 5 цифр.")
else:
    # Цикл while для перебора каждой цифры числа
    while number > 0:
        digit = number % 10  # Получаем последнюю цифру
        if digit % 5 == 0:  # Проверяем, кратна ли цифра 5
            sum_of_multiples_of_5 += digit  # Добавляем к сумме

        number = number // 10  # Убираем последнюю цифру
        count += 1  # Увеличиваем счётчик

    # Печатаем результат
    print("Сумма цифр, кратных 5:", sum_of_multiples_of_5)

#Задача №6
#Простой магазин с остатком средств
#В данной задаче есть система клиентов, каждый клиент может обслуживаться отдельно и есть возможность переключаться между клиентами. Обслуженный клиент выходит из очереди, а новый встаёт в неё.
#Допустим изначально у вас 5 клиентов. У пользователя есть сумма денег, например, 1000. Программа в цикле предлагает купить товары по разным ценам: 150 за хлеб, 250 за молоко, 300 за мясо.
#Пользователь вводит товара (1 - хлеб, 2 - молоко, 3 - мясо), а программа вычитает стоимость товара из его баланса и выводит остаток. Если денег не хватает, программа сообщает об этом и
#предлагает выбрать другой товар. Цикл завершается если у пользователя кончаются деньги.

# Начальный баланс для 5 клиентов
client1_balance = 1000
client2_balance = 1000
client3_balance = 1000
client4_balance = 1000
client5_balance = 1000

# Цены на товары
bread_price = 150
milk_price = 250
meat_price = 300

# Переменная для отслеживания, какой клиент сейчас на очереди
current_client = 1

# Цикл обслуживания клиентов
while current_client <= 5:
    # Выбираем баланс текущего клиента
    if current_client == 1:
        balance = client1_balance
    elif current_client == 2:
        balance = client2_balance
    elif current_client == 3:
        balance = client3_balance
    elif current_client == 4:
        balance = client4_balance
    elif current_client == 5:
        balance = client5_balance

    print(f"\nОбслуживание клиента {current_client}. Баланс: {balance} единиц.")

    # Пока у клиента есть деньги, он может совершать покупки
    while balance > 0:
        # Печатаем доступные товары
        print("Доступные товары:")
        print(f"1 - Хлеб ({bread_price} единиц)")
        print(f"2 - Молоко ({milk_price} единиц)")
        print(f"3 - Мясо ({meat_price} единиц)")

        # Запрос на выбор товара
        choice = input("Выберите товар (1 - хлеб, 2 - молоко, 3 - мясо) или 'выход' для завершения: ").strip()

        if choice == "1":
            if balance >= bread_price:
                balance -= bread_price
                print(f"Вы купили хлеб за {bread_price} единиц. Остаток: {balance} единиц.")
            else:
                print("Недостаточно средств для покупки хлеба.")
        elif choice == "2":
            if balance >= milk_price:
                balance -= milk_price
                print(f"Вы купили молоко за {milk_price} единиц. Остаток: {balance} единиц.")
            else:
                print("Недостаточно средств для покупки молока.")
        elif choice == "3":
            if balance >= meat_price:
                balance -= meat_price
                print(f"Вы купили мясо за {meat_price} единиц. Остаток: {balance} единиц.")
            else:
                print("Недостаточно средств для покупки мяса.")
        elif choice == "выход":
            print(f"Клиент {current_client} завершил покупки и покидает очередь.")
            break  # Клиент покидает очередь
        else:
            print("Неверный выбор. Попробуйте снова.")

    # Обновляем баланс клиента
    if current_client == 1:
        client1_balance = balance
    elif current_client == 2:
        client2_balance = balance
    elif current_client == 3:
        client3_balance = balance
    elif current_client == 4:
        client4_balance = balance
    elif current_client == 5:
        client5_balance = balance

    # Переходим к следующему клиенту
    current_client += 1

print("\nВсе клиенты обслужены.")





