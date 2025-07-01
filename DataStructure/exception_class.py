class InsufficientFundsError(Exception): pass
balance=10000
try:
    amount=int(input("Enter amount to withdraw: "))
    if amount<=0:
        raise ValueError("Withdrawl amount must be greater than 0")
    if amount>balance:
        raise InsufficientFundsError("Insufficient balance")
    balance-=amount
    print(f"Withdrawl successful! Remaining balance: {balance}")
except ValueError as ve:
    print("Invalid input: ",ve)
except InsufficientFundsError as ie:
    print("Trnasaction failed :",ie)