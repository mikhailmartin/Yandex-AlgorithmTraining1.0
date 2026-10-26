import sys
from collections import defaultdict


sys.setrecursionlimit(100_000)


def main(lines: list[str] | None = None) -> list[tuple[str, int]]:

    lines = lines or sys.stdin.read().splitlines()

    n = int(lines[0])
    persons = []
    for i in range(n - 1):
        child, parent = lines[i+1].split()
        persons.append((child, parent))

    all_persons = set()
    all_children = set()
    child_of = defaultdict(list)
    for child, parent in persons:
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


if __name__ == "__main__":
    result = main()
    for answer in result:
        print(*answer)
