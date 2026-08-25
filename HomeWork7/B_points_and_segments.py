"""
Точки и отрезки

Ограничение времени - 3 секунды
Ограничение памяти - 256Mb
Ввод - стандартный ввод или input.txt
Вывод - стандартный вывод или output.txt

Дано n отрезков на числовой прямой и m точек на этой же прямой. Для каждой из
данных точек определите, скольким отрезкам они принадлежат. Точка x считается
принадлежащей отрезку с концами a и b, если выполняется двойное неравенство
min(a, b) ≤ x ≤ max(a, b).


Формат ввода:
Первая строка содержит два целых числа n (1 ≤ n ≤ 10^5) – число отрезков и
m (1 ≤ m ≤ 10^5) – число точек. В следующих n строках по два целых числа
a_i и b_i – координаты концов соответствующего отрезка. В последней строке
m целых чисел – координаты точек. Все числа по модулю не превосходят 10^9.


Формат вывода:
В выходной файл выведите m чисел – для каждой точки количество отрезков,
в которых она содержится.


Пример
input: 3 2
input: 0 5
input: -3 2
input: 7 10
input: 1 6
output: 2 0
"""
from dataclasses import dataclass
from enum import IntEnum
from typing import Self


class EventType(IntEnum):
    BEGIN = 0
    POINT = 1
    END = 2


@dataclass(frozen=True)
class ProblemInput:
    n: int
    m: int
    segments: list[tuple[int, int]]
    points: list[int]


class Solver:
    def __init__(self, data: ProblemInput) -> None:
        self.data = data

    @property
    def n(self) -> int:
        return self.data.n

    @property
    def m(self) -> int:
        return self.data.m

    @property
    def segments(self) -> list[tuple[int, int]]:
        return self.data.segments

    @property
    def points(self) -> list[int]:
        return self.data.points

    @classmethod
    def from_stdin(cls) -> Self:

        n, m = map(int, input().split())
        segments = []
        for _ in range(n):
            a, b = map(int, input().split())
            segments.append((a, b))
        points = list(map(int, input().split()))

        return cls(ProblemInput(n, m, segments, points))

    @classmethod
    def from_strings(cls, lines: list[str]) -> Self:

        n, m = map(int, lines[0].split())
        segments = []
        for i in range(n):
            a, b = map(int, lines[i+1].split())
            segments.append((a, b))
        points = list(map(int, lines[-1].split()))

        return cls(ProblemInput(n, m, segments, points))

    def solve(self) -> list[int]:

        events = []
        for a, b in self.segments:
            begin, end = min(a, b), max(a, b)
            events.append((begin, EventType.BEGIN))
            events.append((end, EventType.END))
        for i, point in enumerate(self.points):
            events.append((point, EventType.POINT, i))
        events.sort()

        count = 0
        result = [0] * self.m
        for event in events:
            event_type = event[1]
            if event_type == EventType.BEGIN:
                count += 1
            elif event_type == EventType.POINT:
                i = event[2]
                result[i] = count
            elif event_type == EventType.END:
                count -= 1

        return result


def main() -> None:

    solver = Solver.from_stdin()
    result = solver.solve()

    print(" ".join(map(str, result)))


if __name__ == "__main__":
    main()
