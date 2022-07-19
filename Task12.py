# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

print()
def binNum(n):
    res = str("")
    while n != 0:
        res += str(n % 2)
        n //= 2
    return ''.join(reversed(res))

num = int(input('Введите число: '))
print(f'Число {num} в двоичной системе выглядит так: {bin(num)}')