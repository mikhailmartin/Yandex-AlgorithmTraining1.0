import sys


def main(lines: list[str] | None = None) -> int:

    lines = lines or sys.stdin.read().splitlines()

    n = int(lines[0])
    birds = [tuple(map(int, lines[1+i].split())) for i in range(n)]

    xs = set()
    for bird in birds:
        xs.add(bird[0])

    return len(xs)


if __name__ == "__main__":
    result = main()
    print(result)
