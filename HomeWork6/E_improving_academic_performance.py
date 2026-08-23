"""
Улучшение успеваемости

Ограничение времени - 1 секунда
Ограничение памяти - 64Mb
Ввод - стандартный ввод или input.txt
Вывод - стандартный вывод или output.txt

В лицее на уроках информатики ответы учеников оцениваются целым числом баллов от
2 до 5. Итоговая оценка по информатике выставляется как среднее арифметическое
оценок на всех уроках, округленное до ближайшего целого числа. Если среднее
значение находится ровно посередине между двумя целыми числами, то оценка
округляется вверх.

Примеры округления оценок приведены в таблице.

Все ученики лицея стремятся получить итоговую оценку по информатике не ниже 4
баллов. К сожалению, один из учеников получил на уроках a двоек, b троек и c
четвёрок. Теперь он планирует получить несколько пятёрок, причём хочет, чтобы
итоговая оценка была не меньше 4 баллов. Ему надо понять, какое минимальное
количество пятёрок ему необходимо получить, чтобы добиться своей цели.

Требуется написать программу, которая по заданным целым неотрицательные числам
a, b и c определяет минимальное количество пятёрок, которое необходимо получить
ученику, чтобы его итоговая оценка по информатике была не меньше 4 баллов.


Формат ввода:
Входные данные содержат три строки. Первая строка содержит целое неотрицательное
число a, вторая строка содержит целое неотрицательное число b, третья строка
содержит целое неотрицательное число c (0 ≤ a, b, c ≤ 10^15, a + b + c ≥ 1).


Формат вывода:
Выходные данные должны содержать одно число: минимальное число пятёрок, которое
необходимо получить ученику, чтобы итоговая оценка была не меньше 4 баллов.


Пример 1
input: 2
input: 0
input: 0
output: 2
"""
from dataclasses import dataclass
from typing import Self


@dataclass(frozen=True)
class ProblemInput:
    twos: int
    threes: int
    fours: int


class Solver:
    def __init__(self, data: ProblemInput) -> None:
        self.data = data

    @property
    def twos(self) -> int:
        return self.data.twos

    @property
    def threes(self) -> int:
        return self.data.threes

    @property
    def fours(self) -> int:
        return self.data.fours

    @classmethod
    def from_stdin(cls) -> Self:

        a = int(input())
        b = int(input())
        c = int(input())

        return cls(ProblemInput(a, b, c))

    @classmethod
    def from_strings(cls, lines: list[str]) -> Self:

        a = int(lines[0])
        b = int(lines[1])
        c = int(lines[2])

        return cls(ProblemInput(a, b, c))

    def solve(self) -> int:

        amount = self.twos + self.threes + self.fours
        fives = self.left_binary_search(lo=0, hi=amount)

        return fives

    def left_binary_search(self, lo: int, hi: int) -> int:

        while lo < hi:
            mid = (lo + hi) // 2
            if self.check(mid):
                hi = mid
            else:
                lo = mid + 1

        return lo

    def check(self, fives: int) -> bool:
        amount = self.twos * 2 + self.threes * 3 + self.fours * 4 + fives * 5
        n = self.twos + self.threes + self.fours + fives
        return 2 * amount >= 7 * n


def main() -> None:

    solver = Solver.from_stdin()
    result = solver.solve()
    print(result)


if __name__ == "__main__":
    main()
