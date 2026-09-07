"""
Охрана

Ограничение времени - 4 секунды
Ограничение памяти - 64Mb
Ввод - стандартный ввод или input.txt
Вывод - стандартный вывод или output.txt

На секретной военной базе работает N охранников. Сутки поделены на 10000 равных
промежутков времени, и известно когда каждый из охранников приходит на дежурство
и уходит с него. Например, если охранник приходит в 5, а уходит в 8, то значит,
что он был в 6, 7 и 8-ой промежуток (а в 5-й нет!!!).

Укажите, верно ли что для данного набора охранников, объект охраняется в любой
момент времени хотя бы одним охранником и удаление любого из них приводит к
появлению промежутка времени, когда объект не охраняется.


Формат ввода:
В первой строке входного файла записано натуральное число K (1 ≤ K ≤ 100)
— количество тестов в файле. Каждый тест начинается с числа N (1 ≤ N ≤ 10000),
за которым следует N пар неотрицательных целых чисел A и B — время прихода на
дежурство и ухода (0 ≤ A ≤ B ≤ 10000) соответствующего охранника.


Формат вывода:
Выведите K строк, где в M-ой строке находится слово Accepted, если M-ый набор
охранников удовлетворяет описанным выше условиям. В противном случае выведите
Wrong Answer.


Пример
input: 2
input: 3 0 3000 2500 7000 2700 10000
input: 2 0 3000 2700 10000
output: Wrong Answer
output: Accepted
"""
import sys
from dataclasses import dataclass
from enum import IntEnum
from typing import Literal, Self, Iterator


class EventType(IntEnum):
    IN = 0
    OUT = 1


@dataclass
class ProblemInput:
    k: int
    tests_iterator: Iterator[tuple[int, list[tuple[int, int]]]]


class Solver:
    def __init__(self, data: ProblemInput) -> None:
        self.data = data

    @classmethod
    def from_stdin(cls) -> Self:
        # Генератор токенов: читает stdin ПОСТРОЧНО,
        # поэтому в памяти только одна строка за раз
        def token_generator():
            for line in sys.stdin:
                for token in line.split():
                    yield token

        tokens = token_generator()
        k = int(next(tokens))

        def create_tests_iterator():
            for _ in range(k):
                n = int(next(tokens))
                guards = []
                for _ in range(n):
                    a = int(next(tokens))
                    b = int(next(tokens))
                    guards.append((a, b))
                yield (n, guards)

        return cls(ProblemInput(k, create_tests_iterator()))

    @classmethod
    def from_strings(cls, lines: list[str]) -> Self:
        k = int(lines[0])

        def read_tests():
            for j in range(k):
                test = list(map(int, lines[j + 1].split()))
                n = test[0]
                guards = []
                for i in range(n):
                    guards.append((test[1 + i * 2], test[1 + i * 2 + 1]))
                yield (n, guards)

        return cls(ProblemInput(k, read_tests()))

    def solve(self) -> list[Literal["Accepted", "Wrong Answer"]]:

        result = []
        for test in self.data.tests_iterator:
            answer = self._check(test)
            result.append(answer)

        return result

    @staticmethod
    def _check(test: tuple[int, list[tuple[int, int]]]) -> Literal["Accepted", "Wrong Answer"]:

        n, guards = test

        events = []
        for idx, (time_in, time_out) in enumerate(guards):
            events.append((time_in, EventType.IN, idx))
            events.append((time_out, EventType.OUT, idx))
        events.sort()

        good_seq = set()
        now_seq = set()
        good_flag = True
        prev_time = -1
        for time, event_type, idx in events:
            if time != 0 and len(now_seq) == 0:
                good_flag = False
                break

            if len(now_seq) == 1 and time != prev_time:
                good_seq.update(now_seq)

            if event_type == EventType.IN:
                now_seq.add(idx)
            elif event_type == EventType.OUT:
                now_seq.remove(idx)

            prev_time = time

        if events[-1][0] != 10000:
            good_flag = False

        if good_flag and len(good_seq) == n:
            return "Accepted"
        else:
            return "Wrong Answer"


def main() -> None:

    solver = Solver.from_stdin()
    result = solver.solve()

    for answer in result:
        print(answer)


if __name__ == "__main__":
    main()
