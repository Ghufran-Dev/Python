x=5 # global variable
def func():
    # global x
    x=7 # local variable
    return x

def func2():
    return x

print(func())
# print(func2())
print(x)