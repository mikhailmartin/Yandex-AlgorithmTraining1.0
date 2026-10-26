import sys


def main(lines: list[str] | None = None) -> int:

    lines = lines or sys.stdin.read().splitlines()

    n, k = map(int, lines[0].split())
    nums = list(map(int, lines[1].split()))

    prefix_sum_nums = [0] * (n+1)
    for i, num in enumerate(nums, start=1):
        prefix_sum_nums[i] = prefix_sum_nums[i-1] + num

    left = right = 0
    count = 0
    while left < n+1 and right < n+1:

        sum_ = prefix_sum_nums[right] - prefix_sum_nums[left]

        if sum_ == k:
            count += 1
            left += 1
            right += 1
        elif sum_ < k:
            right += 1
        elif sum_ > k:
            left += 1

    return count


if __name__ == "__main__":
    result = main()
    print(result)
