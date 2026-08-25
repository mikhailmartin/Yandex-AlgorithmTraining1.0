"""
Наблюдение за студентами

Ограничение времени - 1 секунда
Ограничение памяти - 64Mb
Ввод - стандартный ввод или input.txt
Вывод - стандартный вывод или output.txt

На первом курсе одной Школы, учится 1 ≤ N ≤ 10^9 студентов. При проведении
экзаменов студентов рассаживают в ряд, каждого за своей партой. Парты
пронумерованы числами от 0 до N−1.

Известно, что студент, оставшись без наблюдения, открывает телефон и начинает
искать ответы на экзамен в поисковике Яндекса.

Поэтому было решено позвать M преподавателей наблюдать за студентами. Когда за
студентом наблюдает хотя бы один преподаватель, он стесняется и не идёт искать
ответы к экзамену. Преподаватель с номером i видит студентов, сидящих за партами
от b_i до e_i включительно.

Необходимо посчитать количество студентов, которые всё таки будут искать ответы
к экзамену в Яндексе.


Формат ввода:
В первой строке находятся два целых числа 1 ≤ N ≤ 10^9, 1 ≤ M ≤ 10^4 — число
студентов и число преподавателей соответственно. В следующих M строках
содержится по два целых числа 0 ≤ b_i ≤ e_i ≤ N−1 — парты, за которыми наблюдает
i-й преподаватель.


Формат вывода:
Выведите одно число — количество студентов оставшихся без наблюдения.


Пример 1
input: 10 3
input: 1 3
input: 2 4
input: 9 9
output: 5

Пример 2
input: 10 2
input: 1 1
input: 1 2
output: 8
"""
from dataclasses import dataclass
from typing import Self


@dataclass(frozen=True)
class ProblemInput:
    n: int
    m: int
    intervals: list[tuple[int, int]]


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
    def intervals(self) -> list[tuple[int, int]]:
        return self.data.intervals

    @classmethod
    def from_stdin(cls) -> Self:

        n, m = map(int, input().split())
        intervals = []
        for _ in range(m):
            b, e = map(int, input().split())
            intervals.append((b, e))

        return cls(ProblemInput(n, m, intervals))

    @classmethod
    def from_strings(cls, lines: list[str]) -> Self:

        n, m = map(int, lines[0].split())
        intervals = []
        for i in range(m):
            b, e = map(int, lines[i+1].split())
            intervals.append((b, e))

        return cls(ProblemInput(n, m, intervals))

    def solve(self) -> int:

        events = []
        for begin, end in self.intervals:
            events.append((begin, 1))
            events.append((end + 1, -1))
        events.sort()

        supervised = 0
        supervisors = 0
        prev_pos = 0

        i = 0
        n_events = len(events)
        while i < n_events:
            curr_pos = events[i][0]

            if supervisors > 0:
                supervised += curr_pos - prev_pos

            while i < n_events and events[i][0] == curr_pos:
                supervisors += events[i][1]
                i += 1

            prev_pos = curr_pos

        return self.n - supervised


def main() -> None:

    solver = Solver.from_stdin()
    result = solver.solve()

    print(result)


if __name__ == "__main__":
    main()
