"""
Сапёр

Ограничение времени - 1 секунда
Ограничение памяти - 64Mb
Ввод - стандартный ввод или input.txt
Вывод - стандартный вывод или output.txt

Вам необходимо построить поле для игры "Сапёр" по его конфигурации – размерам и
координатам расставленных на нём мин.

Вкратце напомним правила построения поля для игры "Сапёр":
- Поле состоит из клеток с минами и пустых клеток
- Клетки с миной обозначаются символом *
- Пустые клетки содержат число k_{i,j}, 0≤ k_{i,j} ≤ 8 – количество мин на
соседних клетках.

Соседними клетками являются восемь клеток, имеющих смежный угол или сторону.


Формат ввода:
В первой строке содержатся три числа: N, 1 ≤ N ≤ 100 - количество строк на поле,
M, 1 ≤ M ≤ 100 - количество столбцов на поле, K, 0 ≤ K ≤ N ⋅ M - количество мин на поле.

В следующих K строках содержатся по два числа с координатами мин:
p, 1 ≤ p ≤ N - номер строки мины, q, 1 ≤ 1 ≤ M - номер столбца мины.


Формат вывода:
Выведите построенное поле, разделяя строки поля переводом строки, а столбцы - пробелом.


Пример 1
input: 3 2 2
input: 1 1
input: 2 2
output: * 2
output: 2 *
output: 1 1

Пример 2
input: 2 2 0
output: 0 0
output: 0 0

Пример 3
input: 4 4 4
input: 1 3
input: 2 1
input: 4 2
input: 4 4
output: 1 2 * 1
output: * 2 1 1
output: 2 2 2 1
output: 1 * 2 *
"""


def main(n: int, m: int, mines: list[tuple[int, int]]):
    """
    Строит поле для игры "Сапёр" по его конфигурации.

    Parameters:
        n: количество строк на поле;
        m: количество столбцов на поле;
        mines: список с координатами мин, координаты - кортежи вида (p, q),
          где p - номер строки мины, q - номер столбца мины.

    Returns:
        Поле для игры "Сапёр".
    """
    lines = []
    for line_number in range(1, n+1):

        cells = []
        for column_number in range(1, m+1):

            count = 0
            for p, q in mines:

                dif1 = abs(p - line_number)
                dif2 = abs(q - column_number)

                if dif1 == 0 and dif2 == 0:
                    count = "*"
                    break
                elif dif1 <= 1 and dif2 <= 1:
                    count += 1

            cells.append(str(count))

        line = " ".join(cells)
        lines.append(line)

    lines = "\n".join(lines)

    return lines


if __name__ == "__main__":

    n, m, k = map(int, input().split())
    mines = [tuple(map(int, input().split())) for _ in range(k)]
    print(main(n, m, mines))