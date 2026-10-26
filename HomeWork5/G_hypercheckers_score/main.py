import sys
from collections import Counter


def main(lines: list[str] | None = None) -> int:

    lines = lines or sys.stdin.read().splitlines()

    n, k = map(int, lines[0].split())
    nums = list(map(int, lines[1].split()))

    num_counter = Counter(nums)
    unique_nums = sorted(num_counter.keys())

    right = 0
    duplicates_counter = 0
    counter = 0
    for left in range(len(unique_nums)):

        left_num = unique_nums[left]

        # передвигаем правый указатель "до упора",
        # считая количество карточек, имеющих дубликаты
        while (
            right < len(unique_nums) and unique_nums[right] / unique_nums[left] <= k
        ):
            right_num = unique_nums[right]
            if num_counter[right_num] >= 2:
                duplicates_counter += 1
            right += 1

        # (a, a, a) -> 1
        if num_counter[left_num] >= 3:
            counter += 1

        # (a, a, b) -> 3
        distance = right - left
        if num_counter[left_num] >= 2:
            counter += (distance - 1) * 3
            duplicates_counter -= 1

        # (a, b, b) -> 3
        counter += duplicates_counter * 3

        # (a, b, c) -> 6
        counter += (distance - 1) * (distance - 2) * 3

    return counter


if __name__ == "__main__":
    result = main()
    print(result)
