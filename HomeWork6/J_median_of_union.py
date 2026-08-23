"""
Медиана объединения

Ограничение времени - 1 секунда
Ограничение памяти - 64Mb
Ввод - стандартный ввод или input.txt
Вывод - стандартный вывод или output.txt

Дано N упорядоченных по неубыванию последовательностей целых чисел (т.е. каждый
следующий элемент больше либо равен предыдущему), в каждой из
последовательностей ровно L элементов. Для каждых двух последовательностей
выполняют следующую операцию: объединяют их элементы (в объединённой
последовательности каждое число будет идти столько раз, сколько раз оно
встречалось суммарно в объединяемых последовательностях), упорядочивают их по
неубыванию и смотрят, какой элемент в этой последовательности из 2L элементов
окажется на месте номер L (этот элемент называют левой медианой).

Напишите программу, которая для каждой пары последовательностей выведет левую
медиану их объединения.


Формат ввода:
Сначала вводятся числа N и L (2 ≤ N ≤ 100, 1 ≤ L ≤ 300). В следующих N строках
задаются последовательности. Каждая последовательность состоит из L чисел, по
модулю не превышающих 30_000.


Формат вывода:
В первой строке выведите медиану объединения 1-й и 2-й последовательностей,
во второй строке — объединения 1-й и 3-й, и так далее, в (N‑1)-ой строке —
объединения 1-й и N-ой последовательностей, далее медиану объединения 2-й и 3-й,
2-й и 4-й, и т.д. до 2-й и N-ой, затем 3-й и 4-й и так далее. В последней строке
должна быть выведена медиана объединения (N–1)-й и N-ой последовательностей.


Пример:
input: 3 6
input: 1 4 7 10 13 16
input: 0 2 5 9 14 20
input: 1 7 16 16 21 22
output: 7
output: 10
output: 9
"""
from dataclasses import dataclass
from typing import Self


@dataclass(frozen=True)
class ProblemInput:
    n: int
    l: int
    arrays: list[list[int]]


class Solver:
    def __init__(self, data: ProblemInput) -> None:
        self.data = data

    @property
    def n(self) -> int:
        return self.data.n

    @property
    def l(self) -> int:
        return self.data.l

    @property
    def arrays(self) -> list[list[int]]:
        return self.data.arrays

    @classmethod
    def from_stdin(cls) -> Self:

        n, l = map(int, input().split())
        arrays = []
        for _ in range(n):
            array = list(map(int, input().split()))
            arrays.append(array)

        return cls(ProblemInput(n, l, arrays))

    @classmethod
    def from_strings(cls, lines: list[str]) -> Self:

        n, l = map(int, lines[0].split())
        arrays = []
        for i in range(n):
            array = list(map(int, lines[i+1].split()))
            arrays.append(array)

        return cls(ProblemInput(n, l, arrays))

    def solve(self) -> list[int]:

        result = []
        for i in range(self.n):
            for j in range(i+1, self.n):
                median = self.left_median_of_union(self.arrays[i], self.arrays[j])
                result.append(median)

        return result

    def left_median_of_union(self, a_array: list[int], b_array: list[int]) -> int:

        i = self.right_binary_search(lo=0, hi=self.l, check_params=(a_array, b_array))
        j = self.l - i

        a_left = a_array[i-1] if i > 0 else float("-inf")
        b_left = b_array[j-1] if j > 0 else float("-inf")

        return max(a_left, b_left)

    def right_binary_search(self, lo: int, hi: int, check_params) -> int:

        while lo < hi:
            mid = (lo + hi + 1) // 2
            if self.check(mid, check_params):
                lo = mid
            else:
                hi = mid - 1

        return lo

    def check(self, mid: int, check_params) -> bool:

        a_array, b_array = check_params
        i = mid
        j = self.l - i

        a_left = a_array[i-1] if i > 0 else float("-inf")
        b_right = b_array[j] if j < self.l else float("+inf")

        return a_left <= b_right


def main() -> None:

    solver = Solver.from_stdin()
    result = solver.solve()

    for answer in result:
        print(answer)


if __name__ == "__main__":
    main()
