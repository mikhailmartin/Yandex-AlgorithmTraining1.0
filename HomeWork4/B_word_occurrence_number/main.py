INPUT_FILE_NAME = "input.txt"


def main():
    input_file = open(INPUT_FILE_NAME, "r", encoding="utf8")

    word_count = dict()
    for line in input_file:
        for word in line.split():
            print(word_count.get(word, 0), end=" ")
            word_count[word] = word_count.get(word, 0) + 1


if __name__ == "__main__":
    main()
