"""
Родословная: подсчет уровней

Ограничение времени - 1 секунда
Ограничение памяти - 64Mb
Ввод - стандартный ввод или input.txt
Вывод - стандартный вывод или output.txt

В генеалогическом древе у каждого человека, кроме родоначальника, есть ровно
один родитель. Каждому элементу дерева сопоставляется целое неотрицательное
число, называемое высотой. У родоначальника высота равна 0, у любого другого
элемента высота на 1 больше, чем у его родителя. Вам дано генеалогическое древо,
определите высоту всех его элементов.


Формат ввода:
Программа получает на вход число элементов в генеалогическом древе N. Далее
следует N−1 строка, задающие родителя для каждого элемента древа, кроме
родоначальника. Каждая строка имеет вид имя_потомка имя_родителя.


Формат вывода:
Программа должна вывести список всех элементов древа в лексикографическом
порядке. После вывода имени каждого элемента необходимо вывести его высоту.


Пример 1
input: 9
input: Alexei Peter_I
input: Anna Peter_I
input: Elizabeth Peter_I
input: Peter_II Alexei
input: Peter_III Anna
input: Paul_I Peter_III
input: Alexander_I Paul_I
input: Nicholaus_I Paul_I
output: Alexander_I 4
output: Alexei 1
output: Anna 1
output: Elizabeth 1
output: Nicholaus_I 4
output: Paul_I 3
output: Peter_I 0
output: Peter_II 2
output: Peter_III 2

Пример 2
input: 10
input: AQHFYP MKFXCLZBT
input: AYKOTYQ QIUKGHWCDC
input: IWCGKHMFM WPLHJL
input: MJVAURUDN QIUKGHWCDC
input: MKFXCLZBT IWCGKHMFM
input: PUTRIPYHNQ UQNGAXNP
input: QIUKGHWCDC WPLHJL
input: UQNGAXNP WPLHJL
input: YURTPJNR QIUKGHWCDC
output: AQHFYP 3
output: AYKOTYQ 2
output: IWCGKHMFM 1
output: MJVAURUDN 2
output: MKFXCLZBT 2
output: PUTRIPYHNQ 2
output: QIUKGHWCDC 1
output: UQNGAXNP 1
output: WPLHJL 0
output: YURTPJNR 2

Пример 3
input: 10
input: BFNRMLH CSZMPFXBZ
input: CSZMPFXBZ IHWBQDJ
input: FMVQTU FUXATQUGIG
input: FUXATQUGIG IRVAVMQKN
input: GNVIZ IQGIGUJZ
input: IHWBQDJ LACXYFQHSQ
input: IQGIGUJZ JMUPNYRQD
input: IRVAVMQKN GNVIZ
input: JMUPNYRQD BFNRMLH
output: BFNRMLH 3
output: CSZMPFXBZ 2
output: FMVQTU 9
output: FUXATQUGIG 8
output: GNVIZ 6
output: IHWBQDJ 1
output: IQGIGUJZ 5
output: IRVAVMQKN 7
output: JMUPNYRQD 4
output: LACXYFQHSQ 0


Примечания:
Эта задача имеет решение сложности O(n), но вам достаточно написать решение
сложности O(n^2) (не считая сложности обращения к элементам словаря). Пример
ниже соответствует приведённому древу рода Романовых.
"""
from collections import defaultdict
from dataclasses import dataclass
from typing import Self

import sys
sys.setrecursionlimit(100000)


@dataclass(frozen=True)
class ProblemInput:
    n: int
    persons: list[tuple[str, str]]


class Solver:
    def __init__(self, data: ProblemInput) -> None:
        self.data = data

    @classmethod
    def from_stdin(cls) -> Self:
        n = int(input())
        persons = []
        for _ in range(n-1):
            child, parent = input().split()
            persons.append((child, parent))
        return cls(ProblemInput(n, persons))

    @classmethod
    def from_strings(cls, lines: list[str]) -> Self:
        n = int(lines[0])
        persons = []
        for i in range(n-1):
            child, parent = lines[i+1].split()
            persons.append((child, parent))
        return cls(ProblemInput(n, persons))

    def solve(self) -> list[tuple[str, int]]:

        all_persons = set()
        all_children = set()
        child_of = defaultdict(list)
        for child, parent in self.data.persons:
            all_persons.add(child)
            all_persons.add(parent)
            all_children.add(child)
            child_of[parent].append(child)

        root = (all_persons - all_children).pop()
        counter = {root: 0}

        def foo(prnt: str) -> int:
            for ch in child_of[prnt]:
                counter[ch] = counter[prnt] + 1
                foo(ch)
            return counter[prnt]

        foo(root)

        return sorted(counter.items())


def main() -> None:

    solver = Solver.from_stdin()
    result = solver.solve()

    for answer in result:
        print(*answer)


if __name__ == "__main__":
    main()
