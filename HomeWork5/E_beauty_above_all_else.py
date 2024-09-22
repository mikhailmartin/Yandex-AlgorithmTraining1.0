"""
Красота превыше всего

Ограничение времени - 2 секунды
Ограничение памяти - 64Mb
Ввод - стандартный ввод или input.txt
Вывод - стандартный вывод или output.txt

В парке города Питсбурга есть чудесная аллея, состоящая из N посаженных в один
ряд деревьев, каждое одного из K сортов. В связи с тем, что Питсбург принимает
открытый чемпионат Байтландии по программированию, было решено построить
огромную арену для проведения соревнований. Так, согласно этому плану вся аллея
подлежала вырубке. Однако министерство деревьев и кустов воспротивилось этому
решению, и потребовало оставить некоторые из деревьев в покое. Согласно новому
плану строительства все деревья, которые не будут вырублены, должны образовывать
один непрерывный отрезок, являющийся подотрезком исходного. Каждого из K видов
деревьев требуется сохранить хотя бы по одному экземпляру. На вас возложена
задача найти отрезок наименьшей длины, удовлетворяющий указанным ограничениям.


Формат ввода:
В первой строке входного файла находятся два числа N и K (1 ≤ N, K ≤ 250000).
Во второй строке входного файла следуют N чисел (разделенных пробелами),
i-ое число второй строки задает цвет i-ого слева дерева в аллее. Гарантируется,
что присутствует хотя бы одно дерево каждого цвета.


Формат вывода:
В выходной файл выведите два числа, координаты левого и правого концов отрезка
минимальной длины, удовлетворяющего условию. Если оптимальных ответов несколько,
выведите любой.


Пример 1
input: 5 3
input: 1 2 1 3 2
output: 2 4

Пример 2
input: 6 4
input: 2 4 2 3 3 1
output: 2 6
"""


def main(n: int, k: int, trees: list[int]) -> tuple[int, int]:

    best_left_pointer = 0
    best_right_pointer = n-1
    tree_type_counter = ["tech"] + [0] * k
    unique_tree_type_counter = 0

    left_pointer = 0
    for right_pointer, tree_type in enumerate(trees):

        if tree_type_counter[tree_type] == 0:
            unique_tree_type_counter += 1
        tree_type_counter[tree_type] += 1

        if unique_tree_type_counter == k:
            while tree_type_counter[trees[left_pointer]] > 1:
                tree_type_counter[trees[left_pointer]] -= 1
                left_pointer += 1

            if best_right_pointer - best_left_pointer > right_pointer - left_pointer:
                best_left_pointer = left_pointer
                best_right_pointer = right_pointer

    return best_left_pointer+1, best_right_pointer+1


if __name__ == "__main__":

    n, k = map(int, input().split())
    trees = list(map(int, input().split()))

    left, right = main(n, k, trees)
    print(left, right)
