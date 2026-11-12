n = int(input("Enter number of transactions: "))
thresh = float(input("Enter high-value threshold limit (Rs): "))

seen_ids = []
dup_ids = []
high_val_ids = []
suspicious = []

for i in range(1, n + 1):
    print("\n--- Transaction", i, "---")
    tid = input("Enter Transaction ID: ").upper()
    amt = float(input("Enter Transaction Amount: "))

    if tid in seen_ids:
        if tid not in dup_ids:
            dup_ids.append(tid)
        if tid not in suspicious:
            suspicious.append(tid)
    else:
        seen_ids.append(tid)

    if amt > thresh:
        high_val_ids.append(tid)
        if tid not in suspicious:
            suspicious.append(tid)

print("\n=== Fraud & Duplicate Detection Report ===")
print("Duplicate Transaction IDs  :", dup_ids)
print("Threshold Violation IDs    :", high_val_ids)
print("All Suspicious Entries     :", suspicious)
