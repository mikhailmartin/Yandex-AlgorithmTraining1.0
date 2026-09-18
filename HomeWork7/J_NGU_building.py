"""
НГУ-стройка

Ограничение времени - 4 секунды
Ограничение памяти - 64Mb
Ввод - стандартный ввод или input.txt
Вывод - стандартный вывод или output.txt

Над ареной огромного спортивного комплекса Независимого Главного Университета
(НГУ) решили построить перекрытие. Перекрытие будет построено по клеевой
технологии и состоять из склеенных друг с другом блоков. Блок представляет собой
лёгкий прямоугольный параллелепипед. Два блока можно склеить, если они
соприкасаются перекрывающимися частями боковых граней ненулевой площади.

НГУ представил план комплекса, имеющий вид прямоугольника размером W на L. При
этом один из углов прямоугольника находится в начале системы координат, а другой
имеет координаты (W, L). Стены комплекса параллельны осям координат.

Подрядчики известили НГУ, что они готовы к определённому сроку изготовить блоки
и установить их. Для каждого блока фиксировано место его возможного монтажа,
совпадающее по размерам с этим блоком. Места выбраны так, что рёбра блоков
параллельны осям координат. Места монтажа блоков не пересекаются.

По техническим условиям перекрытие должно состоять из такого набора склеенных
блоков, который содержит сплошной горизонтальный слой ненулевой толщины.
Торопясь ввести комплекс в эксплуатацию, НГУ решил построить перекрытие из
минимально возможного числа блоков.

Требуется написать программу, которая позволяет выбрать минимальное число
блоков, которые, будучи установленными на указанных подрядчиками местах,
образуют перекрытие, либо определить, что этого сделать невозможно. Высота, на
которой образуется перекрытие, не имеет значения.


Формат ввода:
В первой строке входного файла указаны три целых числа: N — количество возможных
блоков (1 ≤ N ≤ 10^5) и размеры комплекса W и L (1 ≤ W, L ≤ 10^4). Каждая из
последующих N строк описывает место монтажа одного блока, определяемое
координатами противоположных углов: (x_1, y_1, z_1) и (x_2, y_2, z_2), при этом
0 ≤ x_1 < x_2 ≤ W, 0 ≤ y_1 < y_2 ≤ L, 0 ≤ z_1 < z_2 ≤ 10^9. Все числа во входном
файле целые и разделяются пробелами или переводами строк.

Гарантируется, что места установки блоков не пересекаются друг с другом.


Формат вывода:
Первая строка выходного файла должна содержать либо слово «YES», если перекрытие
возможно построить, иначе — слово «NO». В первом случае вторая строка выходного
файла должна содержать минимальное число блоков, образующих перекрытие, а
последующие строки — номера этих блоков, в соответствии с порядком, в котором
они перечислены во входном файле.

Если возможно несколько минимальных наборов блоков, выведите любой из них.


Пример 1
input: 1 10 10
input: 0 0 0 10 10 10
output: YES
output: 1
output: 1

Пример 2
input: 2 10 10
input: 0 0 0 10 5 5
input: 0 5 5 10 10 10
output: NO
"""
from dataclasses import dataclass
from enum import IntEnum
from typing import Self


class EventType(IntEnum):
    OUT = 0
    IN = 1


@dataclass
class ProblemInput:
    n: int
    w: int
    l: int
    blocks: list[tuple[int, int, int, int, int, int]]


class Solver:
    def __init__(self, data: ProblemInput) -> None:
        self.data = data

    @classmethod
    def from_stdin(cls) -> Self:
        n, w, l = map(int, input().split())
        blocks = []
        for _ in range(n):
            x1, y1, z1, x2, y2, z2 = map(int, input().split())
            blocks.append((x1, y1, z1, x2, y2, z2))
        return cls(ProblemInput(n, w, l, blocks))

    @classmethod
    def from_strings(cls, lines: list[str]) -> Self:
        n, w, l = map(int, lines[0].split())
        blocks = []
        for i in range(n):
            x1, y1, z1, x2, y2, z2 = map(int, lines[i+1].split())
            blocks.append((x1, y1, z1, x2, y2, z2))
        return cls(ProblemInput(n, w, l, blocks))

    def solve(self) -> list[int]:

        events = []
        for i, (x1, y1, z1, x2, y2, z2) in enumerate(self.data.blocks, 1):
            area = (x2 - x1) * (y2 - y1)
            events.append((z1, EventType.IN, area, i))
            events.append((z2, EventType.OUT, area, i))
        events.sort()

        # за первый проход выясняем, существует ли решение
        total_area = self.data.w * self.data.l
        curr_area = 0
        success = False
        count = 0
        min_count = 10 ** 5 + 1
        for z, event_type, area, i in events:
            if event_type == EventType.IN:
                curr_area += area
                count += 1
                if curr_area == total_area:
                    success = True
                    min_count = min(min_count, count)
            elif event_type == EventType.OUT:
                curr_area -= area
                count -= 1

        if not success:
            return []

        # за второй проход ищем набор блоков
        curr_area = 0
        count = 0
        blocks = set()
        for z, event_type, area, i in events:
            if event_type == EventType.IN:
                curr_area += area
                count += 1
                blocks.add(i)
                if curr_area == total_area and count == min_count:
                    break
            elif event_type == EventType.OUT:
                curr_area -= area
                count -= 1
                blocks.remove(i)

        return sorted(blocks)


def main() -> None:

    solver = Solver.from_stdin()
    result = solver.solve()

    n = len(result)
    if n == 0:
        print("NO")
    else:
        print("YES")
        print(n)
        print("\n".join(map(str, result)))


if __name__ == "__main__":
    main()
