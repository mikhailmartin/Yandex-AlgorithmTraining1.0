"""
Треугольники

Ограничение времени - 4 секунды
Ограничение памяти - 256Mb
Ввод - стандартный ввод или input.txt
Вывод - стандартный вывод или output.txt

Петя достаточно давно занимается в математическом кружке, поэтому он уже успел
не только правила выполнения простейших операций, но и такое достаточно сложное
понятие как симметрия. Для того, чтобы получше изучить симметрию Петя решил
начать с наиболее простых геометрических фигур – треугольников. Он скоро понял,
что осевой симметрией обладают так называемые равнобедренные треугольники.
Поэтому теперь Петя ищет везде такие треугольники.

Напомним, что треугольник называется равнобедренным, если его площадь
положительна, и у него есть хотя бы две равные стороны.

Недавно Петя, зайдя в класс, увидел, что на доске нарисовано n точек.
Разумеется, он сразу задумался, сколько существует троек из этих точек, которые
являются вершинами равнобедренных треугольников.

Требуется написать программу, решающую указанную задачу.


Формат ввода:
Входной файл содержит целое число n (3 ≤ n ≤ 1500). Каждая из последующих строк
содержит по два целых числа – x_i и y_i – координаты i-ой точки. Координаты
точек не превосходят 10^9 по абсолютной величине. Среди заданных точек нет
совпадающих.


Формат вывода:
В выходной файл выведите ответ на задачу.


Пример 1
input: 3
input: 0 0
input: 2 2
input: -2 2
output: 1

Пример 2
input: 4
input: 0 0
input: 1 1
input: 1 0
input: 0 1
output: 4
"""


def parse_data() -> list[tuple[int, int]]:

    n = int(input())
    points = [tuple(map(int, input().split())) for _ in range(n)]

    return points


def main(points: list[tuple[int, int]]) -> int:

    result = 0
    for core_point in points:

        distances = []
        symmetrics = set()
        for other_point in points:
            distance = get_distance(core_point, other_point)
            distances.append(distance)

            # проверка на вырожденный треугольник
            if other_point in symmetrics:
                result -= 1

            symmetric = get_symmetric(other_point, core_point)
            symmetrics.add(symmetric)
        distances.sort()

        right_pointer = 0
        for left_pointer in range(len(distances)):
            while (
                right_pointer < len(distances)
                and distances[left_pointer] == distances[right_pointer]
            ):
                right_pointer += 1
            result += right_pointer - left_pointer - 1

    return result


def get_distance(point1: tuple[int, int], point2: tuple[int, int]) -> int:
    return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5


def get_symmetric(point: tuple[int, int], center: tuple[int, int]) -> tuple[int, int]:
    dx = center[0] - point[0]
    dy = center[1] - point[1]
    return point[0] + 2 * dx, point[1] + 2 * dy


if __name__ == "__main__":

    points = parse_data()
    result = main(points)
    print(result)
