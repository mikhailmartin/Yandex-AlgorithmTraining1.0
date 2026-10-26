import sys


def main(lines: list[str] | None = None) -> tuple[int, int]:

    lines = lines or sys.stdin.read().splitlines()

    nums = list(map(int, lines[0].split()))

    # инициализация
    num0 = nums[0]
    num1 = nums[1]
    if num0 >= num1:
        max1 = min2 = num0
        max2 = min1 = num1
    else:
        max1 = min2 = num1
        max2 = min1 = num0

    for num in nums[2:]:

        if num >= max1:
            max2 = max1
            max1 = num
        elif num > max2:
            max2 = num

        if num <= min1:
            min2 = min1
            min1 = num
        elif num < min2:
            min2 = num

    if max1 * max2 >= min1 * min2:
        return max2, max1
    else:
        return min1, min2


if __name__ == "__main__":
    num1, num2 = main()
    print(num1, num2)
