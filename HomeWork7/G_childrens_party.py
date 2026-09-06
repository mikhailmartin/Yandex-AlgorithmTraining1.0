"""
Детский праздник

Ограничение времени - 1 секунда
Ограничение памяти - 64Mb
Ввод - стандартный ввод или input.txt
Вывод - стандартный вывод или output.txt

Организаторы детского праздника планируют надуть для него M воздушных шариков.
С этой целью они пригласили N добровольных помощников, i-й среди которых
надувает шарик за T_i минут, однако каждый раз после надувания Z_i шариков
устаёт и отдыхает Y_i минут. Теперь организаторы праздника хотят узнать, через
какое время будут надуты все шарики при наиболее оптимальной работе помощников,
и сколько шариков надует каждый из них. (Если помощник надул шарик, и должен
отдохнуть, но больше шариков ему надувать не придётся, то считается, что он
закончил работу сразу после окончания надувания последнего шарика, а не после
отдыха).


Формат ввода:
В первой строке входных данных задаются числа M и N (0 ≤ M ≤ 15000, 1 ≤ N ≤ 1000).
Следующие N строк содержат по три целых числа - T_i, Z_i и Y_i соответственно
(1 ≤ T_i, Y_i ≤ 100, 1 ≤ Z_i ≤ 1000).


Формат вывода:
Выведите в первой строке число T - время, за которое будут надуты все шарики.
Во второй строке выведите N чисел - количество шариков, надутых каждым из
приглашённых помощников. Разделяйте числа пробелами. Если распределений шариков
несколько, выведите любое из них.


Пример 1
input: 1 2
input: 2 1 1
input: 1 1 2
output: 1
output: 0 1

Пример 2
input: 2 2
input: 1 1 1
input: 1 1 1
output: 1
output: 1 1
"""
import bisect
from collections import deque
from dataclasses import dataclass
from enum import IntEnum
from typing import Self


class EventType(IntEnum):
    READY = 0
    RESTED = 1


@dataclass
class ProblemInput:
    m: int
    n: int
    helpers: list[tuple[int, int, int]]


class Solver:
    def __init__(self, data: ProblemInput) -> None:
        self.data = data

    @property
    def helpers(self) -> list[tuple[int, int, int]]:
        return self.data.helpers

    @classmethod
    def from_stdin(cls) -> Self:

        m, n = map(int, input().split())
        helpers = []
        for _ in range(n):
            t, z, y = map(int, input().split())
            helpers.append((t, z, y))

        return cls(ProblemInput(m, n, helpers))

    @classmethod
    def from_strings(cls, lines: list[str]) -> Self:

        m, n = map(int, lines[0].split())
        helpers = []
        for i in range(n):
            t, z, y = map(int, lines[i+1].split())
            helpers.append((t, z, y))

        return cls(ProblemInput(m, n, helpers))

    def solve(self):

        if self.data.m == 0:
            return 0, [0] * self.data.n

        events = []
        for idx, (t, z, y) in enumerate(self.helpers):
            events.append((t, EventType.READY, idx))
        events.sort()
        events = deque(events)

        total = 0
        counter = [0] * self.data.n
        while events:
            time, event_type, idx = events.popleft()
            if event_type == EventType.READY:
                total += 1
                counter[idx] += 1

                if total == self.data.m:
                    break

                t, z, y = self.helpers[idx]
                if counter[idx] % z == 0:
                    bisect.insort(events, (time + y, EventType.RESTED, idx))
                else:
                    bisect.insort(events, (time + t, EventType.READY, idx))

            elif event_type == EventType.RESTED:
                t, z, y = self.helpers[idx]
                bisect.insort(events, (time + t, EventType.READY, idx))

        return time, counter


def main() -> None:

    solver = Solver.from_stdin()
    result = solver.solve()

    print(result[0])
    print(*result[1])


if __name__ == "__main__":
    main()
