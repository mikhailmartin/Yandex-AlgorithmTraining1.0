"""
Количество слов в тексте

Ограничение времени - 1 секунда
Ограничение памяти - 64Mb
Ввод - стандартный ввод или input.txt
Вывод - стандартный вывод или output.txt

Во входном файле (вы можете читать данные из sys.stdin, подключив библиотеку
sys) записан текст. Словом считается последовательность непробельных символов
идущих подряд, слова разделены одним или большим числом пробелов или символами
конца строки. Определите, сколько различных слов содержится в этом тексте.


Формат ввода:
Вводится текст.


Формат вывода:
Выведите ответ на задачу.


Пример 1
input: She sells sea shells on the sea shore;
The shells that she sells are sea shells I'm sure.
So if she sells sea shells on the sea shore,
I'm sure that the shells are sea shore shells.
output: 19
"""
INPUT_FILE_NAME = "input.txt"


def main(text: str) -> int:

    return len(set(text.split()))


if __name__ == "__main__":

    with open(INPUT_FILE_NAME, "r", encoding="utf8") as input_file:
        text = input_file.read()

    n_unique_word = main(text)

    print(n_unique_word)
