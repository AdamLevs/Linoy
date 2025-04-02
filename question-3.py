import random

lowest_num = (int(input("What is the lowest number: ")))
highest_num = (int(input("What is the highest number: ")))
chances = (int(input("How many chances do you want: ")))

random_num = random.randint(lowest_num, highest_num)
print("random_num:", random_num)

for i in range(chances):
    guess = (int(input("Guess the number: ")))
    if guess == random_num:
        print("You WON!", "it took you", i + 1, "chances")
        break
    elif i == chances - 1:
        print("You lost! The number was:", random_num)
        break
    elif guess < random_num:
        print("The number is lower than the random number")
    else:
        print("The number is higher than the random number")
