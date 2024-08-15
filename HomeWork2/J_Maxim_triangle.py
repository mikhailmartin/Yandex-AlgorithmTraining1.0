"""
Треугольник Максима

Ограничение времени - 1 секунда
Ограничение памяти - 64Mb
Ввод - стандартный ввод или input.txt
Вывод - стандартный вывод или output.txt

С детства Максим был неплохим музыкантом и мастером на все руки. Недавно он
самостоятельно сделал несложный перкуссионный музыкальный инструмент —
треугольник. Ему нужно узнать, какова частота звука, издаваемого его
инструментом.

У Максима есть профессиональный музыкальный тюнер, с помощью которого можно
проигрывать ноту с заданной частотой. Максим действует следующим образом: он
включает на тюнере ноты с разными частотами и для каждой ноты на слух
определяет, ближе или дальше она к издаваемому треугольником звуку, чем
предыдущая нота. Поскольку слух у Максима абсолютный, он определяет это всегда
абсолютно верно.

Вам Максим показал запись, в которой приведена последовательность частот,
выставляемых им на тюнере, и про каждую ноту, начиная со второй, записано —
ближе или дальше она к звуку треугольника, чем предыдущая нота. Заранее
известно, что частота звучания треугольника Максима составляет не менее 30 герц
и не более 4000 герц.

Требуется написать программу, которая определяет, в каком интервале может
находиться частота звучания треугольника.


Формат ввода:
Первая строка входного файла содержит целое число n — количество нот, которые
воспроизводил Максим с помощью тюнера (2 ≤ n ≤ 1000). Последующие n строк
содержат записи Максима, причём каждая строка содержит две компоненты:
вещественное число f_i — частоту, выставленную на тюнере, в герцах
(30 ≤ f_i ≤ 4000), и слово «closer» или слово «further» для каждой частоты,
кроме первой.

Слово «closer» означает, что частота данной ноты ближе к частоте звучания
треугольника, чем частота предыдущей ноты, что формально описывается
соотношением: |f_i − f_{triangle}| < |f_i − 1 − f_{triangle}|.

Слово «further» означает, что частота данной ноты дальше, чем предыдущая.

Если оказалось, что очередная нота так же близка к звуку треугольника, как и
предыдущая нота, то Максим мог записать любое из двух указанных выше слов.

Гарантируется, что результаты, полученные Максимом, непротиворечивы.


Формат вывода:
В выходной файл необходимо вывести через пробел два вещественных числа —
наименьшее и наибольшее возможное значение частоты звучания треугольника,
изготовленного Максимом. Числа должны быть выведены с точностью не хуже 10^{−6}.


Пример 1
input: 3
input: 440
input: 220 closer
input: 300 further
output: 30.0 260.0

Пример 2
input: 4
input: 554
input: 880 further
input: 440 closer
input: 622 closer
output: 531.0 660.0
"""


def main(
    previous_frequency: int,
    frequencies_answers: list[tuple[float, str]],
    left_border: float = 30.,
    right_border: float = 4000.,
) -> tuple[float, float]:

    for frequency, answer in frequencies_answers:

        if answer == "closer":
            if frequency < previous_frequency:
                right_border = min(right_border, (frequency + previous_frequency) / 2)
            elif frequency > previous_frequency:
                left_border = max(left_border, (frequency + previous_frequency) / 2)
        elif answer == "further":
            if frequency < previous_frequency:
                left_border = max(left_border, (frequency + previous_frequency) / 2)
            elif frequency > previous_frequency:
                right_border = min(right_border, (frequency + previous_frequency) / 2)

        previous_frequency = frequency

    return left_border, right_border


if __name__ == "__main__":

    n = int(input())
    first_frequency = float(input())
    frequencies_answers = []
    for _ in range(n-1):
        frequency, answer = input().split()
        frequency = float(frequency)
        frequencies_answers.append((frequency, answer))

    left_border, right_border = main(first_frequency, frequencies_answers)
    print(left_border, right_border)
