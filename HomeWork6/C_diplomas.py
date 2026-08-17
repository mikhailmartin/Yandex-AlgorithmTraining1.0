"""
Дипломы

Ограничение времени - 1 секунда
Ограничение памяти - 64Mb
Ввод - стандартный ввод или input.txt
Вывод - стандартный вывод или output.txt

Когда Петя учился в школе, он часто участвовал в олимпиадах по информатике,
математике и физике. Так как он был достаточно способным мальчиком и усердно
учился, то на многих из этих олимпиад он получал дипломы. К окончанию школы у
него накопилось n дипломов, причём, как оказалось, все они имели одинаковые
размеры: w — в ширину и h — в высоту. Сейчас Петя учится в одном из лучших
российских университетов и живёт в общежитии со своими одногруппниками. Он решил
украсить свою комнату, повесив на одну из стен свои дипломы за школьные
олимпиады. Так как к бетонной стене прикрепить дипломы достаточно трудно, то он
решил купить специальную доску из пробкового дерева, чтобы прикрепить её к
стене, а к ней — дипломы. Для того чтобы эта конструкция выглядела более
красиво, Петя хочет, чтобы доска была квадратной и занимала как можно меньше
места на стене. Каждый диплом должен быть размещён строго в прямоугольнике
размером w на h. Дипломы запрещается поворачивать на 90 градусов.
Прямоугольники, соответствующие различным дипломам, не должны иметь общих
внутренних точек. Требуется написать программу, которая вычислит минимальный
размер стороны доски, которая потребуется Пете для размещения всех своих
дипломов.


Формат ввода:
Входной файл содержит три целых числа: w, h, n (1 ≤ w, h, n ≤ 10^9).


Формат вывода:
В выходной файл необходимо вывести ответ на поставленную задачу.


Пример
input: 2 3 10
output: 9
"""
from dataclasses import dataclass
from typing import Self


@dataclass
class ProblemInput:
    w: int
    h: int
    n: int


class Solver:
    def __init__(self, data: ProblemInput) -> None:
        self.data = data

    @property
    def w(self) -> int:
        return self.data.w

    @property
    def h(self) -> int:
        return self.data.h

    @property
    def n(self) -> int:
        return self.data.n

    @classmethod
    def from_stdin(cls) -> Self:
        w, h, n = map(int, input().split())
        return cls(ProblemInput(w, h, n))

    @classmethod
    def from_strings(cls, lines: list[str]) -> Self:
        w, h, n = map(int, lines[0].split())
        return cls(ProblemInput(w, h, n))

    def solve(self) -> int:

        min_width = self.w
        max_width = self.w * self.n
        min_height = self.h
        max_height = self.h * self.n

        min_size = max(min_width, min_height)
        max_size = max(max_width, max_height)

        size = self.left_binary_search(left=min_size, right=max_size)

        return size

    def left_binary_search(self, left: int, right: int) -> int:

        while left < right:
            middle = (left + right) // 2
            if self.check(middle):
                right = middle
            else:
                left = middle + 1

        return left

    def check(self, size: int) -> bool:

        n_row = size // self.w
        n_col = size // self.h

        return self.n <= n_row * n_col


def main() -> None:

    solver = Solver.from_stdin()
    result = solver.solve()

    print(result)


if __name__ == "__main__":
    main()
