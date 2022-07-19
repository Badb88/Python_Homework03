# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

print()
def operOne(arr):
    for i in range(len(arr)):
        arr[i] = int(round(arr[i] - int(arr[i]), 2) * 100)
    return arr

def operTwo(arr2):
    max = arr2[0]
    min = arr2[0]
    for i in range(len(arr2)):
        if arr2[i] != 0:
            if arr2[i] > max:
                max = arr2[i]
            elif arr2[i] < min:
                min = arr2[i]
    return (max-min)/100

a = [1.1, 1.2, 3.1, 5, 10.01]
print(f'В списке вещественных чисел {a}, разница между максимальным \nи минимальным значением дробной части элементов = {operTwo(operOne(a))}')