import sys


def main(lines: list[str] | None = None) -> int:

    lines = lines or sys.stdin.read().splitlines()

    n, k = map(int, lines[0].split())
    wires = [int(lines[i+1]) for i in range(n)]

    def rbs(lo: int, hi: int) -> int:
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if check(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo

    def check(length: int) -> bool:
        count = 0
        for wire in wires:
            count += wire // length
        return count >= k

    if not check(1):
        return 0

    return rbs(lo=1, hi=max(wires))


if __name__ == "__main__":
    result = main()
    print(result)
