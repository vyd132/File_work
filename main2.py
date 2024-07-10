import os
if os.path.exists('save.txt'):
    save=open('save.txt','r')
    text= save.read()
    print(text)
    save.close()