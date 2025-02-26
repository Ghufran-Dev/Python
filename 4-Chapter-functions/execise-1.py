# which num is greater
def greater(a,b):
    if a>b:
        return a
    return b

print(f"{greater(4,5)} is greater")


# def greatest(a,b,c):
#     if a > b and a > c:
#         return a
#     elif b > a and b>c:
#         return b
#     return c
# print(greatest(4,3,5))


# function inside function

def greatest(a, b, c):
    return greater(greater(a,b), c)
print(greatest(4,5,6))



# is palindrome
def is_palindrome(word):
    return word == word[::-1]
print(is_palindrome('ammar'))


# fibonacci series
n = 10
a, b = 0, 1
if n == 1:
    print(a)
elif n == 2:
    print(a, b)
else:
    print(a, b , end=' ')
    for i in range(0, n-2):
        c = a+b
        a = b
        b = c
        print(b,end=' ')



# default parameter
# last argument default not first
def user_info(first_name = 'muhammad', last_name = 'ghufran', age= 35):
    print(first_name)
    print(last_name)
    print(age)

user_info('')