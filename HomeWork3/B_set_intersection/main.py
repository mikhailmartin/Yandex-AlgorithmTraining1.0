import sys


def main(lines: list[str] | None = None) -> list[int]:

    lines = lines or sys.stdin.read().splitlines()

    num_set1 = set(map(int, lines[0].split()))
    num_set2 = set(map(int, lines[1].split()))

    return list(sorted(num_set1 & num_set2))


if __name__ == "__main__":
    result = main()
    print(" ".join(map(str, result)))
