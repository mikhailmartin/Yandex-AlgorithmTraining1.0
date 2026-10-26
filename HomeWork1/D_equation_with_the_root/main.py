import sys


def main(lines: list[str] | None = None) -> str | int:

    lines = lines or sys.stdin.read().splitlines()

    a = int(lines[0])
    b = int(lines[1])
    c = int(lines[2])

    if c < 0:
        x = "NO SOLUTION"
    elif a == 0:
        if b == (c ** 2):
            x = "MANY SOLUTIONS"
        else:
            x = "NO SOLUTION"
    else:
        x = (c ** 2 - b) / a
        if (x % 1) == 0:
            x = int(x)
        else:
            x = "NO SOLUTION"

    return x


if __name__ == "__main__":
    result = main()
    print(result)
