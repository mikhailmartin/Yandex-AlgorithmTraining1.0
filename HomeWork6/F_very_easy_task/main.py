import sys


def main(lines: list[str] | None = None) -> int:

    lines = lines or sys.stdin.read().splitlines()

    n, x, y = map(int, lines[0].split())

    if x < y:
        fast = x
        slow = y
    else:
        fast = y
        slow = x

    def lbs(lo: int, hi: int) -> int:
        while lo < hi:
            mid = (lo + hi) // 2
            if check(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo

    def check(time: int) -> bool:
        # первую копию делаем всегда на быстром ксероксе
        time -= fast  # осталось времени

        f = time // fast  # успеем сделать f копий на быстром принтере
        s = time // slow  # успеем сделать s копий на медленном принтере

        return n - 1 <= f + s

    return lbs(lo=fast, hi=n*slow)


if __name__ == "__main__":
    result = main()
    print(result)
