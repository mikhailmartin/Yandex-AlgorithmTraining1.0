"""
Подстрока

Ограничение времени - 1 секунда
Ограничение памяти - 64Mb
Ввод - стандартный ввод или input.txt
Вывод - стандартный вывод или output.txt

В этой задаче Вам требуется найти максимальную по длине подстроку данной строки,
такую что каждый символ встречается в ней не более k раз.


Формат ввода:
В первой строке даны два целых числа n и k (1 ≤ n ≤ 100000, 1 ≤ k ≤ n),
где n – количество символов в строке. Во второй строке n символов –
данная строка, состоящая только из строчных латинских букв.


Формат вывода:
В выходной файл выведите два числа – длину искомой подстроки и номер её первого
символа. Если решений несколько, выведите любое.


Пример 1
input: 3 1
input: abb
output: 2 1

Пример 2
input: 5 2
input: ababa
output: 4 1
"""


def parse_data() -> tuple[int, str]:

    n, k = map(int, input().split())
    string = input()

    return k, string


def main(k: int, string: str):

    # инициализируем словарь со всеми символами
    char_counter = dict()
    for char in string:
        char_counter[char] = 0

    best_length = -1
    best_start = -1
    right_pointer = 0
    for left_pointer in range(len(string)):

        while right_pointer < len(string) and char_counter[string[right_pointer]] <= k-1:
            char_counter[string[right_pointer]] += 1
            right_pointer += 1

        current_length = right_pointer - left_pointer
        if current_length > best_length:
            best_length = current_length
            best_start = left_pointer

        char_counter[string[left_pointer]] -= 1

    return best_length, best_start+1


if __name__ == "__main__":

    k, string = parse_data()
    result = main(k, string)
    print(*result)
