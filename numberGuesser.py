number = int(input("Guess a number between 1 and 100: "))
if (number > 27):
    print("Your guess was too high.")
elif (number < 27):
    print("Your guess was too low.")
else:
    print("Your guess was correct!")