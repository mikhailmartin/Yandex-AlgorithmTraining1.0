"""
Уравнение с корнем

Ограничение времени - 1 секунда
Ограничение памяти - 64Mb
Ввод - стандартный ввод или input.txt
Вывод - стандартный вывод или output.txt

Решите в целых числах уравнение:
sqrt(ax + b) = c,
a, b, c – данные целые числа: найдите все решения или сообщите, что решений в
целых числах нет.


Формат ввода:
Вводятся три числа a, b и c по одному в строке.


Формат вывода:
Программа должна вывести все решения уравнения в порядке возрастания, либо
NO SOLUTION (заглавными буквами), если решений нет. Если решений бесконечно
много, вывести MANY SOLUTIONS.


Пример 1
input: 1
input: 0
input: 0
output: 0

Пример 2
input: 1
input: 2
input: 3
output: 7

Пример 3
input: 1
input: 2
input: -3
output: NO SOLUTION
"""
if __name__ == "__main__":

    a = int(input())
    b = int(input())
    c = int(input())

    if c < 0:
        x = "NO SOLUTION"
    elif a == 0:
        if b == (c ** 2):
            x = "MANY SOLUTIONS"
        else:
            x = "NO SOLUTION"
    else:
        x = (c ** 2 - b) / a
        if (x % 1) == 0:
            x = int(x)
        else:
            x = "NO SOLUTION"

    print(x)
