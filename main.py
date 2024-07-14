MAX_LINES = 3
MAX_BET = 200
MIN_BET = 1

def deposit():
    while True:
        amount = input("Enter Deposit amount, Ksh: ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Enter amount greater than 0.")
        else:
            print("Please enter a number.")

    return amount


def lines_to_bet():
    while True:
        lines = input("Enter number of lines to bet on(1-" + str(MAX_LINES) + "): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter Lines greater than 0 and upto " + str(MAX_LINES) + " lines please!")
        else:
            print("Please enter a number.")

    return lines


def get_bet():
    while True:
        amount = input("Enter Deposit amount, Ksh: ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Enter amount greater than 0.")
        else:
            print("Please enter a number.")

    return amount


def main():
    balance = deposit()
    lines = lines_to_bet()
    print(balance, lines)


main()
