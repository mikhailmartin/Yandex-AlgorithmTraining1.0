"""
Стильная одежда

Ограничение времени - 1 секунда
Ограничение памяти - 64Mb
Ввод - стандартный ввод или input.txt
Вывод - стандартный вывод или output.txt

Глеб обожает шоппинг. Как-то раз он загорелся идеей подобрать себе майку и
штаны так, чтобы выглядеть в них максимально стильно. В понимании Глеба
стильность одежды тем больше, чем меньше разница в цвете элементов его одежды.

В наличии имеется N (1 ≤ N ≤ 100 000) маек и M (1 ≤ M ≤ 100 000) штанов, про
каждый элемент известен его цвет (целое число от 1 до 10 000 000). Помогите
Глебу выбрать одну майку и одни штаны так, чтобы разница в их цвете была как
можно меньше.


Формат ввода:
Сначала вводится информация о майках: в первой строке целое число N
(1 ≤ N ≤ 100 000) и во второй N целых чисел от 1 до 10 000 000 — цвета имеющихся
в наличии маек. Гарантируется, что номера цветов идут в возрастающем порядке
(в частности, цвета никаких двух маек не совпадают).

Далее в том же формате идёт описание штанов: их количество M (1 ≤ M ≤ 100 000)
и в следующей строке M целых чисел от 1 до 10 000 000 в возрастающем порядке —
цвета штанов.


Формат вывода:
Выведите пару неотрицательных чисел — цвет майки и цвет штанов, которые следует
выбрать Глебу. Если вариантов выбора несколько, выведите любой из них.


Пример 1
input: 2
input: 3 4
input: 3
input: 1 2 3
output: 3 3

Пример 2
input: 2
input: 4 5
input: 3
input: 1 2 3
output: 4 3

Пример 3
input: 5
input: 1 2 3 4 5
input: 5
input: 1 2 3 4 5
output: 1 1
"""


def main(n: int, shirts: list[int], m: int, pants: list[int]) -> tuple[int, int]:

    i = j = 0
    i_best = j_best = 0
    style_best = abs(shirts[i] - pants[j])

    while i < n and j < m:

        style = abs(shirts[i] - pants[j])

        if style < style_best:

            i_best = i
            j_best = j
            style_best = style

            if style_best == 0:
                break

        if shirts[i] < pants[j]:
            i += 1
        else:
            j += 1

    return shirts[i_best], pants[j_best]


if __name__ == "__main__":

    n = int(input())
    shirts = list(map(int, input().split()))
    m = int(input())
    pants = list(map(int, input().split()))

    result = main(n, shirts, m, pants)
    print(*result)
