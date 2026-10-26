import sys


def main(lines: list[str] | None = None) -> tuple[int, int]:

    lines = lines or sys.stdin.read().splitlines()

    n = int(lines[0])
    shirts = list(map(int, lines[1].split()))
    m = int(lines[2])
    pants = list(map(int, lines[3].split()))

    i = j = 0
    i_best = j_best = 0
    style_best = abs(shirts[i] - pants[j])

    while i < n and j < m:

        style = abs(shirts[i] - pants[j])

        if style < style_best:

            i_best = i
            j_best = j
            style_best = style

            if style_best == 0:
                break

        if shirts[i] < pants[j]:
            i += 1
        else:
            j += 1

    return shirts[i_best], pants[j_best]


if __name__ == "__main__":
    result = main()
    print(*result)
