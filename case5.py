driver = input("Enter Driver Name: ")
vtype = input("Enter Vehicle Category (LIGHT / HEAVY): ").upper()
n = int(input("Enter number of violations: "))

total_fine = 0

for i in range(1, n + 1):
    print("\n--- Violation", i, "---")
    print("1: No Helmet/Seatbelt (Rs.1000) | 2: Signal Jump (Rs.2000) | 3: Overspeeding (Rs.3000)")
    code = int(input("Enter offence code (1/2/3): "))
    rep = input("Is this a repeat offence? (YES/NO): ").upper()

    if code == 1:
        fine = 1000
    elif code == 2:
        fine = 2000
    else:
        fine = 3000

    if vtype == "HEAVY":
        fine = fine + 500

    if rep == "YES":
        fine = fine * 2

    print("Penalty for Violation", i, ": Rs.", fine)
    total_fine = total_fine + fine

print("\n=== Traffic Penalty Summary ===")
print("Driver Name   :", driver)
print("Total Penalty : Rs.", total_fine)

if total_fine > 5000:
    print("Status: DISQUALIFIED (License suspended due to penalty > Rs. 5000)")
else:
    print("Status: WARNING ISSUED (License remains active)")
