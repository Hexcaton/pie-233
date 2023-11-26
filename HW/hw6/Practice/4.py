def deposit(balance, amount, currency):
    balance += amount
    print(f"Deposited {amount} {currency}. Your new balance is {balance} {currency}.")
    return balance

def withdraw(balance, amount, currency):
    if amount <= balance:
        balance -= amount
        print(f"Withdrew {amount} {currency}. Your new balance is {balance} {currency}.")
    else:
        print("Insufficient funds. Withdrawal failed.")
    return balance

def check_balance(balance, currency):
    print(f"Your balance is {balance} {currency}.")

# Инициализация начального баланса и валюты
initial_balance = 750
initial_currency = "$"
current_balance = initial_balance

print("*********My purse*********")

action = input("Do you want to withdraw or deposit money? ").lower()

if action in ["withdraw", "deposit"]:
    amount = float(input("Enter an amount: "))
    if action == "withdraw":
        current_balance = withdraw(current_balance, amount, initial_currency)
    else:
        current_balance = deposit(current_balance, amount, initial_currency)
    check_balance(current_balance, initial_currency)
else:
    print("Invalid action.")