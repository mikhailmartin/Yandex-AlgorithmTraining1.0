import sys


def main(lines: list[str] | None = None) -> tuple[int, int]:

    lines = lines or sys.stdin.read().splitlines()

    n, k = map(int, lines[0].split())
    string = lines[1]

    # инициализируем словарь со всеми символами
    char_counter = dict()
    for char in string:
        char_counter[char] = 0

    best_length = -1
    best_start = -1
    right = 0
    for left in range(len(string)):

        while right < len(string) and char_counter[string[right]] <= k-1:
            char_counter[string[right]] += 1
            right += 1

        current_length = right - left
        if current_length > best_length:
            best_length = current_length
            best_start = left

        char_counter[string[left]] -= 1

    return best_length, best_start+1


if __name__ == "__main__":
    result = main()
    print(*result)
