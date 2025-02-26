name, char = input("Enter your name and character to count: ").split(",")

name =name.strip().lower()
c = name.count(char.strip().lower())
print(f"Your name is {name} length is {len(name)} and {char} is count by {c} times")