"""
Определить вид последовательности

Ограничение времени - 1 секунда
Ограничение памяти - 64Mb
Ввод - стандартный ввод или input.txt
Вывод - стандартный вывод или output.txt

По последовательности чисел во входных данных определите её вид:
* CONSTANT – последовательность состоит из одинаковых значений
* ASCENDING – последовательность является строго возрастающей
* WEAKLY ASCENDING – последовательность является нестрого возрастающей
* DESCENDING – последовательность является строго убывающей
* WEAKLY DESCENDING – последовательность является нестрого убывающей
* RANDOM – последовательность не принадлежит ни к одному из вышеупомянутых типов


Формат ввода:
По одному на строке поступают числа последовательности a_i, |a_i| ≤ 10^9.

Признаком окончания последовательности является число -2×10^9. Оно в
последовательность не входит.


Формат вывода:
В единственной строке выведите тип последовательности.


Пример
input: -530
input: -530
input: -530
input: -530
input: -530
input: -530
input: -2000000000
output: CONSTANT
"""
from typing import Literal


def get_sequence() -> list[int]:

    sequence = []
    while True:

        element = int(input())

        if element == -2_000_000_000:
            break
        else:
            sequence.append(element)

    return sequence


def identify_sequence_type(sequence: list) -> Literal[
    "CONSTANT",
    "ASCENDING",
    "WEAKLY ASCENDING",
    "DESCENDING",
    "WEAKLY DESCENDING",
    "RANDOM",
]:
    if not check_sequence(sequence):
        return "RANDOM"

    is_ascending = False
    is_descending = False
    is_constant = False

    for i in range(1, len(sequence)):

        previous = sequence[i-1]
        current = sequence[i]

        if previous < current:
            is_ascending = True
        elif previous == current:
            is_constant = True
        else:
            is_descending = True

    if not is_ascending and not is_descending and is_constant:
        sequence_type = "CONSTANT"
    elif is_ascending and not is_descending and not is_constant:
        sequence_type = "ASCENDING"
    elif is_ascending and not is_descending and is_constant:
        sequence_type = "WEAKLY ASCENDING"
    elif not is_ascending and is_descending and not is_constant:
        sequence_type = "DESCENDING"
    elif not is_ascending and is_descending and is_constant:
        sequence_type = "WEAKLY DESCENDING"
    else:
        sequence_type = "RANDOM"

    return sequence_type


def check_sequence(sequence: list) -> bool:

    if len(sequence) in [0, 1]:
        return False
    else:
        return True


if __name__ == "__main__":

    # sequence = get_sequence()
    sequence = [-530, -530, -530, -530, -530, -530]
    sequence_type = identify_sequence_type(sequence)
    print(sequence_type)
