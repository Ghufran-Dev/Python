# exercise one of three
# sum of n natural numbers
# ask n number
# print total from 1 to n

# exercise 1
# n = int(input("Enter number: "))
# total = 0
# i = 1
# while i<=n:
#     total+=i
#     i +=1
# print(total)

# exercise 2
# ask 2 digit number
# calculate 1+2+3+4 and print

# num = '1234'
# total = 0
# i = 0
# while i < len(num):
#     total += int(num[i])
#     i +=1
# print(total)


# exercise 3
# from name count each word
name = 'ammar '
temp=''
i = 0
while i < len(name):
    if name[i] not in temp:
        temp +=  name[i]
        print(f"{name[i]} = {name.count(name[i])}")
    i+=1