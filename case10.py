init_books = int(input("Enter total books owned by library: "))
n = int(input("Enter number of borrowing records: "))

records = []

for i in range(1, n + 1):
    print("\n--- Borrowing Record", i, "---")
    bid = input("Enter Book ID: ").upper()
    taken = int(input("Enter days borrowed: "))
    allowed = int(input("Enter allowed borrowing days: "))
    ret = input("Is book returned? (YES/NO): ").upper()
    records.append((bid, taken, allowed, ret))

total_fine = 0
overdue_books = []
unreturned_cnt = 0

print("\n--- Fine Calculation Details ---")
for i in range(n):
    bid, taken, allowed, ret = records[i]

    if taken > allowed:
        delay = taken - allowed
        fine = delay * 10
        total_fine = total_fine + fine
        overdue_books.append(bid)
        print(bid, "-> Overdue by", delay, "days | Fine: Rs.", fine)
    else:
        print(bid, "-> Returned on time | Fine: Rs. 0")

    if ret == "NO":
        unreturned_cnt = unreturned_cnt + 1

avail_books = init_books - unreturned_cnt

print("\n=== Library Reconciliation Summary ===")
print("Total Fine Collected   : Rs.", total_fine)
print("Overdue Book IDs       :", overdue_books)
print("Books Still Borrowed   :", unreturned_cnt)
print("Available Books Now    :", avail_books)
