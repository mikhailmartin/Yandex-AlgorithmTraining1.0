import sys


def main(lines: list[str] | None = None) -> int:

    lines = lines or sys.stdin.read().splitlines()

    w, h, n = map(int, lines[0].split())

    min_width = w
    max_width = w * n
    min_height = h
    max_height = h * n

    min_size = max(min_width, min_height)
    max_size = max(max_width, max_height)

    def lbs(lo: int, high: int) -> int:
        while lo < high:
            mid = (lo + high) // 2
            if check(mid):
                high = mid
            else:
                lo = mid + 1
        return lo

    def check(size: int) -> bool:
        n_row = size // w
        n_col = size // h
        return n <= n_row * n_col

    size = lbs(lo=min_size, high=max_size)

    return size


if __name__ == "__main__":
    result = main()
    print(result)
