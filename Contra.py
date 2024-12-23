lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
size = 3
#разбиение списка на подсписки
result = [lst[i:i+size] for i in range(0, len(lst), size)]
#переворот чётных подписков
for i in range(1, len(result), 2):
    result[i] = result[i][::-1]
print(result)


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
n = len(lst)
size = n // 3
#разбиение списка на подсписки
result = [lst[i:i+size] for i in range(0, n, size)]
#переворот чётных подписков
for i in range(1, len(result), 2):
    result[i] = result[i][::-1]
print(result)