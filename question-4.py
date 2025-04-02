numbers = []

while True:
    user_input = input("Enter a number: ")
    if user_input == "stop":
        break
    if user_input.isdigit():
        numbers.append(int(user_input))
    else:
        print("You can only enter numbers or write 'stop' to stop the program")

total_sum = 0
all_even = True
for i in numbers:
    total_sum += i
    if i % 2 != 0:
        all_even = False
    else:
        continue

print("The total sum is:", total_sum)

if all_even:
    print("All the numbers are even")
else:
    print("Not all the numbers are even")

