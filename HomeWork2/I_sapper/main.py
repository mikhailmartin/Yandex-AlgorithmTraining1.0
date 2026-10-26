import sys


def main(lines: list[str] | None = None) -> str:

    lines = lines or sys.stdin.read().splitlines()

    n, m, k = map(int, lines[0].split())
    mines = [tuple(map(int, lines[1+i].split())) for i in range(k)]

    rows = []
    for row_number in range(1, n+1):
        cells = []
        for col_number in range(1, m+1):

            count = 0
            for p, q in mines:

                dif1 = abs(p - row_number)
                dif2 = abs(q - col_number)

                if dif1 == 0 and dif2 == 0:
                    count = "*"
                    break
                elif dif1 <= 1 and dif2 <= 1:
                    count += 1

            cells.append(str(count))

        row = " ".join(cells)
        rows.append(row)

    rows = "\n".join(rows)

    return rows


if __name__ == "__main__":
    result = main()
    print(result)
