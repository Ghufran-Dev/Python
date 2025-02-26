# and or
# watch a movie
# name starts with a or A and age = 19

name = 'Ammar'
age = 19
# if name[0].lower() == 'a' and age == 19:
if name.startswith('a') or name.startswith('A') and age == 19:
# if name[0] == "A" or name[0] == 'a' and age == 19:
    print('you can watch movie')
else:
    print('sorry')