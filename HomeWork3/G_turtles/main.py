import sys


def main(lines: list[str] | None = None) -> int:

    lines = lines or sys.stdin.read().splitlines()

    n = int(lines[0])
    seen = [tuple(map(int, lines[1+i].split())) for i in range(n)]

    available = set([(i, n-1-i) for i in range(n)])
    seen = set(seen)

    return len(available & seen)


if __name__ == "__main__":
    result = main()
    print(result)
