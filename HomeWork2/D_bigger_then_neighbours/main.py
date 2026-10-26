import sys


def main(lines: list[str] | None = None) -> int:

    lines = lines or sys.stdin.read().splitlines()

    nums = list(map(int, lines[0].split()))

    count = 0
    for i in range(1, len(nums)-1):
        prev = nums[i-1]
        curr = nums[i]
        next = nums[i+1]

        if curr > prev and curr > next:
            count += 1

    return count


if __name__ == "__main__":
    result = main()
    print(result)
