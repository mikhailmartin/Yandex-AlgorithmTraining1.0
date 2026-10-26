import sys
from typing import Self


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


def main(lines: list[str] | None = None) -> list[int]:

    lines = lines or sys.stdin.read().splitlines()

    sequence = list(map(int, lines[0].split()))

    tree = BinarySearchTree()
    for num in sequence[:-1]:
        tree.add_node(num)

    sorted_leafs = tree.leafs()

    return sorted_leafs


if __name__ == "__main__":
    result = main()
    print("\n".join(map(str, result)))
