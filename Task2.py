# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

n = abs(int(input('Введите размер элементов списка: ')))
list_n = input('Введите элементы списка через пробел: ').split()
massiv = list(map(int, list_n))
if len(massiv) != n:
    print('Введенно неверное количество элементов!')
else:
    print(massiv)
    x = int(input('Введите число х: '))
    near = massiv[0]
    for i in massiv:
        if abs(x - i) < abs(x - near):
            near = i
    print(f'Ближайшее к {x} число в списке {near}')
