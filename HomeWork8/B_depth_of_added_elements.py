"""
Глубина добавляемых элементов

Ограничение времени - 4 секунды
Ограничение памяти - 256Mb
Ввод - стандартный ввод или input.txt
Вывод - стандартный вывод или output.txt

В бинарное дерево поиска добавляются элементы. Выведите глубину для каждого
добавленного элемента в том порядке, как они добавлялись. Если элемент уже есть
в дереве, то ничего добавлять и выводить не нужно. Глубиной называется
расстояние от корня дерева до элемента включительно.


Формат ввода:
Вводится последовательность целых чисел, оканчивающаяся нулём. Сам ноль в
последовательность не входит. По данной последовательности требуется построить
дерево.


Формат вывода:
Выведите ответ на задачу.


Пример
input: 7 3 2 1 9 5 4 6 8 0
output: 1 2 3 4 2 3 4 4 3
"""
from dataclasses import dataclass
from typing import Self


@dataclass(frozen=True)
class ProblemInput:
    sequence: list[int]


class TreeNode:
    def __init__(self, value: int, depth: int) -> None:
        self.value = value
        self.left: Self | None = None
        self.right: Self | None = None
        self.depth: int = depth


class BinarySearchTree:
    def __init__(self) -> None:
        self.tree: TreeNode | None = None
        self.depth: int = 0

    def add_node(self, value: int) -> int | None:
        if self.tree is None:
            self.tree = TreeNode(value, 1)
            return 1
        else:
            return self._add_node(self.tree, value)

    def _add_node(self, node: TreeNode, value: int) -> int | None:
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value, node.depth+1)
                self.depth = max(self.depth, node.left.depth)
                return node.left.depth
            else:
                return self._add_node(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = TreeNode(value, node.depth+1)
                self.depth = max(self.depth, node.right.depth)
                return node.right.depth
            else:
                return self._add_node(node.right, value)
        else:
            return None

class Solver:
    def __init__(self, data: ProblemInput) -> None:
        self.data = data

    @classmethod
    def from_stdin(cls) -> Self:
        sequence = list(map(int, input().split()))
        return cls(ProblemInput(sequence))

    @classmethod
    def from_strings(cls, lines: list[str]) -> Self:
        sequence = list(map(int, lines[0].split()))
        return cls(ProblemInput(sequence))

    def solve(self) -> list[int]:

        tree = BinarySearchTree()
        result = []
        for num in self.data.sequence[:-1]:
            depth = tree.add_node(num)
            if depth is not None:
                result.append(depth)

        return result


def main() -> None:

    solver = Solver.from_stdin()
    result = solver.solve()

    print(" ".join(map(str, result)))


if __name__ == "__main__":
    main()
