"""
Счёт в гипершашках

Ограничение времени - 1 секунда
Ограничение памяти - 64Mb
Ввод - стандартный ввод или input.txt
Вывод - стандартный вывод или output.txt

Андрей работает судьёй на чемпионате по гипершашкам. В каждой игре в гипершашки
участвует три игрока. По ходу игры каждый из игроков набирает некоторое
положительное целое число баллов. Если после окончания игры первый игрок набрал
a баллов, второй — b, а третий c, то говорят, что игра закончилась со счётом
a:b:c.

Андрей знает, что правила игры гипершашек устроены таким образом, что в
результате игры баллы любых двух игроков различаются не более чем в k раз.

После матча Андрей показывает его результат, размещая три карточки с очками
игроков на специальном табло. Для этого у него есть набор из n карточек, на
которых написаны числа x_1, x_2, …, x_n. Чтобы выяснить, насколько он готов к
чемпионату, Андрей хочет понять, сколько различных вариантов счёта он сможет
показать на табло, используя имеющиеся карточки.

Требуется написать программу, которая по числу k и значениям чисел на карточках,
которые имеются у Андрея, определяет количество различных вариантов счёта,
которые Андрей может показать на табло.


Формат ввода:
Первая строка входного файла содержит два целых числа: n и k
(3 ≤ n ≤ 100000, 1 ≤ k ≤ 10^9).

Вторая строка входного файла содержит n целых чисел x_1, x_2, …, x_n (1 ≤ x_i ≤ 10^9).


Формат вывода:
Выходной файл должен содержать одно целое число — искомое количество различных
вариантов счёта.


Пример
input: 5 2
input: 1 1 2 2 3
output: 9


Примечания:
В приведённом примере Андрей сможет показать следующие варианты счёта: 1:1:2,
1:2:1, 2:1:1, 1:2:2, 2:1:2, 2:2:1, 2:2:3, 2:3:2, 3:2:2. Другие тройки чисел,
которые можно составить с использованием имеющихся карточек, не удовлетворяют
заданному условию, что баллы любых двух игроков различаются не более чем в
k = 2 раза.
"""


def parse_input() -> tuple[int, int, list[int]]:

    n, k = map(int, input().split())
    numbers = list(map(int, input().split()))

    return n, k, numbers


def main(k: int, numbers: list[int]) -> int:

    number_counter = dict()
    for number in numbers:
        number_counter[number] = number_counter.get(number, 0) + 1
    unique_numbers = sorted(number_counter.keys())

    right_pointer = 0
    duplicates_counter = 0
    counter = 0
    for left_pointer in range(len(unique_numbers)):

        left_number = unique_numbers[left_pointer]

        # передвигаем правый указатель "до упора",
        # считая количество карточек, имеющих дубликаты
        while (
            right_pointer < len(unique_numbers)
            and unique_numbers[right_pointer] / unique_numbers[left_pointer] <= k
        ):
            right_number = unique_numbers[right_pointer]
            if number_counter[right_number] >= 2:
                duplicates_counter += 1
            right_pointer += 1

        # (a, a, a) -> 1
        if number_counter[left_number] >= 3:
            counter += 1

        # (a, a, b) -> 3
        distance = right_pointer - left_pointer
        if number_counter[left_number] >= 2:
            counter += (distance - 1) * 3
            duplicates_counter -= 1

        # (a, b, b) -> 3
        counter += duplicates_counter * 3

        # (a, b, c) -> 6
        counter += (distance - 1) * (distance - 2) * 3

    return counter


if __name__ == "__main__":

    n, k, numbers = parse_input()
    result = main(k, numbers)
    print(result)
