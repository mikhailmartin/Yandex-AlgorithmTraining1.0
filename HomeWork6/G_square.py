"""
Площадь

Ограничение времени - 0.5 секунд
Ограничение памяти - 64Mb
Ввод - стандартный ввод или input.txt
Вывод - стандартный вывод или output.txt

Городская площадь имеет размер n×m и покрыта квадратной плиткой размером 1×1.
При плановой замене плитки выяснилось, что новой плитки недостаточно для
покрытия всей площади, поэтому было решено покрыть плиткой только дорожку по
краю площади, а в центре площади разбить прямоугольную клумбу (см. рисунок к
примеру). При этом дорожка должна иметь одинаковую ширину по всем сторонам
площади. Определите максимальную ширину дорожки, которую можно выложить из
имеющихся плиток.


Формат ввода:
Первая и вторая строки входных данных содержат по одному числу n и m
(3 ≤ n ≤ 2×10^9, 3 ≤ m ≤ 2× 10^9) — размеры площади. Третья строка содержит
количество имеющихся плиток t, 1 ≤ t < nm.


Формат вывода:
Программа должна вывести единственное число — максимальную ширину дорожки,
которую можно выложить из имеющихся плиток.


Примечания:
Пояснение к примеру. Площадь имеет размеры 6 × 7, из 38 плиток можно выложить
дорожку шириной в 2 плитки.


Пример 1
input: 6
input: 7
input: 38
output: 2
"""
from dataclasses import dataclass
from typing import Self


@dataclass(frozen=True)
class ProblemInput:
    n: int
    m: int
    t: int


class Solver:
    def __init__(self, data: ProblemInput) -> None:
        if data.n < data.m:
            self.min_size, self.max_size = data.n, data.m
        else:
            self.min_size, self.max_size = data.m, data.n
        self.t = data.t

    @classmethod
    def from_stdin(cls) -> Self:

        n = int(input())
        m = int(input())
        t = int(input())

        return cls(ProblemInput(n, m, t))

    @classmethod
    def from_strings(cls, lines: list[str]) -> Self:

        n = int(lines[0])
        m = int(lines[1])
        t = int(lines[2])

        return cls(ProblemInput(n, m, t))

    def solve(self) -> int:
        return self.right_binary_search(lo=0, hi=self.min_size // 2)

    def right_binary_search(self, lo: int, hi: int) -> int:

        while lo < hi:
            mid = (lo + hi + 1) // 2
            if self.check(mid):
                lo = mid
            else:
                hi = mid - 1

        return lo

    def check(self, width: int) -> bool:
        return self.tile_count(width) <= self.t

    def tile_count(self, width: int) -> int:
        """
        Считает количество плиток, которое необходимо для создания дорожки
        по краю площади
        """
        return 2 * width * (self.max_size + self.min_size - 2 * width)


def main() -> None:

    solver = Solver.from_stdin()
    result = solver.solve()

    print(result)


if __name__ == "__main__":
    main()
