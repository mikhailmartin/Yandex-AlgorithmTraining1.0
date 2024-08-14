"""
Наибольшее произведение трёх чисел

Ограничение времени - 1 секунда
Ограничение памяти - 64Mb
Ввод - стандартный ввод или input.txt
Вывод - стандартный вывод или output.txt

В данном списке из n ≤ 10⁵ целых чисел найдите три числа, произведение которых
максимально.

Решение должно иметь сложность O(n), где n - размер списка. То есть сортировку
использовать нельзя.

Выведите три искомых числа в любом порядке.


Пример 1
input: 3 5 1 7 9 0 9 -3 10
output: 10 9 9

Пример 2
input: -5 -30000 -12
output: -5 -12 -30000

Пример 3
input: 1 2 3
output: 3 2 1
"""


def main(numbers: list[int]) -> tuple[int, int, int]:

    # инициализация
    max3, max2, max1 = sorted(numbers[:3])
    min1 = max3
    min2 = max2

    for number in numbers[3:]:

        if number >= max1:
            max3 = max2
            max2 = max1
            max1 = number
        elif number >= max2:
            max3 = max2
            max2 = number
        elif number > max3:
            max3 = number

        if number <= min1:
            min2 = min1
            min1 = number
        elif number < min2:
            min2 = number

    if min1 * min2 * max1 > max1 * max2 * max3:
        return min1, min2, max1
    else:
        return max1, max2, max3


if __name__ == "__main__":

    numbers = list(map(int, input().split()))
    num1, num2, num3 = main(numbers)
    print(num1, num2, num3)
