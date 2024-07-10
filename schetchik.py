import os
if not os.path.exists('number.txt'):
    print('меня открыли 1 раз')
    number = open('number.txt', 'w+')
    number.write('1')
    number.close()
    exit()

number=open('number.txt','r')
numbers=number.read()
number.close()

chislo=int(numbers)
corect=chislo+1
print('меня открыли '+str(corect)+' раз')

number=open('number.txt','w+')
number.write(str(corect))
number.close()
