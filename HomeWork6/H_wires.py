"""
Провода

Ограничение времени - 1 секунда
Ограничение памяти - 64Mb
Ввод - стандартный ввод или input.txt
Вывод - стандартный вывод или output.txt

Дано N отрезков провода длиной L_1, L_2, ..., L_N сантиметров. Требуется с
помощью разрезания получить из них K равных отрезков как можно большей длины,
выражающейся целым числом сантиметров. Если нельзя получить K отрезков длиной
даже 1 см, вывести 0.


Формат ввода:
В первой строке находятся числа N и К. В следующих N строках - L_1, L_2, ..., L_N,
по одному числу в строке.

Ограничения: 1 ≤ N, K ≤ 10 000, 100 ≤ L_i ≤ 10 000 000, все числа целые.


Формат вывода:
Вывести одно число - полученную длину отрезков.


Пример:
input: 4 11
input: 802
input: 743
input: 457
input: 539
output: 200
"""
from dataclasses import dataclass
from typing import Self


@dataclass(frozen=True)
class ProblemInput:
    n: int
    k: int
    array: list[int]


class Solver:
    def __init__(self, data: ProblemInput) -> None:
        self.data = data

    @property
    def wires(self) -> list[int]:
        return self.data.array

    @property
    def k(self) -> int:
        return self.data.k

    @classmethod
    def from_stdin(cls) -> Self:

        n, k = map(int, input().split())
        array = []
        for _ in range(n):
            array.append(int(input()))

        return cls(ProblemInput(n, k, array))

    @classmethod
    def from_strings(cls, lines: list[str]) -> Self:

        n, k = map(int, lines[0].split())
        array = []
        for i in range(n):
            array.append(int(lines[i+1]))

        return cls(ProblemInput(n, k, array))

    def solve(self) -> int:

        if not self.check(1):
            return 0

        return self.right_binary_search(left=1, right=max(self.wires))

    def right_binary_search(self, left: int, right: int) -> int:

        while left < right:
            middle = (left + right + 1) // 2
            if self.check(middle):
                left = middle
            else:
                right = middle - 1

        return left

    def check(self, length: int) -> bool:

        count = 0
        for wire in self.wires:
            count += wire // length

        return count >= self.k


def main() -> None:

    solver = Solver.from_stdin()
    result = solver.solve()

    print(result)


if __name__ == "__main__":
    main()
