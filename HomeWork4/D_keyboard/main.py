import sys


def main(lines: list[str] | None = None) -> list[str]:

    lines = lines or sys.stdin.read().splitlines()

    n = int(lines[0])
    cs = list(map(int, lines[1].split()))
    k = int(lines[2])
    ps = list(map(int, lines[3].split()))

    for num in ps:
        cs[num-1] -= 1

    return ["YES" if key < 0 else "NO" for key in cs]


if __name__ == "__main__":
    result = main()
    print("\n".join(result))
