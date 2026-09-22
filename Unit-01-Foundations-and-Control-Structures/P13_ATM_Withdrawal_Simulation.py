correct_pin = 1234
balance = 10000.0
pin = int(input("Enter PIN: "))

if pin == correct_pin:
    amount = float(input("Enter withdrawal amount: "))
    if amount <= 0:
        print("Transaction Failed: Invalid amount entered.")
    elif amount <= balance:
        balance = balance - amount
        print(f"Transaction Successful! Withdrawal Amount: ₹{amount}")
        print(f"Remaining Balance: ₹{balance}")
    else:
        print("Transaction Failed: Insufficient balance.")
else:
    print("Transaction Failed: Incorrect PIN.")