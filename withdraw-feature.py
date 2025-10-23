balance = float(input("Enter your initial balance: "))
deposit = float(input("Enter deposit amount: "))

balance += deposit

print(f"Initial Balance: ₹{balance - deposit}")
print(f"Deposit: ₹{deposit}")
print(f"New Balance after deposit: ₹{balance}")


balance = float(input("Enter your initial balance: "))
deposit = float(input("Enter deposit amount: "))
balance += deposit

withdraw = float(input("Enter withdrawal amount: "))
balance -= withdraw

print(f"Initial Balance: ₹{balance + withdraw - deposit}")
print(f"Deposit: ₹{deposit}")
print(f"New Balance after deposit: ₹{balance + withdraw}")
print(f"Withdraw: ₹{withdraw}")
print(f"Final Balance: ₹{balance}")
