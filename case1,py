name = input("Enter employee name: ")
basic = float(input("Enter basic pay: "))
allow = float(input("Enter allowances: "))
ot = float(input("Enter overtime pay: "))
inc = float(input("Enter incentives: "))

gross = basic + allow + ot + inc

if gross > 50000:
    ded = gross * 0.15
elif gross > 30000:
    ded = gross * 0.10
else:
    ded = gross * 0.05

net = gross - ded

print("\n--- Employee Salary Statement ---")
print("Employee Name    :", name)
print("Gross Salary     : Rs.", round(gross, 2))
print("Total Deductions : Rs.", round(ded, 2))
print("Net Salary       : Rs.", round(net, 2))
