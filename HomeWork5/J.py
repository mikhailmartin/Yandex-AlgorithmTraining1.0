"""
Треугольники

Ограничение времени - 4 секунды
Ограничение памяти - 256Mb
Ввод - стандартный ввод или input.txt
Вывод - стандартный вывод или output.txt

Петя достаточно давно занимается в математическом кружке, поэтому он уже успел
не только правила выполнения простейших операций, но и такое достаточно сложное
понятие как симметрия. Для того, чтобы получше изучить симметрию Петя решил
начать с наиболее простых геометрических фигур – треугольников. Он скоро понял,
что осевой симметрией обладают так называемые равнобедренные треугольники.
Поэтому теперь Петя ищет везде такие треугольники.

Напомним, что треугольник называется равнобедренным, если его площадь
положительна, и у него есть хотя бы две равные стороны.

Недавно Петя, зайдя в класс, увидел, что на доске нарисовано n точек.
Разумеется, он сразу задумался, сколько существует троек из этих точек, которые
являются вершинами равнобедренных треугольников.

Требуется написать программу, решающую указанную задачу.


Формат ввода:
Входной файл содержит целое число n (3 ≤ n ≤ 1500). Каждая из последующих строк
содержит по два целых числа – x_i и y_i – координаты i-ой точки. Координаты
точек не превосходят 109 по абсолютной величине. Среди заданных точек нет
совпадающих.


Формат вывода:
В выходной файл выведите ответ на задачу.


Пример 1
input: 3
input: 0 0
input: 2 2
input: -2 2
output: 1

Пример 2
input: 4
input: 0 0
input: 1 1
input: 1 0
input: 0 1
output: 4
"""
