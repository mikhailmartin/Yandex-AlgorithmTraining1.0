"""
Космическое поселение

Ограничение времени - 1 секунда
Ограничение памяти - 64Mb
Ввод - стандартный ввод или input.txt
Вывод - стандартный вывод или output.txt

Для освоения Марса требуется построить исследовательскую базу. База должна
состоять из n одинаковых модулей, каждый из которых представляет собой
прямоугольник.

Каждый модуль представляет собой жилой отсек, который имеет форму прямоугольника
размером a на b метров. Для повышения надёжности модулей инженеры могут добавить
вокруг каждого модуля слой дополнительной защиты. Толщина этого слоя должна
составлять целое число метров, и все модули должны иметь одинаковую толщину
дополнительной защиты. Модуль с защитой, толщина которой равна d метрам, будет
иметь форму прямоугольника размером (a+2d)(b+2d) метров.

Все модули должны быть расположены на заранее подготовленном прямоугольном поле
размером wh метров. При этом они должны быть организованы в виде регулярной
сетки: их стороны должны быть параллельны сторонам поля, и модули должны быть
ориентированы одинаково.

Требуется написать программу, которая по заданным количеству и размеру модулей,
а также размеру поля для их размещения, определяет максимальную толщину слоя
дополнительной защиты, который можно добавить к каждому модулю.


Формат ввода:
Входной файл содержит пять разделённых пробелами целых чисел: n, a, b, w и h
(1 ≤ n, a, b, w, h ≤ 1018). Гарантируется, что без дополнительной защиты все
модули можно разместить в поселении описанным образом.


Формат вывода:
Выходной файл должен содержать одно целое число: максимальную возможную толщину
дополнительной защиты. Если дополнительную защиту установить не удастся,
требуется вывести число 0.


Примечания:
Для входных данных 11 3 2 21 25 можно установить дополнительную защиту толщиной
2 метра и разместить модули на поле, как показано на рисунке.


Пример 1
input: 1 1 1 1 1
output: 0

Пример 2
input: 1 1 1 3 3
output: 1
"""
from dataclasses import dataclass
from typing import Self


@dataclass(frozen=True)
class ProblemInput:
    n: int
    a: int
    b: int
    w: int
    h: int


class Solver:
    def __init__(self, data: ProblemInput) -> None:
        self.data = data

    @property
    def n(self) -> int:
        return self.data.n

    @property
    def module_size1(self) -> int:
        return self.data.a

    @property
    def module_size2(self) -> int:
        return self.data.b

    @property
    def area_width(self) -> int:
        return self.data.w

    @property
    def area_height(self) -> int:
        return self.data.h

    @classmethod
    def from_stdin(cls) -> Self:
        n, a, b, w, h = map(int, input().split())
        return cls(ProblemInput(n, a, b, w, h))

    @classmethod
    def from_strings(cls, lines: list[str]) -> Self:
        n, a, b, w, h = map(int, lines[0].split())
        return cls(ProblemInput(n, a, b, w, h))

    def solve(self) -> int:

        max_protection1 = (self.area_width - self.module_size1) // 2
        max_protection2 = (self.area_width - self.module_size2) // 2
        max_protection = max(max_protection1, max_protection2)

        protection = self.right_binary_search(left=0, right=max_protection)

        return protection

    def right_binary_search(self, left: int, right: int) -> int:

        while left < right:
            middle = (left + right + 1) // 2
            if self.check(middle):
                left = middle
            else:
                right = middle - 1

        return left

    def check(self, protection: int) -> bool:

        # обычная ориентация
        n_row = self.area_width // (self.module_size1 + 2 * protection)
        n_col = self.area_height // (self.module_size2 + 2 * protection)
        n1 = n_row * n_col

        # повёрнутая на 90 градусов
        n_row = self.area_width // (self.module_size2 + 2 * protection)
        n_col = self.area_height // (self.module_size1 + 2 * protection)
        n2 = n_row * n_col

        return self.n <= n1 or self.n <= n2


def main() -> None:

    solver = Solver.from_stdin()
    result = solver.solve()

    print(result)


if __name__ == "__main__":
    main()
