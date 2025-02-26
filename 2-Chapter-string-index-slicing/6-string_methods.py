# len function also count spaces
name = "aMMar  "
print(len(name))


# lower
print(name.lower())

# upper
print(name.upper())

# title
print(name.title())

# count
print(name.count('M'))

# strip  lstring rstring
print(name.strip())

# replace
# name.replace(" ", "")

girl = "she is Beautiful and she is good dancer"
# print(girl.replace(" ", "_"))
print(girl.replace("is", "was", 1))

# find method use to find the position of character in string
is_position = girl.find("is")
print(girl.find("is", is_position +1))



# center method
print(name.center(11, "*"))
print(name.center(len(name)+8, "*"))