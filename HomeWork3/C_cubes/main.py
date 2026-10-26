import sys


def main(lines: list[str] | None = None) -> tuple[set[int], set[int], set[int]]:

    lines = lines or sys.stdin.read().splitlines()

    n, m = map(int, lines[0].split())
    anyas = set([int(lines[1+i]) for i in range(n)])
    boryas = set([int(lines[1+n+j]) for j in range(m)])

    intersection = anyas & boryas
    only_anyas = anyas - intersection
    only_boryas = boryas - intersection

    return intersection, only_anyas, only_boryas


if __name__ == "__main__":
    intersection, only_anyas, only_boryas = main()

    print(len(intersection))
    print(*sorted(intersection))

    print(len(only_anyas))
    print(*sorted(only_anyas))

    print(len(only_boryas))
    print(*sorted(only_boryas))
