"""
Вывод веток

Ограничение времени - 4 секунды
Ограничение памяти - 256Mb
Ввод - стандартный ввод или input.txt
Вывод - стандартный вывод или output.txt

Для полученного дерева выведите список всех вершин, имеющих только одного
ребёнка, в порядке возрастания.


Формат ввода:
Вводится последовательность целых чисел, оканчивающаяся нулём. Построить по ней
дерево.


Формат вывода:
Выведите список требуемых вершин.


Пример
input: 7 3 2 1 9 5 4 6 8 0
output: 2
output: 9
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

    def add_node(self, value: int) -> None:
        if self.tree is None:
            self.tree = TreeNode(value, depth=1)
        else:
            self._add_node(self.tree, value)

    def _add_node(self, node: TreeNode, value: int) -> None:
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value, node.depth+1)
                self.depth = max(self.depth, node.left.depth)
            else:
                self._add_node(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = TreeNode(value, node.depth+1)
                self.depth = max(self.depth, node.right.depth)
            else:
                self._add_node(node.right, value)
        else:
            pass

    def sorted(self) -> list[int]:
        result = []
        self._sorted(self.tree, result)
        return result

    def _sorted(self, node: TreeNode, lst: list[int]) -> None:
        if node.left:
            self._sorted(node.left, lst)
            lst.append(node.value)
        else:
            lst.append(node.value)

        if node.right:
            self._sorted(node.right, lst)

    def leafs(self) -> list[int]:
        result = []
        self._leafs(self.tree, result)
        return result

    def _leafs(self, node: TreeNode, lst: list[int]) -> None:
        if node.left:
            self._leafs(node.left, lst)
        if node.right:
            self._leafs(node.right, lst)
        if not node.left and not node.right:
            lst.append(node.value)

    def forks(self) -> list[int]:
        result = []
        self._forks(self.tree, result)
        return result

    def _forks(self, node: TreeNode, lst: list[int]) -> None:
        if node.left:
            self._forks(node.left, lst)
        if node.left and node.right:
            lst.append(node.value)
        if node.right:
            self._forks(node.right, lst)

    def branches(self) -> list[int]:
        result = []
        self._branches(self.tree, result)
        return result

    def _branches(self, node: TreeNode, lst: list[int]) -> None:
        if node.left:
            self._branches(node.left, lst)
        if (node.left and not node.right) or (not node.left and node.right):
            lst.append(node.value)
        if node.right:
            self._branches(node.right, lst)


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
        for num in self.data.sequence[:-1]:
            tree.add_node(num)

        sorted_branches = tree.branches()

        return sorted_branches


def main() -> None:

    solver = Solver.from_stdin()
    result = solver.solve()

    print("\n".join(map(str, result)))


if __name__ == "__main__":
    main()
