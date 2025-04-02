age = int(input("How old are you: "))

if age < 0 or age > 120:
    print("Invalid age")
    exit()

work = int(input("Choose your work: \n1.kid\n2.student\n3.worker\n4.retired\n"))
if work not in [1, 2, 3, 4]:
    print("Invalid work choice")
    exit()

membership = input("Do you have a membership? (yes/no): ")

price = 100

if age <= 12:
    price *= 0.5

if work == 2 or work == 4:
    price *= 0.7
elif work == 1:
    print("Your final price is:", price)
    exit()

if membership == "yes":
    if work == 3:
        price *= 0.9
    elif work == 2 or work == 4:
        price *= 0.6
elif membership != "no":
    print("Invalid membership input")
    exit()

print("Your final price is:", price)
