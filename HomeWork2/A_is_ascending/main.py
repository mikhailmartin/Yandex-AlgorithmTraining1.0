import sys


def main(lines: list[str] | None = None) -> str:

    lines = lines or sys.stdin.read().splitlines()

    nums = list(map(int, lines[0].split()))

    n = len(nums)
    i = 1
    while i < n and nums[i-1] < nums[i]:
        i += 1

    return "YES" if i == n else "NO"


if __name__ == "__main__":
    result = main()
    print(result)
