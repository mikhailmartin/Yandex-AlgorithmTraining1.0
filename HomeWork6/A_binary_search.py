"""
Двоичный поиск

Ограничение времени - 1 секунда
Ограничение памяти - 64Mb
Ввод - стандартный ввод или input.txt
Вывод - стандартный вывод или output.txt

Реализуйте двоичный поиск в массиве.


Формат ввода:
В первой строке входных данных содержатся натуральные числа N и K (0 < N, K ≤ 100_000).
Во второй строке задаются N элементов первого массива, а в третьей строке –
K элементов второго массива. Элементы обоих массивов - целые числа, каждое из
которых по модулю не превосходит 10^9.


Формат вывода:
Требуется для каждого из K чисел вывести в отдельную строку "YES", если это
число встречается в первом массиве, и "NO" в противном случае.


Пример 1
input: 10 10
input: 1 61 126 217 2876 6127 39162 98126 712687 1000000000
input: 100 6127 1 61 200 -10000 1 217 10000 1000000000
output: NO
output: YES
output: YES
output: YES
output: NO
output: NO
output: YES
output: YES
output: NO
output: YES

Пример 2
input: 10 10
input: -8 -6 -4 -4 -2 -1 0 2 3 3
input: 8 3 -3 -2 2 -1 2 9 -8 0
output: NO
output: YES
output: NO
output: YES
output: YES
output: YES
output: YES
output: NO
output: YES
output: YES

Пример 3
input: 10 5
input: 1 2 3 4 5 6 7 8 9 10
input: -2 0 4 9 12
output: NO
output: NO
output: YES
output: YES
output: NO
"""
from dataclasses import dataclass
from typing import Self


@dataclass(frozen=True)
class ProblemInput:
    n: int
    k: int
    array1: list[int]
    array2: list[int]


class Solver:
    def __init__(self, data: ProblemInput) -> None:
        self.data = data

    @property
    def n(self) -> int:
        return self.data.n

    @property
    def array1(self) -> list[int]:
        return self.data.array1

    @property
    def array2(self) -> list[int]:
        return self.data.array2

    @classmethod
    def from_stdin(cls) -> Self:

        n, k = map(int, input().split())
        array1 = list(map(int, input().split()))
        array2 = list(map(int, input().split()))

        return cls(ProblemInput(n, k, array1, array2))

    @classmethod
    def from_strings(cls, lines: list[str]) -> Self:

        n, k = map(int, lines[0].split())
        array1 = list(map(int, lines[1].split()))
        array2 = list(map(int, lines[2].split()))

        return cls(ProblemInput(n, k, array1, array2))

    def solve(self) -> list:

        result = []
        for num in self.array2:
            index = self.left_binary_search(left=0, right=self.n - 1, check_param=num)
            if num == self.array1[index]:
                result.append("YES")
            else:
                result.append("NO")

        return result

    def left_binary_search(self, left: int, right: int, check_param: int) -> int:

        while left < right:
            middle = (left + right) // 2
            if self.check(middle, check_param):
                right = middle
            else:
                left = middle + 1

        return left

    def check(self, pointer: int, check_param: int) -> bool:
        return self.array1[pointer] >= check_param


def main() -> None:

    solver = Solver.from_stdin()
    result = solver.solve()

    for answer in result:
        print(answer)


if __name__ == "__main__":
    main()
