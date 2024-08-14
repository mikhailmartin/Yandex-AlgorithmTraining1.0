"""
Симметричная последовательность

Ограничение времени - 1 секунда
Ограничение памяти - 64Mb
Ввод - стандартный ввод или input.txt
Вывод - стандартный вывод или output.txt

Последовательность чисел назовем симметричной, если она одинаково читается как
слева направо, так и справа налево. Например, следующие последовательности
являются симметричными:
1 2 3 4 5 4 3 2 1
1 2 1 2 2 1 2 1

Вашей программе будет дана последовательность чисел. Требуется определить,
какое минимальное количество и каких чисел надо приписать в конец этой
последовательности, чтобы она стала симметричной.


Формат ввода:
Сначала вводится число N — количество элементов исходной последовательности
(1 ≤ N ≤ 100). Далее идут N чисел — элементы этой последовательности,
натуральные числа от 1 до 9.


Формат вывода:
Выведите сначала число M — минимальное количество элементов, которое надо
дописать к последовательности, а потом M чисел (каждое — от 1 до 9) — числа,
которые надо дописать к последовательности.


Пример 1
input: 9
input: 1 2 3 4 5 4 3 2 1
output: 0

Пример 2
input: 5
input: 1 2 1 2 2
output: 3
output: 1 2 1

Пример 3
input: 5
input: 1 2 3 4 5
output: 4
output: 4 3 2 1
"""


def main(sequence: list[int]) -> tuple[int, str]:

    m = find_index_start_palindrome(sequence)
    missing = " ".join(map(str, reversed(sequence[:m])))

    return m, missing


def find_index_start_palindrome(sequence: list[int]) -> int:
    """
    Находит индекс начала палиндрома.

    """
    index_start_palindrome = 0
    symmetric_index = -1

    for index in range(len(sequence)):

        if sequence[index] != sequence[symmetric_index]:
            index_start_palindrome = index+1
            symmetric_index = -1  # сдвигаем индекс влево
        else:
            symmetric_index -= 1  # откатываем индекс на конец

    return index_start_palindrome


if __name__ == "__main__":

    n = int(input())
    sequence = list(map(int, input().split()))
    m, missing = main(sequence)

    print(m)
    if missing:
        print(missing)
