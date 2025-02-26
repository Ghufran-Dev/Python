n = '1234'
total = 0
for i in range(len(n)):
    total += int(n[i])
print(total)

name = 'ammar '
temp =''
for i in range(0, len(name)):
    if name[i] not in temp:
        temp += name[i]
        print(f"{name[i]} : {name.count(name[i])}")




# break and continue
# step argument in range
for i in range(0, 11, 2):
    print(i,end=' ')
print('\n')

# for i in range(10, -1, -2):
for i in range(0, 11, -2):
    print(i, end=" ")


name = 'ammar'
for i in range(len(name)):
    print(name[i], end='')

for i in name:
    print(i, end=' ')