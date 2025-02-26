# intro
# print vs return
def add_two(a, b):
    return a+b

total = add_two(5, 4)
print(total)

# functions practice
def last_char(name):
    return name[-1]

print(last_char('ammar'))

# odd even
def odd_even(n):
    if n%2 ==0:
        print('even')
        # return 'even'
    else:
        print('odd')

odd_even(2)

# def is_even(n):
#     if n%2 ==0:
#         return True
#     return False

def is_even(n):
    return n%2 ==0

print(is_even(9))