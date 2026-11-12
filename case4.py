n = int(input("Enter number of products: "))
min_stk = int(input("Enter minimum stock target per product: "))

for i in range(1, n + 1):
    print("\n--- Product", i, "---")
    pname = input("Enter product name: ")
    op = int(input("Enter opening stock: "))
    inc = int(input("Enter incoming quantity: "))
    disp = int(input("Enter dispatched quantity: "))
    cl = int(input("Enter actual closing stock: "))

    exp = op + inc - disp
    print("Expected Closing Stock:", exp, "| Actual Closing Stock:", cl)

    if exp != cl:
        diff = exp - cl
        print("ALERT: Discrepancy detected! Difference:", diff, "units")
    else:
        print("Stock Status: Matched (No Discrepancy)")

    if cl < min_stk:
        rep = min_stk - cl
        print("Replenishment Required:", rep, "units")
    else:
        print("Replenishment Required: 0 units")
