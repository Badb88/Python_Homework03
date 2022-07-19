# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

print()
# def prodOfNum(arr):
#     lenRes = 0
#     if len(arr) % 2 == 0:
#         lenRes = len(arr) // 2
#     else:
#         lenRes = len(arr) // 2 + 1
#     list = []
#     for i in range(0, lenRes):
#         list.append(arr[i] * arr[(len(arr) - 1) - i])
#     if len(arr) % 2 !=0:
#         list.append(arr[len(arr) // 2])
#     return list

# a = [2, 3, 4, 5, 6]
# print(prodOfNum(a))

def s(a):
    listq=[]
    lenRes = len(a) // 2
    for i in range(lenRes):
        listq.append(a[i] * a[(len(a) - 1) - i])
    if len(a) % 2 == 1:
        listq.append(a[len(a) // 2])
    return listq
ad = [2, 3, 4, 5, 6]
print(s(ad))
