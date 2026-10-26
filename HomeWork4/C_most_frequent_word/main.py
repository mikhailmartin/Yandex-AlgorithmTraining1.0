INPUT_FILE_NAME = "input.txt"


def main() -> str:
    input_file = open(INPUT_FILE_NAME, "r", encoding="utf8")

    word_count = dict()
    for line in input_file:
        words = line.split()
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1
    input_file.close()

    max_count = -1
    most_frequent_word = ""
    for word, count in sorted(word_count.items()):
        if max_count < count:
            max_count = count
            most_frequent_word = word

    return most_frequent_word


if __name__ == "__main__":
    result = main()
    print(result)
