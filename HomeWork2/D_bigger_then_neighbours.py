"""
Больше своих соседей

Ограничение времени - 1 секунда
Ограничение памяти - 64Mb
Ввод - стандартный ввод или input.txt
Вывод - стандартный вывод или output.txt


Дан список чисел. Определите, сколько в этом списке элементов, которые больше
двух своих соседей и выведите количество таких элементов.


Формат ввода:
Вводится список чисел. Все числа списка находятся на одной строке.


Формат вывода:
Выведите ответ на задачу.


Пример 1
input: 1 2 3 4 5
output: 0

Пример 2
input: 5 4 3 2 1
output: 0

Пример 3
input: 1 5 1 5 1
output: 2
"""


def count_bigger_then_neighbours(lst: list[int]) -> int:

    count = 0
    for i in range(1, len(lst)-1):
        previous = lst[i-1]
        current = lst[i]
        next = lst[i+1]

        if current > previous and current > next:
            count += 1

    return count


if __name__ == "__main__":

    lst = list(map(int, input().split()))
    count = count_bigger_then_neighbours(lst)
    print(count)
