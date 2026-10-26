import sys


def main(lines: list[str] | None = None) -> int:

    lines = lines or sys.stdin.read().splitlines()

    a = int(lines[0])
    b = int(lines[1])
    c = int(lines[2])

    twos = a
    threes = b
    fours = c

    def lbs(lo: int, hi: int) -> int:
        while lo < hi:
            mid = (lo + hi) // 2
            if check(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo

    def check(fives: int) -> bool:
        amount = twos * 2 + threes * 3 + fours * 4 + fives * 5
        n = twos + threes + fours + fives
        return 2 * amount >= 7 * n

    amount = twos + threes + fours
    fives = lbs(lo=0, hi=amount)

    return fives


if __name__ == "__main__":
    result = main()
    print(result)
