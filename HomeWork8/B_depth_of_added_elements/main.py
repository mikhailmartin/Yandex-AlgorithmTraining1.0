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


def main(lines: list[str] | None = None) -> list[int]:

    lines = lines or sys.stdin.read().splitlines()

    sequence = list(map(int, lines[0].split()))

    tree = BinarySearchTree()
    res = []
    for num in sequence[:-1]:
        depth = tree.add_node(num)
        if depth is not None:
            res.append(depth)

    return res


if __name__ == "__main__":
    result = main()
    print(" ".join(map(str, result)))
