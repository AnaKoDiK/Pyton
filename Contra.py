lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
size = 3
result = [lst[i:i+size] for i in range(0, len(lst), size)]
#разбиение списка на подсписки
for i in range(1, len(result), 2):
    result[i] = result[i][::-1]
print(result)
