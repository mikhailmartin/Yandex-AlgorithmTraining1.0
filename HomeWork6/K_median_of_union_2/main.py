import sys
from array import array


def main(lines: list[str] | None = None) -> list[int]:

    lines = lines or sys.stdin.read().splitlines()

    n, l = map(int, lines[0].split())
    arrs = []
    for i in range(n):
        x1, d1, a, c, m = list(map(int, lines[i + 1].split()))
        arr = array("i", [0] * l)
        arr[0] = x1
        d = d1
        for j in range(1, l):
            arr[j] = arr[j - 1] + d
            d = (a * d + c) % m
        arrs.append(arr)

    def left_median_of_union(a_arr: array, b_arr: array) -> int:

        def rbs(lo: int, hi: int) -> int:
            while lo < hi:
                mid = (lo + hi + 1) // 2
                if check(mid):
                    lo = mid
                else:
                    hi = mid - 1
            return lo

        def check(mid: int) -> bool:

            i = mid
            j = l - i

            a_left = a_arr[i-1] if i > 0 else float("-inf")
            b_right = b_arr[j] if j < l else float("+inf")

            return a_left <= b_right

        i = rbs(lo=0, hi=l)
        j = l - i

        a_left = a_arr[i - 1] if i > 0 else float("-inf")
        b_left = b_arr[j - 1] if j > 0 else float("-inf")

        return max(a_left, b_left)

    res = []
    for i in range(n):
        for j in range(i+1, n):
            median = left_median_of_union(arrs[i], arrs[j])
            res.append(median)

    return res


if __name__ == "__main__":
    result = main()
    print("\n".join(map(str, result)))
