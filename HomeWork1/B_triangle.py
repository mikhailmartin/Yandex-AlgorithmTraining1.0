"""
Треугольник

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
input: 3
input: 4
input: 5
output: YES

Пример 2
input: 3
input: 5
input: 4
output: YES

Пример 3
input: 4
input: 5
input: 3
output: YES
"""
from typing import Literal


def main(a:int, b: int, c: int) -> Literal["YES", "NO"]:

    if a + b > c:
        answer = "YES"
    else:
        answer = "NO"

    return answer


if __name__ == "__main__":

    a, b, c = sorted(map(int, [input() for _ in range(3)]))
    answer = main(a, b, c)
    print(answer)
