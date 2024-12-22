#Задача №1
#Дан список чисел. Напишите программу, которая разбивает этот список на группы, где каждая группа состоит из чисел, сумма которых не превышает
#определенное значение (например,10). Пример ввода numbers = [1, 3, 5, 7, 2, 4, 6, 8] max_sum = 10. Ожидаемый результат: [[1, 3, 5], [7, 2], [4, 6], [8]]

numbers = [1, 3, 5, 7, 2, 4, 6, 8]
max_sum = 10

groups = []
current_group = []
current_sum = 0
for num in numbers:
        # Если добавление числа не превышает max_sum, добавляем его в текущую группу
    if current_sum + num <= max_sum:
            current_group.append(num)
            current_sum += num
    else:
            # Иначе начинаем новую группу
            groups.append(current_group)
            current_group = [num]
            current_sum = num
    # Добавляем последнюю группу, если она не пуста
if current_group:
   groups.append(current_group)
print(groups)

#Задача №2
#Дан список и целое число k. Напишите программу, которая генерирует все возможные сочетания из k элементов данного списка. Пример ввода items = [1, 2, 3, 4] k = 2
#Ожидаемый результат [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)].
#Входные данные
items = [1, 2, 3, 4]
k = 2
# Генерация сочетаний с помощью циклов и генераторов
combinations_list = [
    (items[i], items[j])
    for i in range(len(items))
    for j in range(i + 1, len(items))
]
# Вывод результата
print(combinations_list)

