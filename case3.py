bal = float(input("Enter opening account balance: "))
n = int(input("Enter number of transactions: "))

valid_cnt = 0
rej_cnt = 0

for i in range(1, n + 1):
    print("\n--- Transaction", i, "---")
    ttype = input("Enter type (D for Deposit / W for Withdrawal): ").upper()
    amt = float(input("Enter amount: "))

    if amt <= 0:
        print("Rejected: Amount must be greater than zero.")
        rej_cnt = rej_cnt + 1
    elif ttype == "D":
        bal = bal + amt
        valid_cnt = valid_cnt + 1
        print("Deposit successful. Updated Balance: Rs.", bal)
    elif ttype == "W":
        if amt > 20000:
            print("Rejected: Exceeds Rs. 20000 withdrawal limit.")
            rej_cnt = rej_cnt + 1
        elif amt > bal:
            print("Rejected: Insufficient balance.")
            rej_cnt = rej_cnt + 1
        else:
            bal = bal - amt
            valid_cnt = valid_cnt + 1
            print("Withdrawal successful. Updated Balance: Rs.", bal)
    else:
        print("Rejected: Invalid transaction type.")
        rej_cnt = rej_cnt + 1

print("\n=== ATM Transaction Summary ===")
print("Final Account Balance  : Rs.", bal)
print("Successful Transactions:", valid_cnt)
print("Rejected Transactions  :", rej_cnt)
