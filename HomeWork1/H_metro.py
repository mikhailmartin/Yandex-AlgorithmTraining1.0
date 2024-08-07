"""
Метро

Ограничение времени - 1 секунда
Ограничение памяти - 64Mb
Ввод - стандартный ввод или input.txt
Вывод - стандартный вывод или output.txt

На некоторых кросс-платформенных станциях метро (как, например,
«Третьяковская») на разные стороны платформы приходят поезда разных
направлений. Таня договорилась встретиться с подругой на такой станции, но
поскольку подруга приехала из другого часового пояса, то из-за джетлага сильно
проспала, и Тане пришлось долго её ждать. Поезда всегда ходят точно по
расписанию, и Таня знает, что поезд стоит на платформе ровно одну минуту, а
интервал между поездами (время, в течение которого поезда у платформы нет)
составляет a минут для поездов на первом пути и b минут для поездов на втором
пути. То есть на первый путь приезжает поезд и стоит одну минуту, затем в
течение a минут поезда у платформы нет, затем в течение одной минуты у
платформы стоит следующий поезд и т. д.

Пока Таня стояла на платформе, она насчитала n поездов на первом пути и m
поездов на втором пути. Определите минимальное и максимальное время, которое
Таня могла провести на платформе, или сообщите, что она точно сбилась со счёта.

Все поезда, которые видела Таня, она наблюдала в течение всей минуты, то есть
Таня не приходит и не уходит с платформы посередине той минуты, когда поезд
стоит на платформе.


Формат ввода:
Первая строка входных данных содержит число a — интервал между поездами на
первом пути. Вторая строка содержит число b — интервал между поездами на втором
пути. Третья строка содержит число n — количество поездов на первом пути,
которые увидела Таня. Четвёртая строка содержит число m — количество поездов на
втором пути, которые увидела Таня. Все числа — целые, от 1 до 1000.


Формат вывода:
Программа должна вывести два числа: минимальное и максимальное время в минутах,
которое Таня могла стоять на платформе, или одно число -1, если Таня точно
ошиблась.


Пример 1
input: 1
input: 3
input: 3
input: 2
output: 5 7

Пример 2
input: 1
input: 5
input: 1
input: 2
output: -1


Примечание
В первом примере по первому пути поезда ходят через 1 минуту. По второму —
через 3. Стоя на платформе 5, 6 или 7 минут, Таня могла насчитать 3 поезда на
первом пути и 2 на втором.
"""


def main(a: int, b: int, n: int, m: int) -> tuple[int, int] | tuple[int]:

    min1 = a * (n - 1) + n
    max1 = a * (n + 1) + n

    min2 = b * (m - 1) + m
    max2 = b * (m + 1) + m

    min3 = max(min1, min2)
    max3 = min(max1, max2)

    if min3 > max3:
        return (-1,)
    else:
        return min3, max3


if __name__ == "__main__":

    # a, b, n, m = [int(input()) for _ in range(4)]
    # a, b, n, m = 1, 3, 3, 2
    a, b, n, m = 1, 5, 1, 2
    print(*main(a, b, n, m))
