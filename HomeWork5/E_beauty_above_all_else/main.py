import sys


def main(lines: list[str] | None = None) -> tuple[int, int]:

    lines = lines or sys.stdin.read().splitlines()

    n, k = map(int, lines[0].split())
    trees = list(map(int, lines[1].split()))

    best_left = 0
    best_right = n-1
    tree_type_counter = ["tech"] + [0] * k
    unique_tree_type_counter = 0

    left = 0
    for right, tree_type in enumerate(trees):

        if tree_type_counter[tree_type] == 0:
            unique_tree_type_counter += 1
        tree_type_counter[tree_type] += 1

        if unique_tree_type_counter == k:
            while tree_type_counter[trees[left]] > 1:
                tree_type_counter[trees[left]] -= 1
                left += 1

            if best_right - best_left > right - left:
                best_left = left
                best_right = right

    return best_left+1, best_right+1


if __name__ == "__main__":
    result = main()
    print(*result)
