# number guessing game


import random
winning_number = random.randint(1,10)
user_number = int(input("Enter your desired number: "))
# print(winning_number)
while True:
    if user_number == winning_number:
        print("you win")
        break
    else: # nested if else
        if user_number > winning_number:
            print('too high')
        else:
            print("too low")
    user_number = int(input("Enter your desired number: "))
    