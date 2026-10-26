import sys


def main(lines: list[str] | None = None) -> int:

    lines = lines or sys.stdin.read().splitlines()

    n, r, c = map(int, lines[0].split())
    arr = [int(lines[i+1]) for i in range(n)]
    arr.sort()

    def lbs(lo: int, hi: int) -> int:
        while lo < hi:
            mid = (lo + hi) // 2
            if check(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo

    def check(max_discomfort: int) -> bool:
        # считаем количество возможных бригад с заданным максимальным неудобством
        i = 0
        count = 0
        while i < n - c + 1:
            left = arr[i]
            right = arr[i + c - 1]
            curr_discomfort = right - left
            if curr_discomfort <= max_discomfort:
                count += 1
                i += c
            else:
                i += 1
        return r <= count

    left = 0
    right = arr[-1] - arr[0]

    return lbs(lo=left, hi=right)


if __name__ == "__main__":
    result = main()
    print(result)
