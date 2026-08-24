"""
Медиана объединения-2

Ограничение времени - 5 секунд
Ограничение памяти - 256Mb
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
Сначала вводятся числа N и L (2 ≤ N ≤ 200, 1 ≤ L ≤ 50_000). В следующих N
строках задаются параметры, определяющие последовательности.

Каждая последовательность определяется пятью целочисленными параметрами:
x_1, d_1, a, c, m. Элементы последовательности вычисляются по следующим формулам:
x_1 нам задано, а для всех i от 2 до L: x_i = x_{i–1} + d_{i–1}.
Последовательность d_i определяется следующим образом: d_1 нам задано,
а для i ≥ 2 d_i = ((a * d_{i–1} + c) mod m), где mod – операция получения
остатка от деления (a * d_{i–1} + c) на m.

Для всех последовательностей выполнены следующие ограничения: 1 ≤ m ≤ 40_000,
0 ≤ a < m, 0 ≤ c < m, 0 ≤ d_1 < m. Гарантируется, что все члены всех
последовательностей по модулю не превышают 10^9.


Формат вывода:
В первой строке выведите медиану объединения 1-й и 2-й последовательностей,
во второй строке — объединения 1-й и 3-й, и так далее, в (N‑1)-ой строке —
объединения 1-й и N-ой последовательностей, далее медиану объединения 2-й и 3-й,
2-й и 4-й, и т.д. до 2-й и N-ой, затем 3-й и 4-й и так далее. В последней строке
должна быть выведена медиана объединения (N–1)-й и N-ой последовательностей.


Примечания:
Последовательности, объединения которых мы считаем, таковы:
1 4 7 10 13 16
0 2 5 9 14 20
1 7 16 16 21 22


Пример:
input: 3 6
input: 1 3 1 0 5
input: 0 2 1 1 100
input: 1 6 8 5 11
output: 7
output: 10
output: 9
"""
from array import array
from dataclasses import dataclass
from typing import Self


@dataclass(frozen=True)
class ProblemInput:
    n: int
    l: int
    arrs: list[array]


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
    def arrs(self) -> list[array]:
        return self.data.arrs

    @classmethod
    def from_stdin(cls) -> Self:

        n, l = map(int, input().split())
        arrs = []
        for _ in range(n):
            x1, d1, a, c, m = list(map(int, input().split()))
            arr = array("i", [0] * l)
            arr[0] = x1
            d = d1
            for i in range(1, l):
                arr[i] = arr[i-1] + d
                d = (a * d + c) % m
            arrs.append(arr)

        return cls(ProblemInput(n, l, arrs))

    @classmethod
    def from_strings(cls, lines: list[str]) -> Self:

        n, l = map(int, lines[0].split())
        arrs = []
        for i in range(n):
            x1, d1, a, c, m = list(map(int, lines[i + 1].split()))
            arr = array("i", [0] * l)
            arr[0] = x1
            d = d1
            for j in range(1, l):
                arr[j] = arr[j-1] + d
                d = (a * d + c) % m
            arrs.append(arr)

        return cls(ProblemInput(n, l, arrs))

    def solve(self) -> list[int]:

        result = []
        for i in range(self.n):
            for j in range(i+1, self.n):
                median = self.left_median_of_union(self.arrs[i], self.arrs[j])
                result.append(median)

        return result

    def left_median_of_union(self, a_arr: array, b_arr: array) -> int:

        i = self.right_binary_search(lo=0, hi=self.l, check_params=(a_arr, b_arr))
        j = self.l - i

        a_left = a_arr[i - 1] if i > 0 else float("-inf")
        b_left = b_arr[j - 1] if j > 0 else float("-inf")

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

        a_arr, b_arr = check_params
        i = mid
        j = self.l - i

        a_left = a_arr[i-1] if i > 0 else float("-inf")
        b_right = b_arr[j] if j < self.l else float("+inf")

        return a_left <= b_right


def main() -> None:

    solver = Solver.from_stdin()
    result = solver.solve()

    for answer in result:
        print(answer)


if __name__ == "__main__":
    main()
