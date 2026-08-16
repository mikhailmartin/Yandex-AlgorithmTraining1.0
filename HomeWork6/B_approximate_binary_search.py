"""
Приближенный двоичный поиск

Ограничение времени - 1 секунда
Ограничение памяти - 64Mb
Ввод - стандартный ввод или input.txt
Вывод - стандартный вывод или output.txt

Для каждого из чисел второй последовательности найдите ближайшее к нему в
первой.


Формат ввода:
В первой строке входных данных содержатся числа N и K (0 < N, K ≤ 100_001).
Во второй строке задаются N чисел первого массива, отсортированного по
неубыванию, а в третьей строке – K чисел второго массива. Каждое число в обоих
массивах по модулю не превосходит 2*10^9.


Формат вывода:
Для каждого из K чисел выведите в отдельную строку число из первого массива,
наиболее близкое к данному. Если таких несколько, выведите меньшее из них.


Пример 1
input: 5 5
input: 1 3 5 7 9
input: 2 4 8 1 6
output: 1
output: 3
output: 7
output: 1
output: 5

Пример 2
input: 6 11
input: 1 1 4 4 8 120
input: 1 2 3 4 5 6 7 8 63 64 65
output: 1
output: 1
output: 4
output: 4
output: 4
output: 4
output: 8
output: 8
output: 8
output: 8
output: 120

Пример 3
input: 10 10
input: -5 1 1 3 5 5 8 12 13 16
input: 0 3 7 -17 23 11 0 11 15 7
output: 1
output: 3
output: 8
output: -5
output: 16
output: 12
output: 1
output: 12
output: 16
output: 8
"""
from dataclasses import dataclass
from typing import Self


@dataclass
class ProblemInput:
    n: int
    k: int
    array1: list[int]
    array2: list[int]


class Solver:
    def __init__(self, data) -> None:
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
            left = self.left_binary_search(left=0, right=self.n - 1, check_param=num)

            if left == 0:
                result.append(self.array1[left])
            else:
                left_num = self.array1[left - 1]
                right_num = self.array1[left]

                if num - left_num <= right_num - num:
                    result.append(left_num)
                else:
                    result.append(right_num)

        return result

    def left_binary_search(self, left: int, right: int, check_param: int) -> int:

        while left < right:
            middle = (left + right) // 2
            if self.left_check(middle, check_param):
                right = middle
            else:
                left = middle + 1

        return left

    def left_check(self, pointer: int, check_param: int) -> bool:
        return self.array1[pointer] >= check_param


def main() -> None:

    solver = Solver.from_stdin()
    result = solver.solve()

    for answer in result:
        print(answer)

if __name__ == "__main__":
    main()
