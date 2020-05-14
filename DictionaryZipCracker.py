import zipfile
import itertools
import string
from threading import Thread
import sys
import traceback

sys.tracebacklimit = 0

print('''\u001b[31m$$$$$$$$\ $$\                                        
\__$$  __|\__|                                       
   $$ |   $$\  $$$$$$\   $$$$$$\   $$$$$$\ $$$$$$$$\ 
   $$ |   $$ |$$  __$$\ $$  __$$\ $$  __$$\\____$$  |
   $$ |   $$ |$$ /  $$ |$$$$$$$$ |$$ |  \__| $$$$ _/ 
   $$ |   $$ |$$ |  $$ |$$   ____|$$ |      $$  _/   
   $$ |   $$ |\$$$$$$$ |\$$$$$$$\ $$ |     $$$$$$$$\ 
   \__|   \__| \____$$ | \_______|\__|     \________|
              $$\   $$ |                             
              \$$$$$$  |                             
               \______/''')

print('\u001b[35m1 = ZipCracker         2 = PwdList')

myLetters = string.ascii_letters + string.digits + string.punctuation


def crack(zip, pwd):
    try:
        zip.extractall(pwd=str.encode(pwd))
        print('Succes: Password is ' + pwd)
    except:
        #print('Password failed:' + pwd)
        pass


x = input('Select:')
if x == '1':
    print('ZipPath example: /home/tigerz/Desktop/CrackMe.zip')
    y = input('Path to ZIP:')
    zipFile = zipfile.ZipFile(y)
    print('Started ZipCracker')
    for i in range(1, 16):
        for j in map(''.join, itertools.product(myLetters, repeat=i)):
            t = Thread(target=crack, args=(zipFile, j))
            t.start()

if x == '2':
    print('ZipPath example: /home/tigerz/Desktop/CrackMePwdList.zip')
    y = input('Path to ZIP:')
    zipFile2 = zipfile.ZipFile(y)
    print('PasswordList example: /home/tigerz/Desktop/PwdList/List.txt')
    z = input('Path to PasswordList:')
    passwords = open(z, encoding="latin-1")
    for line in passwords.readlines():
        pwd = line.strip('\n')
        t = Thread(target=crack, args=(zipFile2, pwd))
        t.start()
