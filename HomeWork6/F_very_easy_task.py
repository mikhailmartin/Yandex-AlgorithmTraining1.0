"""
Очень лёгкая задача

Ограничение времени - 1 секунда
Ограничение памяти - 64Mb
Ввод - стандартный ввод или input.txt
Вывод - стандартный вывод или output.txt

Сегодня утром жюри решило добавить в вариант олимпиады ещё одну, Очень Лёгкую
Задачу. Ответственный секретарь Оргкомитета напечатал её условие в одном
экземпляре, и теперь ему нужно до начала олимпиады успеть сделать ещё N копий.
В его распоряжении имеются два ксерокса, один из которых копирует лист за х
секунд, а другой – за y. (Разрешается использовать как один ксерокс, так и оба
одновременно. Можно копировать не только с оригинала, но и с копии.) Помогите
ему выяснить, какое минимальное время для этого потребуется.


Формат ввода:
На вход программы поступают три натуральных числа N, x и y, разделённые пробелом
(1 ≤ N ≤ 2 × 10^8, 1 ≤ x, y ≤ 10).


Формат вывода:
Выведите одно число – минимальное время в секундах, необходимое для получения N копий.


Пример 1
input: 4 1 1
output: 3

Пример 2
input: 5 1 2
output: 4
"""
from dataclasses import dataclass
from typing import Self


@dataclass(frozen=True)
class ProblemInput:
    n: int
    speed1: int
    speed2: int


class Solver:
    def __init__(self, data: ProblemInput) -> None:
        self.n = data.n
        if data.speed1 < data.speed2:
            self.fast, self.slow = data.speed1, data.speed2
        else:
            self.fast, self.slow = data.speed2, data.speed1

    @classmethod
    def from_stdin(cls) -> Self:
        n, x, y = map(int, input().split())
        return cls(ProblemInput(n, x, y))

    @classmethod
    def from_strings(cls, lines: list[str]) -> Self:
        n, x, y = map(int, lines[0].split())
        return cls(ProblemInput(n, x, y))

    def solve(self) -> int:
        time = self.left_binary_search(left=self.fast, right=self.n * self.slow)
        return time

    def left_binary_search(self, left: int, right: int) -> int:

        while left < right:
            middle = (left + right) // 2
            if self.check(middle):
                right = middle
            else:
                left = middle + 1

        return left

    def check(self, time: int) -> bool:
        # первую копию делаем всегда на быстром ксероксе
        time -= self.fast  # осталось времени
        n = self.n - 1  # осталось сделать копий

        f = time // self.fast  # успеем сделать f копий на быстром принтере
        s = time // self.slow  # успеем сделать s копий на медленном принтере

        return n <= f + s


def main() -> None:

    # solver = Solver.from_stdin()
    solver = Solver.from_strings(["34854 4 3"])
    result = solver.solve()

    print(result)


if __name__ == "__main__":
    main()
