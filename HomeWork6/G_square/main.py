import sys


def main(lines: list[str] | None = None) -> int:

    lines = lines or sys.stdin.read().splitlines()

    n = int(lines[0])
    m = int(lines[1])
    t = int(lines[2])

    if n < m:
        min_size = n
        max_size = m
    else:
        min_size = m
        max_size = n

    def rbs(lo: int, hi: int) -> int:
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if check(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo

    def check(width: int) -> bool:
        return tile_count(width) <= t

    def tile_count(width: int) -> int:
        """
        Считает количество плиток, которое необходимо для создания дорожки
        по краю площади.
        """
        return 2 * width * (max_size + min_size - 2 * width)

    return rbs(lo=0, hi=min_size // 2)


if __name__ == "__main__":
    result = main()
    print(result)
