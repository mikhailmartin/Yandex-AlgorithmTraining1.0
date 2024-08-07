"""
Скорая помощь

Ограничение времени - 1 секунда
Ограничение памяти - 64Mb
Ввод - стандартный ввод или input.txt
Вывод - стандартный вывод или output.txt

Бригада скорой помощи выехала по вызову в один из отделенных районов.
К сожалению, когда диспетчер получил вызов, он успел записать только адрес дома
и номер квартиры K_1, а затем связь прервалась. Однако он вспомнил, что по
этому же адресу дома некоторое время назад скорая помощь выезжала в
квартиру K_2, которая расположена в подъезде P_2 на этаже N_2. Известно, что в
доме M этажей и количество квартир на каждой лестничной площадке одинаково.
Напишите программу, которая вычисляет номер подъезда P_1 и номер этажа N_1
квартиры K_1.


Формат ввода:
Во входном файле записаны пять положительных целых чисел K_1, M, K_2, P_2, N_2.
Все числа не превосходят 10^6.


Формат вывода:
Выведите два числа P_1 и N_1. Если входные данные не позволяют однозначно
определить P_1 или N_1, вместо соответствующего числа напечатайте 0. Если
входные данные противоречивы, напечатайте два числа –1 (минус один).


Пример 1
input: 89 20 41 1 11
output: 2 3

Пример 2
input: 11 1 1 1 1
output: 0 1

Пример 3
input: 3 2 2 2 1
output: -1 -1
"""


def main(k1: int, m: int, k2: int, p2: int, n2: int) -> tuple[int, int]:

    entrance_number1 = -1
    floor_number1 = -1
    flag = False

    for flat_number in range(1, 1_000_000+1):  # количество квартир на этаже

        entrance, floor = validate(k1, m, k2, p2, n2, flat_number)

        if entrance != -1:
            flag = True
            if entrance_number1 == -1:
                entrance_number1, floor_number1 = entrance, floor
            elif entrance_number1 != entrance and entrance_number1 != 0:
                entrance_number1 = 0
            elif floor_number1 != floor and floor != 0:
                floor_number1 = 0

    if flag:
        return entrance_number1, floor_number1
    else:
        return -1, -1


def validate(
    k1: int, m: int, k2: int, p2: int, n2: int, flat_number: int
) -> tuple[int, int]:

    def get_entrance_and_floor(k: int, m: int, flat_number: int) -> tuple[int, int]:

        # номер лестничной площадки из всех площадок в доме
        landing_number = ((k - 1) // flat_number) + 1
        # номер подъезда
        entrance_number = ((landing_number - 1) // m) + 1
        # номер этажа
        floor_number = ((landing_number - 1) % m) + 1

        return entrance_number, floor_number

    entrance_number2, floor_number2 = get_entrance_and_floor(k2, m, flat_number)

    if p2 == entrance_number2 and n2 == floor_number2:
        entrance_number1, floor_number1 = get_entrance_and_floor(k1, m, flat_number)
    else:
        entrance_number1, floor_number1 = -1, -1

    return entrance_number1, floor_number1


if __name__ == "__main__":

    # k1, m, k2, p2, n2 = map(int, input().split())
    # k1, m, k2, p2, n2 = 89, 20, 41, 1, 11
    # k1, m, k2, p2, n2 = 11, 1, 1, 1, 1
    k1, m, k2, p2, n2 = 3, 2, 2, 2, 1

    p1, n1 = main(k1, m, k2, p2, n2)

    print(p1, n1)
