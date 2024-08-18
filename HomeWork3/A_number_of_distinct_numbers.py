"""
Количество различных чисел

Ограничение времени - 1 секунда
Ограничение памяти - 64Mb
Ввод - стандартный ввод или input.txt
Вывод - стандартный вывод или output.txt

Дан список чисел, который может содержать до 100000 чисел. Определите, сколько
в нём встречается различных чисел.


Формат ввода:
Вводится список целых чисел. Все числа списка находятся на одной строке.


Формат вывода:
Выведите ответ на задачу.


Пример 1
input: 1 2 3 2 1
output: 3

Пример 2
input: 1 2 3 4 5 6 7 8 9 10
output: 10

Пример 3
input: 1 2 3 4 5 1 2 1 2 7 3
output: 6
"""
if __name__ == "__main__":

    print(len(set(map(int, input().split()))))