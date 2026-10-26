INPUT_FILE_NAME = "input.txt"


def main():
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

                print(accounts.get(name, "ERROR"))
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


if __name__ == "__main__":
    main()
