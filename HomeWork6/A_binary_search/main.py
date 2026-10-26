import sys


def main(lines: list[str] | None = None) -> list[str]:

    lines = lines or sys.stdin.read().splitlines()

    n, k = map(int, lines[0].split())
    arr1 = list(map(int, lines[1].split()))
    arr2 = list(map(int, lines[2].split()))

    def lbs(lo: int, hi: int) -> int:
        while lo < hi:
            mid = (lo + hi) // 2
            if check(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo

    def check(ptr: int) -> bool:
        return arr1[ptr] >= num

    res = []
    for num in arr2:
        index = lbs(lo=0, hi=n-1)
        if num == arr1[index]:
            res.append("YES")
        else:
            res.append("NO")

    return res


if __name__ == "__main__":
    result = main()
    print("\n".join(result))
