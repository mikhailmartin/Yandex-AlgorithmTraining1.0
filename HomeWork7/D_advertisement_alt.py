"""
Реклама

Ограничение времени - 1 секунда
Ограничение памяти - 64Mb
Ввод - стандартный ввод или input.txt
Вывод - стандартный вывод или output.txt

Фирма NNN решила транслировать свой рекламный ролик в супермаркете XXX. Однако
денег, запланированных на рекламную кампанию, хватило лишь на две трансляции
ролика в течение одного рабочего дня.

Фирма NNN собрала информацию о времени прихода и времени ухода каждого
покупателя в некоторый день. Менеджер по рекламе предположил, что и на следующий
день покупатели будут приходить и уходить ровно в те же моменты времени.

Помогите ему определить моменты времени, когда нужно включить трансляцию
рекламных роликов, чтобы как можно большее количество покупателей прослушало
ролик целиком от начала до конца хотя бы один раз. Ролик длится ровно 5 единиц
времени. Трансляции роликов не должны пересекаться, то есть начало второй
трансляции должно быть хотя бы на 5 единиц времени позже, чем начало первой.

Если трансляция ролика включается, например, в момент времени 10, то покупатели,
пришедшие в супермаркет в момент времени 10 (или раньше) и уходящие из
супермаркета в момент 15 (или позднее) успеют его прослушать целиком, а,
например, покупатель, пришедший в момент времени 11, равно как и покупатель,
уходящий в момент 14 - не успеют. Если покупатель успевает услышать только конец
первой трансляции ролика (не сначала) и начало второй трансляции (не до конца),
то считается, что он не услышал объявления. Если покупатель успевает услышать
обе трансляции ролика, то при подсчёте числа людей, прослушавших ролик, он всё
равно учитывается всего один раз (фирме важно именно количество различных людей,
услышавших ролик).


Формат ввода:
В первой строке входного файла вводится число N - количество покупателей (1 ≤ N ≤ 2000).
В следующих N строках записано по паре натуральных чисел - время прихода и
время ухода каждого из них. Все значения времени - натуральные числа,
не превышающие 10^9. Время ухода человека из супермаркета всегда строго больше
времени его прихода в супермаркет.


Формат вывода:
Выведите через пробел три числа: количество покупателей, которые прослушают
ролик целиком от начала до конца хотя бы один раз, и моменты времени, когда
должна начинаться трансляция ролика. Моменты времени должны быть выведены в
возрастающем порядке и должны быть натуральными числами, не превышающими 2·10^9.
Если вариантов ответа несколько, выведите любой из них.


Пример 1
input: 4
input: 1 11
input: 1 3
input: 6 15
input: 1 6
output: 3 1 6

Пример 2
input: 1
input: 1 10
output: 1 3 25

Пример 3
input: 3
input: 1 10
input: 11 20
input: 21 30
output: 2 1 22


Примечания:
1. Трансляция роликов начинается в моменты времени 1 и 6. Первое объявление
успевают прослушать покупатели номер 1 и 4, второе - 1 и 3. Когда бы ни
начиналась трансляция объявления, 2-й покупатель не сможет его прослушать,
так как находится в супермаркете менее 5 минут. Приведённый ответ является
не единственным верным ответом на этот тест.

2. Объявление, трансляция которого начинается в момент 3, единственный
покупатель обязательно услышит. Вторую трансляцию (раз она оплачена) мы можем
сделать когда угодно, например, в 25 минут в пустом супермаркете (впрочем, мы
не можем начать трансляцию второго объявления, например, в момент 7 - т.к. к
этому моменту ещё не закончится первая трансляция)

3. Объявление услышат лишь 2 из 3-х покупателей.
"""
from dataclasses import dataclass
from enum import IntEnum
from typing import Self


class EventType(IntEnum):
    IN = 0
    START = 1
    END = 2
    OUT = 3


@dataclass
class ProblemInput:
    n: int
    customers: list[tuple[int, int]]


class Solver:
    def __init__(self, data: ProblemInput, promo: int = 5) -> None:
        self.data = data
        self.promo = promo

    @classmethod
    def from_stdin(cls) -> Self:

        n = int(input())
        customers = []
        for _ in range(n):
            time_in, time_out = map(int, input().split())
            customers.append((time_in, time_out))

        return cls(ProblemInput(n, customers))

    @classmethod
    def from_strings(cls, lines: list[str]) -> Self:

        n = int(lines[0])
        customers = []
        for i in range(n):
            time_in, time_out = map(int, lines[i+1].split())
            customers.append((time_in, time_out))

        return cls(ProblemInput(n, customers))

    def solve(self) -> tuple[int, int, int]:

        events = []
        seen = set()
        for i, (time_in, time_out) in enumerate(self.data.customers):
            if time_out - time_in >= self.promo:
                events.append((time_in, EventType.IN, i))
                events.append((time_out, EventType.OUT, i))

                time_start = time_in
                time_end = time_in + self.promo
                if time_start not in seen:
                    events.append((time_start, EventType.START, i))
                    events.append((time_end, EventType.END, i))
                    seen.add(time_start)

                time_start = time_out - self.promo
                time_end = time_out
                if time_start not in seen:
                    events.append((time_start, EventType.START, i))
                    events.append((time_end, EventType.END, i))
                    seen.add(time_start)
        events.sort()

        curr_active = 0
        start_active = dict()
        time_active: dict[int, int] = dict()
        for time, event_type, i in events:
            if event_type == EventType.OUT:
                curr_active &= ~(1 << i)
            elif event_type == EventType.IN:
                curr_active |= 1 << i
            elif event_type == EventType.START:
                start_active[time] = curr_active
            elif event_type == EventType.END:
                start_time = time - self.promo
                before_active = start_active[start_time]
                time_active[start_time] = before_active & curr_active
        del events

        time_active: list[tuple[int, int]] = list(time_active.items())
        n = len(time_active)

        max_customers = 0
        start1 = 1
        start2 = 1 + self.promo
        for i in range(n):
            time1, active1 = time_active[i]

            if active1.bit_count() > max_customers:
                max_customers = active1.bit_count()
                start1 = time1
                start2 = time1 + self.promo

            for j in range(i+1, n):
                time2, active2 = time_active[j]

                if abs(time1 - time2) < self.promo:
                    continue

                customers = active1 | active2
                if customers.bit_count() > max_customers:
                    max_customers = customers.bit_count()
                    start1 = time1
                    start2 = time2

        return max_customers, *sorted([start1, start2])


def main() -> None:

    solver = Solver.from_stdin()
    result = solver.solve()

    print(*result)


if __name__ == "__main__":
    main()
