import sys


def main(lines: list[str] | None = None) -> int:

    lines = lines or sys.stdin.read().splitlines()

    n, a, b, w, h = map(int, lines[0].split())

    max_protection1 = (w - a) // 2
    max_protection2 = (w - b) // 2
    max_protection = max(max_protection1, max_protection2)

    def rbs(lo: int, hi: int) -> int:
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if check(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo

    def check(protection: int) -> bool:

        # обычная ориентация
        n_row = w // (a + 2 * protection)
        n_col = h // (b + 2 * protection)
        n1 = n_row * n_col

        # повёрнутая на 90 градусов
        n_row = w // (b + 2 * protection)
        n_col = h // (a + 2 * protection)
        n2 = n_row * n_col

        return n <= n1 or n <= n2

    protection = rbs(lo=0, hi=max_protection)

    return protection


if __name__ == "__main__":
    result = main()
    print(result)
