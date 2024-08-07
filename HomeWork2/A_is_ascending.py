"""
Возрастает ли список?

Ограничение времени - 1 секунда
Ограничение памяти - 64Mb
Ввод - стандартный ввод или input.txt
Вывод - стандартный вывод или output.txt

Дан список. Определите, является ли он монотонно возрастающим(то есть верно ли,
что каждый элемент этого списка больше предыдущего).

Выведите YES, если массив монотонно возрастает и NO в противном случае.


Пример 1
input: 1 7 9
output: YES

Пример 2
input: 1 9 7
output: NO

Пример 3
input: 2 2 2
output: NO
"""
from typing import Literal


def is_ascending(lst: list) -> Literal["YES", "NO"]:

    i = 1
    while i < len(lst) and lst[i - 1] < lst[i]:
        i += 1

    return "YES" if i == len(lst) else "NO"


if __name__ == "__main__":

    lst = list(map(int, input().split()))
    print(is_ascending(lst))
