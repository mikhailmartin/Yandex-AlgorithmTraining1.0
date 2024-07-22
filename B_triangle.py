"""
Ограничение времени - 1 секунда
Ограничение памяти - 64Mb
Ввод - стандартный ввод или input.txt
Вывод - стандартный вывод или output.txt

Даны три натуральных числа. Возможно ли построить треугольник с такими
сторонами. Если это возможно, выведите строку YES, иначе выведите строку NO.

Треугольник — это три точки, не лежащие на одной прямой.


Формат ввода:
Вводятся три натуральных числа.


Формат вывода:
Выведите ответ на задачу.


Пример 1
>>> 3
>>> 4
>>> 5
YES

Пример 2
>>> 3
>>> 5
>>> 4
YES

Пример 3
>>> 4
>>> 5
>>> 3
YES
"""
a, b, c = sorted(map(int, [input() for _ in range(3)]))

if a + b > c:
    answer = "YES"
else:
    answer = "NO"

print(answer)
