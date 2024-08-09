"""
Ближайшее число

Ограничение времени - 1 секунда
Ограничение памяти - 64Mb
Ввод - стандартный ввод или input.txt
Вывод - стандартный вывод или output.txt

Напишите программу, которая находит в массиве элемент, самый близкий по
величине к данному числу.


Формат ввода:
В первой строке задается одно натуральное число N, не превосходящее 1000
– размер массива. Во второй строке содержатся N чисел – элементы массива (целые
числа, не превосходящие по модулю 1000). В третьей строке вводится одно целое
число x, не превосходящее по модулю 1000.


Формат вывода:
Вывести значение элемента массива, ближайшее к x. Если таких чисел несколько,
выведите любое из них.


Пример 1
input: 5
input: 1 2 3 4 5
input: 6
output: 5

Пример 2
input: 5
input: 5 4 3 2 1
input: 3
output: 3
"""


def get_input_data() -> tuple[list[int], int]:

    n = int(input())
    lst = list(map(int, input().split()))
    x = int(input())

    return lst, x


def find_nearest_number(lst: list[int], x: int) -> int:

    nearest_number = lst[0]
    nearest_dist = abs(x - nearest_number)

    for element in lst[1:]:

        current_dist = abs(x - element)

        if current_dist < nearest_dist:
            nearest_number = element
            nearest_dist = current_dist

    return nearest_number


if __name__ == "__main__":

    lst, x = get_input_data()
    nearest_number = find_nearest_number(lst, x)
    print(nearest_number)
