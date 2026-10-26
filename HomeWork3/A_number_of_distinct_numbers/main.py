import sys


def main(lines: list[str] | None = None) -> int:

    lines = lines or sys.stdin.read().splitlines()

    return len(set(map(int, lines[0].split())))


if __name__ == "__main__":
    result = main()
    print(result)
