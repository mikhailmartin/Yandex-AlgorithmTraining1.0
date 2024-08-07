"""
Узник замка Иф

Ограничение времени - 1 секунда
Ограничение памяти - 64Mb
Ввод - стандартный ввод или input.txt
Вывод - стандартный вывод или output.txt

За многие годы заточения узник замка Иф проделал в стене прямоугольное
отверстие размером D × E. Замок Иф сложен из кирпичей, размером A × B × C.
Определите, сможет ли узник выбрасывать кирпичи в море через это отверстие,
если стороны кирпича должны быть параллельны сторонам отверстия.


Формат ввода:
Программа получает на вход числа A, B, C, D, E.


Формат вывода:
Программа должна вывести слово YES или NO.


Пример 1
input: 1
input: 1
input: 1
input: 1
input: 1
output: YES


Пример 2
input: 2
input: 2
input: 2
input: 1
input: 1
output: NO
"""


def main(a: int, b: int, c: int, d: int, e: int) -> str:

    # упорядочиваем размеры кирпича в порядке неубывания
    if a > b:
        a, b, c = b, a, c
    if b > c:
        a, b, c = a, c, b
    if a > b:
        a, b, c = b, a, c

    # упорядочимваем размеры отверстия
    if d > e:
        d, e = e, d

    # проверяем пролезет ли кирпич в дырку
    if (a <= d) and (b <= e):
        return "YES"
    else:
        return "NO"


if __name__ == "__main__":

    a, b, c, d, e = [int(input()) for _ in range(5)]
    answer = main(a, b, c, d, e)
    print(answer)
