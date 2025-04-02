number = int(input("Enter a number: "))
if number < 0:  # We're assuming that the number must be positive and 0 is not a positive number
    print("The number must be positive")
else:
    sum_num = 0
    for i in range(1, number):
        if number % i == 0:
            sum_num += i
            print(i)
    if sum_num == number:
        print(f"The number: {number} is a perfect number")
    else:
        print(f"the number: {number} is not a perfect number")
