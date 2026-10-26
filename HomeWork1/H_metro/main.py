import sys


def main(lines: list[str] | None = None) -> tuple[int, int] | tuple[int]:

    lines = lines or sys.stdin.read().splitlines()

    a = int(lines[0])
    b = int(lines[1])
    n = int(lines[2])
    m = int(lines[3])

    min1 = a * (n - 1) + n
    max1 = a * (n + 1) + n

    min2 = b * (m - 1) + m
    max2 = b * (m + 1) + m

    min3 = max(min1, min2)
    max3 = min(max1, max2)

    if min3 > max3:
        return (-1,)
    else:
        return min3, max3


if __name__ == "__main__":
    result = main()
    print(*result)
