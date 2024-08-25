"""
Банковские счета

Ограничение времени - 1 секунда
Ограничение памяти - 64Mb
Ввод - стандартный ввод или input.txt
Вывод - стандартный вывод или output.txt

Некоторый банк хочет внедрить систему управления счетами клиентов,
поддерживающую следующие операции:
- Пополнение счета клиента.
- Снятие денег со счета.
- Запрос остатка средств на счете.
- Перевод денег между счетами клиентов.
- Начисление процентов всем клиентам.

Вам необходимо реализовать такую систему. Клиенты банка идентифицируются именами
(уникальная строка, не содержащая пробелов). Первоначально у банка нет ни одного
клиента. Как только для клиента проводится операция пополнения, снятия или
перевода денег, ему заводится счет с нулевым балансом. Все дальнейшие операции
проводятся только с этим счетом. Сумма на счету может быть как положительной,
так и отрицательной, при этом всегда является целым числом.


Формат ввода:
Входной файл содержит последовательность операций. Возможны следующие операции:
DEPOSIT name sum - зачислить сумму sum на счет клиента name. Если у клиента нет
счета, то счет создается. WITHDRAW name sum - снять сумму sum со счета клиента
name. Если у клиента нет счета, то счет создается. BALANCE name - узнать остаток
средств на счету клиента name. TRANSFER name1 name2 sum - перевести сумму sum со
счета клиента name1 на счет клиента name2. Если у какого-либо клиента нет счета,
то ему создается счет. INCOME p - начислить всем клиентам, у которых открыты
счета, p% от суммы счета. Проценты начисляются только клиентам с положительным
остатком на счету, если у клиента остаток отрицательный, то его счет не
меняется. После начисления процентов сумма на счету остается целой, то есть
начисляется только целое число денежных единиц. Дробная часть начисленных
процентов отбрасывается.


Формат вывода:
Для каждого запроса BALANCE программа должна вывести остаток на счету данного
клиента. Если же у клиента с запрашиваемым именем не открыт счет в банке,
выведите ERROR.


Пример 1
input: DEPOSIT Ivanov 100
input: INCOME 5
input: BALANCE Ivanov
input: TRANSFER Ivanov Petrov 50
input: WITHDRAW Petrov 100
input: BALANCE Petrov
input: BALANCE Sidorov
output: 105
output: -50
output: ERROR

Пример 2
input: BALANCE Ivanov
input: BALANCE Petrov
input: DEPOSIT Ivanov 100
input: BALANCE Ivanov
input: BALANCE Petrov
input: DEPOSIT Petrov 150
input: BALANCE Petrov
input: DEPOSIT Ivanov 10
input: DEPOSIT Petrov 15
input: BALANCE Ivanov
input: BALANCE Petrov
input: DEPOSIT Ivanov 46
input: BALANCE Ivanov
input: BALANCE Petrov
input: DEPOSIT Petrov 14
input: BALANCE Ivanov
input: BALANCE Petrov
output: ERROR
output: ERROR
output: 100
output: ERROR
output: 150
output: 110
output: 165
output: 156
output: 165
output: 156
output: 179

Пример 3
input: BALANCE a
input: BALANCE b
input: DEPOSIT a 100
input: BALANCE a
input: BALANCE b
input: WITHDRAW a 20
input: BALANCE a
input: BALANCE b
input: WITHDRAW b 78
input: BALANCE a
input: BALANCE b
input: WITHDRAW a 784
input: BALANCE a
input: BALANCE b
input: DEPOSIT b 849
input: BALANCE a
input: BALANCE b
output: ERROR
output: ERROR
output: 100
output: ERROR
output: 80
output: ERROR
output: 80
output: -78
output: -704
output: -78
output: -704
output: 771
"""
INPUT_FILE_NAME = "input.txt"


if __name__ == "__main__":

    input_file = open(INPUT_FILE_NAME, "r", encoding="utf8")

    accounts = dict()
    for line in input_file:

        line = line.split()
        operation_type = line[0]

        match operation_type:
            case "DEPOSIT":
                name = line[-2]
                summ = int(line[-1])

                accounts[name] = accounts.get(name, 0) + summ
            case "WITHDRAW":
                name = line[-2]
                summ = int(line[-1])

                accounts[name] = accounts.get(name, 0) - summ
            case "BALANCE":
                name = line[-1]

                print(accounts.get(name, 'ERROR'))
            case "TRANSFER":
                name1 = line[-3]
                name2 = line[-2]
                summ = int(line[-1])

                accounts[name1] = accounts.get(name1, 0) - summ
                accounts[name2] = accounts.get(name2, 0) + summ
            case "INCOME":
                p = int(line[-1])

                for name in accounts:
                    if accounts[name] > 0:
                        accounts[name] += int(accounts[name] * (p / 100))
