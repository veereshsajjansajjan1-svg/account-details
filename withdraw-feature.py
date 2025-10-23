balance = float(input("Enter your initial balance: "))
deposit = float(input("Enter deposit amount: "))

balance += deposit

print(f"Initial Balance: ₹{balance - deposit}")
print(f"Deposit: ₹{deposit}")
print(f"New Balance after deposit: ₹{balance}")
