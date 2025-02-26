# string slicing [start argument : stop argument]
language = "python"
print(language[0:])
# stop argument sy 1 extra 
print(language[0:4])
print(language[-3:6])

# slicing / selecting sub sequence
print(language[0:6:2])
print(language[0::2]) # same
print(language[::2]) # same

# reverse
print(language[3::-1])