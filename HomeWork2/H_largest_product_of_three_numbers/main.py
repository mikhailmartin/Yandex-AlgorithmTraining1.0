import sys


def main(lines: list[str] | None = None) -> tuple[int, int, int]:

    lines = lines or sys.stdin.read().splitlines()

    nums = list(map(int, lines[0].split()))

    # инициализация
    max3, max2, max1 = sorted(nums[:3])
    min1 = max3
    min2 = max2

    for num in nums[3:]:

        if num >= max1:
            max3 = max2
            max2 = max1
            max1 = num
        elif num >= max2:
            max3 = max2
            max2 = num
        elif num > max3:
            max3 = num

        if num <= min1:
            min2 = min1
            min1 = num
        elif num < min2:
            min2 = num

    if min1 * min2 * max1 > max1 * max2 * max3:
        return min1, min2, max1
    else:
        return max1, max2, max3


if __name__ == "__main__":
    num1, num2, num3 = main()
    print(num1, num2, num3)
