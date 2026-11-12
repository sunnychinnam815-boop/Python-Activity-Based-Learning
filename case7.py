n = int(input("Enter number of records to validate: "))

for i in range(1, n + 1):
    print("\n--- Student Record", i, "---")
    sid = input("Enter 8-character Student ID: ")
    email = input("Enter College Email: ").lower()

    # Validate Student ID
    if len(sid) != 8:
        print("ID Status   : INVALID (Must be exactly 8 characters)")
    elif not sid.isalnum():
        print("ID Status   : INVALID (Contains invalid special characters)")
    else:
        print("ID Status   : VALID")

    # Validate Email
    if email.count("@") != 1:
        print("Email Status: INVALID (Missing or multiple '@' separator)")
    elif email[0] == "@":
        print("Email Status: INVALID (Missing username before '@')")
    elif not email.endswith(".edu.in"):
        print("Email Status: INVALID (Must end with '.edu.in' domain)")
    else:
        print("Email Status: VALID")
