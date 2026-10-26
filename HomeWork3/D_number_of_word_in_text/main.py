INPUT_FILE_NAME = "input.txt"


def main(text: str) -> int:
    return len(set(text.split()))


if __name__ == "__main__":

    with open(INPUT_FILE_NAME, "r", encoding="utf8") as input_file:
        text = input_file.read()

    n_unique_word = main(text)

    print(n_unique_word)
