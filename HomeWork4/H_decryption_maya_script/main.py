import sys
from collections import Counter


def main(lines: list[str] | None = None) -> int:

    lines = lines or sys.stdin.read().splitlines()

    len_word, len_string = map(int, lines[0].split())
    word = lines[1]
    string = lines[2]

    word_counter = Counter(word)
    string_counter = Counter(string[:len_word])
    count = 1 if word_counter == string_counter else 0

    for i in range(len_string - len_word):

        char_to_remove = string[i]
        char_to_add = string[i+len_word]

        string_counter[char_to_remove] -= 1
        string_counter[char_to_add] += 1

        if word_counter == string_counter:
            count += 1

    return count


if __name__ == "__main__":
    result = main()
    print(result)
