"""
Кондиционер

Ограничение времени - 1 секунда
Ограничение памяти - 64Mb
Ввод - стандартный ввод или input.txt
Вывод - стандартный вывод или output.txt

В офисе, где работает программист Петр, установили кондиционер нового типа.
Этот кондиционер отличается особой простотой в управлении. У кондиционера есть
всего лишь два управляемых параметра: желаемая температура и режим работы.

Кондиционер может работать в следующих четырех режимах:
* «freeze» — охлаждение. В этом режиме кондиционер может только уменьшать
температуру. Если температура в комнате и так не больше желаемой, то он
выключается.
* «heat» — нагрев. В этом режиме кондиционер может только увеличивать
температуру. Если температура в комнате и так не меньше желаемой, то он
выключается.
* «auto» — автоматический режим. В этом режиме кондиционер может как
увеличивать, так и уменьшать температуру в комнате до желаемой.
* «fan» — вентиляция. В этом режиме кондиционер осуществляет только вентиляцию
воздуха и не изменяет температуру в комнате.

Кондиционер достаточно мощный, поэтому при настройке на правильный режим работы
он за час доводит температуру в комнате до желаемой.

Требуется написать программу, которая по заданной температуре в комнате t_room,
установленным на кондиционере желаемой температуре t_cond и режиму работы
определяет температуру, которая установится в комнате через час.


Формат ввода:
Первая строка входного файла содержит два целых числа t_room, и t_cond,
разделенных ровно одним пробелом (–50 ≤ t_room ≤ 50, –50 ≤ t_cond ≤ 50).

Вторая строка содержит одно слово, записанное строчными буквами латинского
алфавита — режим работы кондиционера.


Формат вывода:
Выходной файл должен содержать одно целое число — температуру, которая
установится в комнате через час.


Примеры:
Пример 1
input: 10 20
input: heat
output: 20

Пример 2
input: 10 20
input: freeze
output: 10


Примечания
В первом примере кондиционер находится в режиме нагрева. Через час он нагреет
комнату до желаемой температуры в 20 градусов.

Во втором примере кондиционер находится в режиме охлаждения. Поскольку
температура в комнате ниже, чем желаемая, кондиционер самостоятельно
выключается и температура в комнате не поменяется.
"""
t_room, t_cond = map(int, input().split())
mode = input()

match mode:
    case "freeze":
        t_result = t_cond if t_room >= t_cond else t_room
    case "heat":
        t_result = t_cond if t_cond >= t_room else t_room
    case "auto":
        t_result = t_cond
    case "fan":
        t_result = t_room
    case _:
        assert False

print(t_result)