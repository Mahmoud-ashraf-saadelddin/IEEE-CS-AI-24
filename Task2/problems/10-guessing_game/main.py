import random
# generate a random number between 1 and 100 and assign it to a variable called number
number = random.randint(1, 100)

while True:
    # taking a number from user
    user_number = int(input("enter a number between 1 and 100 "))
    if user_number < number:
        print("you should enter a higher number ")
    elif user_number > number:
        print("you should enter a lower number ")
    else:
        print(f"your number {user_number} is correct")
        break



