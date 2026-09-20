"""
Родословная: число потомков

Ограничение времени - 2 секунды
Ограничение памяти - 64Mb
Ввод - стандартный ввод или input.txt
Вывод - стандартный вывод или output.txt

В генеалогическом древе у каждого человека, кроме родоначальника, есть ровно
один родитель.

Для каждого элемента дерева определите число всех его потомков (не считая его
самого).


Формат ввода:
Программа получает на вход число элементов в генеалогическом древе N. Далее
следует N−1 строка, задающие родителя для каждого элемента древа, кроме
родоначальника. Каждая строка имеет вид имя_потомка имя_родителя.


Формат вывода:
Выведите список всех элементов в лексикографическом порядке, для каждого
элемента выводите количество всех его потомков.


Пример
input: 9
input: Alexei Peter_I
input: Anna Peter_I
input: Elizabeth Peter_I
input: Peter_II Alexei
input: Peter_III Anna
input: Paul_I Peter_III
input: Alexander_I Paul_I
input: Nicholaus_I Paul_I
output: Alexander_I 0
output: Alexei 1
output: Anna 4
output: Elizabeth 0
output: Nicholaus_I 0
output: Paul_I 2
output: Peter_I 8
output: Peter_II 0
output: Peter_III 3


Примечания
Если вы используете рекурсию, то вам может быть полезно добавление в начало
программы следующих строк:
import sys
sys.setrecursionlimit(100000)
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
        counter = dict()

        def foo(prnt: str) -> int:
            count = 0
            for ch in child_of[prnt]:
                count += 1 + foo(ch)
            counter[prnt] = count
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
