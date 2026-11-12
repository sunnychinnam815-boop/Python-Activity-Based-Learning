venue = float(input("Enter venue cost: "))
equip = float(input("Enter equipment cost: "))
cater = float(input("Enter catering cost: "))
trans = float(input("Enter transport cost: "))
cert = float(input("Enter certificate cost: "))

sponsor = float(input("Enter sponsorship amount received: "))
fee = float(input("Enter registration fee per student: "))
count = int(input("Enter actual number of registered participants: "))

total_cost = venue + equip + cater + trans + cert
contrib = count * fee
total_collected = sponsor + contrib

rem_needed = total_cost - sponsor
if rem_needed <= 0:
    min_reg = 0
else:
    min_reg = int((rem_needed + fee - 1) // fee)

print("\n--- Campus Event Financial Report ---")
print("Total Event Cost          : Rs.", total_cost)
print("Participant Contributions : Rs.", contrib)
print("Total Funds Collected     : Rs.", total_collected)
print("Min Registrations Needed  :", min_reg)

if total_collected < total_cost:
    shortfall = total_cost - total_collected
    print("Sponsorship/Fund Shortfall: Rs.", shortfall)
else:
    surplus = total_collected - total_cost
    print("Event Breaks Even! Surplus: Rs.", surplus)
