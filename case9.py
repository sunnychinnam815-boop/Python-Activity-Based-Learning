w_cnt = int(input("Enter number of wards: "))
d_cnt = int(input("Enter number of days: "))
cap = int(input("Enter bed capacity per ward: "))

occ = []

for w in range(w_cnt):
    print("\nEnter daily bed occupancy for Ward", w + 1, ":")
    row = []
    for d in range(d_cnt):
        b = int(input("  Day " + str(d + 1) + ": "))
        row.append(b)
    occ.append(row)

print("\n--- Ward Utilization & Capacity Report ---")
for w in range(w_cnt):
    w_sum = 0
    viol = 0
    for d in range(d_cnt):
        w_sum = w_sum + occ[w][d]
        if occ[w][d] > cap:
            viol = viol + 1

    util_pct = (w_sum / (d_cnt * cap)) * 100
    print("Ward", w + 1, "-> Utilization:", round(util_pct, 2), "% | Capacity Violations:", viol)

peak_day = 1
max_patients = -1

for d in range(d_cnt):
    day_tot = 0
    for w in range(w_cnt):
        day_tot = day_tot + occ[w][d]
    if day_tot > max_patients:
        max_patients = day_tot
        peak_day = d + 1

print("\nPeak-Demand Period: Day", peak_day, "with", max_patients, "total patients")
