"""
Рассадка в аудитории

Ограничение времени - 1 секунда
Ограничение памяти - 64Mb
Ввод - стандартный ввод или input.txt
Вывод - стандартный вывод или output.txt

Экзамен по берляндскому языку проходит в узкой и длинной аудитории. На экзамен
пришло N студентов. Все они посажены в ряд. Таким образом, позиция каждого
человека задаётся координатой на оси Ox (эта ось ведёт вдоль длинной аудитории).
Два человека могут разговаривать, если расстояние между ними меньше или равно D.
Какое наименьшее количество типов билетов должен подготовить преподаватель,
чтобы никакие два студента с одинаковыми билетами не могли разговаривать?
Выведите способ раздачи преподавателем билетов.


Формат ввода:
В первой строке входного файла содержится два целых числа N, D (1 ≤ N ≤ 10000; 0 ≤ D ≤ 10^6).
Вторая строка содержит последовательность различных целых чисел X_1, X_2, ..., X_N,
где X_i (0 ≤ X_i ≤ 10^6) обозначает координату вдоль оси Ox i-го студента.


Формат вывода:
В первую строчку выходного файла выведите количество вариантов, а во вторую,
разделяя пробелами, номера вариантов студентов в том порядке, в каком они
перечислены во входном файле.


Пример 1
input: 4 1
input: 11 1 12 2
output: 2
output: 1 1 2 2

Пример 2
input: 4 0
input: 11 1 12 2
output: 1
output: 1 1 1 1
"""
from collections import deque
from dataclasses import dataclass
from enum import IntEnum
from typing import Self


class EventType(IntEnum):
    BEGIN = 0
    END = 1


@dataclass
class ProblemInput:
    n: int
    d: int
    students: list[int]


class Solver:
    def __init__(self, data: ProblemInput) -> None:
        self.data = data

    @classmethod
    def from_stdin(cls) -> Self:

        n, d = map(int, input().split())
        students = list(map(int, input().split()))

        return cls(ProblemInput(n, d, students))

    @classmethod
    def from_strings(cls, lines: list[str]) -> Self:

        n, d = map(int, lines[0].split())
        students = list(map(int, lines[1].split()))

        return cls(ProblemInput(n, d, students))

    def solve(self) -> tuple[int, list[int]]:

        events = []
        for i, student in enumerate(self.data.students):
            events.append((student, EventType.BEGIN, i))
            events.append((student + self.data.d, EventType.END, i))
        events.sort()

        available = deque()
        result = [0] * self.data.n
        next_variant = 1
        for _, event_type, i in events:
            if event_type == EventType.BEGIN:
                if not available:
                    available.append(next_variant)
                    next_variant += 1
                result[i] = available.popleft()
            elif event_type == EventType.END:
                available.append(result[i])

        return max(result), result


def main() -> None:

    solver = Solver.from_stdin()
    result = solver.solve()

    print(result[0])
    print(" ".join(map(str, result[1])))


if __name__ == "__main__":
    main()
