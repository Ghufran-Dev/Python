name = input("what is your name: ")
# input always return string
print("salam" + name)


# string formatting
print(f"salam + {name}")

# more than 1 input
nam, age = input("Enter your name and age").split()
# enter with space or split(",")
print(nam,age)