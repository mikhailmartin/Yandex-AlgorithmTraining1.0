import sys


def main(lines: list[str] | None = None) -> int:

    lines = lines or sys.stdin.read().splitlines()

    n, r = map(int, lines[0].split())
    monuments = list(map(int, lines[1].split()))

    i = j = 0
    count = 0

    while i < n and j < n:

        distance = monuments[j] - monuments[i]

        if distance <= r:
            j += 1
        else:
            count += n-j
            i += 1

    return count


if __name__ == "__main__":
    result = main()
    print(result)
