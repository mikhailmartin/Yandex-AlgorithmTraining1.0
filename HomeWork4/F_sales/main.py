INPUT_FILE_NAME = "input.txt"


def main():
    input_file = open(INPUT_FILE_NAME, "r", encoding="utf8")

    customers = dict()
    for line in input_file:

        customer, product, num = line.split()
        num = int(num)

        customers[customer] = customers.get(customer, dict())
        customers[customer][product] = customers[customer].get(product, 0) + num

    for customer in sorted(customers):
        print(customer, ":", sep="")
        for product in sorted(customers[customer]):
            print(product, customers[customer][product])


if __name__ == "__main__":
    main()
