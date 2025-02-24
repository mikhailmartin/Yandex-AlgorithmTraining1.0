"""
Двоичный поиск

Ограничение времени - 1 секунда
Ограничение памяти - 64Mb
Ввод - стандартный ввод или input.txt
Вывод - стандартный вывод или output.txt

Реализуйте двоичный поиск в массиве.


Формат ввода:
В первой строке входных данных содержатся натуральные числа N и K (0 < N, K ≤ 100_000).
Во второй строке задаются N элементов первого массива, а в третьей строке –
K элементов второго массива. Элементы обоих массивов - целые числа, каждое из
которых по модулю не превосходит 10^9.


Формат вывода:
Требуется для каждого из K чисел вывести в отдельную строку "YES", если это
число встречается в первом массиве, и "NO" в противном случае.


Пример 1
input: 10 10
input: 1 61 126 217 2876 6127 39162 98126 712687 1000000000
input: 100 6127 1 61 200 -10000 1 217 10000 1000000000
output: NO
output: YES
output: YES
output: YES
output: NO
output: NO
output: YES
output: YES
output: NO
output: YES

Пример 2
input: 10 10
input: -8 -6 -4 -4 -2 -1 0 2 3 3
input: 8 3 -3 -2 2 -1 2 9 -8 0
output: NO
output: YES
output: NO
output: YES
output: YES
output: YES
output: YES
output: NO
output: YES
output: YES

Пример 3
input: 10 5
input: 1 2 3 4 5 6 7 8 9 10
input: -2 0 4 9 12
output: NO
output: NO
output: YES
output: YES
output: NO
"""


def parse_data() -> tuple[list, list]:

    n, k = map(int, input().split())
    list1 = list(map(int, input().split()))
    list2 = list(map(int, input().split()))

    return list1, list2


def main(list1: list, list2: list) -> list:

    left_pointer = 0
    right_pointer = len(list2)-1
    result = []
    for k in list2:
        pointer = left_binary_search(left_pointer, right_pointer, check_less, )

    return result


def left_binary_search(left_pointer: int, right_pointer: int, check, check_params):

    while left_pointer < right_pointer:
        center_pointer = (left_pointer + right_pointer) // 2
        if check(center_pointer, check_params):
            right_pointer = center_pointer
        else:
            left_pointer = center_pointer + 1

    return left_pointer


def check_less(pointer: int, list_: list, number: int) -> bool:
    return list_[pointer] <= number


if __name__ == "__main__":

    list1, list2 = parse_data()
    result = main(list1, list2)
    print(*result, sep="\n")
