"""
Кубики

Ограничение времени - 1 секунда
Ограничение памяти - 64Mb
Ввод - стандартный ввод или input.txt
Вывод - стандартный вывод или output.txt

Аня и Боря любят играть в разноцветные кубики, причём у каждого из них свой
набор и в каждом наборе все кубики различны по цвету. Однажды дети
заинтересовались, сколько существуют цветов таких, что кубики каждого цвета
присутствуют в обоих наборах. Для этого они занумеровали все цвета случайными
числами. На этом их энтузиазм иссяк, поэтому вам предлагается помочь им в
оставшейся части. Номер любого цвета — это целое число в пределах от 0 до 10^9.


Формат ввода:
В первой строке входного файла записаны числа N и M — количество кубиков у Ани
и Бори соответственно. В следующих N строках заданы номера цветов кубиков Ани.
В последних M строках номера цветов кубиков Бори.


Формат вывода:
Выведите сначала количество, а затем отсортированные по возрастанию номера
цветов таких, что кубики каждого цвета есть в обоих наборах, затем количество и
отсортированные по возрастанию номера остальных цветов у Ани, потом количество
и отсортированные по возрастанию номера остальных цветов у Бори.


Пример 1
input: 4 3
input: 0
input: 1
input: 10
input: 9
input: 1
input: 3
input: 0
output: 2
output: 0 1
output: 2
output: 9 10
output: 1
output: 3

Пример 2
input: 2 2
input: 1
input: 2
input: 2
input: 3
output: 1
output: 2
output: 1
output: 1
output: 1
output: 3

Пример 3
input: 0 0
input: 0
input: 0
input: 0
"""


def main(anyas: set[int], boryas: set[int]) -> tuple[set[int], set[int], set[int]]:

    intersection = anyas & boryas
    only_anyas = anyas - intersection
    only_boryas = boryas - intersection

    return intersection, only_anyas, only_boryas


if __name__ == "__main__":

    n, m = map(int, input().split())
    anyas = set([int(input()) for _ in range(n)])
    boryas = set([int(input()) for _ in range(m)])

    intersection, only_anyas, only_boryas = main(anyas, boryas)

    print(len(intersection))
    print(*sorted(intersection))

    print(len(only_anyas))
    print(*sorted(only_anyas))

    print(len(only_boryas))
    print(*sorted(only_boryas))
