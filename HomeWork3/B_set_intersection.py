"""
Пересечение множеств

Ограничение времени - 1 секунда
Ограничение памяти - 64Mb
Ввод - стандартный ввод или input.txt
Вывод - стандартный вывод или output.txt

Даны два списка чисел, которые могут содержать до 10000 чисел каждый. Выведите
все числа, которые входят как в первый, так и во второй список в порядке
возрастания. Примечание. И даже эту задачу на Питоне можно решить в одну
строчку.


Формат ввода:
Вводятся два списка целых чисел. Все числа каждого списка находятся на отдельной строке.


Формат вывода:
Выведите ответ на задачу.


Пример 1
input: 1 3 2
input: 4 3 2
output: 2 3

Пример 2
input: 1 2 6 4 5 7
input: 10 2 3 4 8
output: 2 4
"""
if __name__ == "__main__":

    print(*sorted(set(map(int, input().split())).intersection(set(map(int, input().split())))))
