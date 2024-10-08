"""
Инопланетный геном

Ограничение времени - 1 секунда
Ограничение памяти - 64Mb
Ввод - стандартный ввод или input.txt
Вывод - стандартный вывод или output.txt

Геном жителей системы Тау Кита содержит 26 видов оснований, для обозначения
которых будем использовать буквы латинского алфавита от A до Z, а сам геном
записывается строкой из латинских букв. Важную роль в геноме играют пары
соседних оснований, например, в геноме «ABBACAB» можно выделить следующие пары
оснований: AB, BB, BA, AC, CA, AB.

Степенью близости одного генома другому геному называется количество пар
соседних оснований первого генома, которые встречаются во втором геноме.


Формат ввода:
Вам даны два генома, определите степень близости первого генома второму геному.
Программа получает на вход две строки, состоящие из заглавных латинских букв.
Каждая строка непустая, и её длина не превосходит 10^5.


Формат вывода:
Программа должна вывести одно целое число – степень близости генома,
записанного в первой строке, геному, записанному во второй строке.


Пример:
input: ABBACAB
input: BCABB
output: 4


Примечания:
Следующие пары оснований первого генома встречаются во втором геноме:
AB, BB, CA, AB. Обратите внимание на то, что пара AB в первом геноме
встречается два раза, поэтому и подсчитана в ответе два раза.
"""


def get_proximity(first_genome: str, second_genome: str) -> int:

    first_pairs = [first_genome[i:i+2] for i in range(len(first_genome)-1)]
    second_pairs = [second_genome[i:i + 2] for i in range(len(second_genome) - 1)]

    second_unique_pairs = set(second_pairs)

    proximity = 0
    for pair in first_pairs:
        if pair in second_unique_pairs:
            proximity += 1

    return proximity


if __name__ == "__main__":

    first_genome = input()
    second_genome = input()
    proximity = get_proximity(first_genome, second_genome)
    print(proximity)
