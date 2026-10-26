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

    def is_balanced(self) -> bool:
        flag, _ = self._is_balanced(self.tree)
        return flag

    def _is_balanced(self, node: TreeNode) -> tuple[bool, int]:
        if node.left:
            left_is_balanced, left_max_depth = self._is_balanced(node.left)
        else:
            left_is_balanced, left_max_depth = True, node.depth

        if node.right:
            right_is_balanced, right_max_depth = self._is_balanced(node.right)
        else:
            right_is_balanced, right_max_depth = True, node.depth

        if (
            left_is_balanced and right_is_balanced
            and abs(left_max_depth - right_max_depth) <= 1
        ):
            node_is_balanced = True
        else:
            node_is_balanced = False

        return node_is_balanced, max(left_max_depth, right_max_depth)


def main(lines: list[str] | None = None) -> bool:

    lines = lines or sys.stdin.read().splitlines()

    sequence = list(map(int, lines[0].split()))

    tree = BinarySearchTree()
    for num in sequence[:-1]:
        tree.add_node(num)

    return tree.is_balanced()


if __name__ == "__main__":
    result = main()
    print("YES" if result else "NO")
