import random

MAX_LINES = 3
MAX_BET = 200
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4
    "C": 6,
    "D": 8
}

def get_slot_machine_spin(rows, cols, symbols):
    


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
        bet_amount = input("Enter Bet amount on each line, Ksh: ")
        if bet_amount.isdigit():
            bet_amount = int(bet_amount)
            if MIN_BET <= bet_amount <= MAX_BET:
                break
            else:
                print(f"Enter amount must be between Ksh.{MIN_BET} - Ksh.{MAX_BET}.")
        else:
            print("Please enter a number.")

    return bet_amount


def main():
    balance = deposit()
    lines = lines_to_bet()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have sufficient funds to make this bet, your balance is Ksh.{balance}")
        else:
            break    

    print(f"You are betting Ksh.{bet} on {lines} lines. Total bet is equal to: Ksh.{total_bet}")



main()
