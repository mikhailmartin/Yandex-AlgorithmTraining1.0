import re


INPUT_FILE_NAME = "input.txt"


def main():
    identifier_count = get_identifier_count(*parse_input())

    max_count = -1
    max_identifier = None
    for identifier, count in identifier_count.items():
        if count > max_count:
            max_count = count
            max_identifier = identifier

    print(max_identifier)


def parse_input() -> tuple[list[str], set[str], bool, bool]:

    # читаем файл в список строк
    input_file = open(INPUT_FILE_NAME, "r", encoding="utf8")
    lines = input_file.read().strip().split("\n")

    # читаем входные параметры и приводим их к нормальной форме
    n, C, D = lines[0].split()
    n = int(n)
    match C:
        case "yes":
            is_case_sensitive = True
        case "no":
            is_case_sensitive = False
    match D:
        case "yes":
            can_start_with_number = True
        case "no":
            can_start_with_number = False

    # читаем ключевые слова с проверками
    keywords = set()
    for keyword in lines[1: n + 1]:

        if not is_case_sensitive:
            keyword = keyword.lower()

        if not can_start_with_number and keyword[0].isdigit():
            continue

        keywords.add(keyword)

    # читаем слова в программе в список
    words = []
    for line in lines[n + 1:]:
        line = re.sub("[^a-zA-Z0-9_]", " ", line)
        words.extend(line.split())

    return words, keywords, is_case_sensitive, can_start_with_number


def get_identifier_count(
    words: list[str],
    keywords: set[str],
    is_case_sensitive: bool,
    can_start_with_number: bool,
) -> dict[str, int]:

    identifier_count = dict()
    for word in words:

        if not is_case_sensitive:
            word = word.lower()

        if not is_identifier(word, keywords, can_start_with_number):
            continue

        identifier_count[word] = identifier_count.get(word, 0) + 1

    return identifier_count


def is_identifier(word: str, keywords: set[str], can_start_with_number: bool) -> bool:

    if not can_start_with_number and word[0].isdigit():
        return False

    if word.isdigit():
        return False

    if word in keywords:
        return False

    return True


if __name__ == "__main__":
    main()
