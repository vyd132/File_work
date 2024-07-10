import os
if not os.path.exists('name.txt'):
    your_name=input('Здесь пока никого не было, как тебя зовут?')
    name = open('name.txt', 'w+')
    name.write(your_name)
    name.close()
    exit()

name=open('name.txt','r')
my_name=name.read()
name.close()

if my_name=='никто':
    your_name = input('Здесь пока никого не было, как тебя зовут?')
else:
    your_name=input('Раньше здесь был '+my_name+" как тебя зовут?")

name=open('name.txt','w+')
name.write(your_name)
name.close()