ID = int(input("Enter your ID: "))
if ID < 0:
    print("Invalid ID")
    exit()

divide = [i for i in range(1, ID + 1) if ID % i == 0]

print("Your divisors are:", divide)