import sys


def main(lines: list[str] | None = None) -> str:

    lines = lines or sys.stdin.read().splitlines()

    a, b, c = sorted(map(int, [lines[i] for i in range(3)]))

    if a + b > c:
        res = "YES"
    else:
        res = "NO"

    return res


if __name__ == "__main__":
    result = main()
    print(result)
