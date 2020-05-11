import zipfile
import itertools
import string
from threading import Thread
import sys

sys.tracebacklimit=0
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

print('\u001b[35m1 = ZipCracker')
x = input('Select:')
if x == '1':
    print('ZipPath example: /home/tigerz/Desktop/CrackMe.zip')
    y = input('Path to ZIP:')
    print('Started ZipCracker')
    def crack(zip, pwd):
        try:
            zip.extractall(pwd=str.encode(pwd))
            print('Succes: Password is ' + pwd)
        except:
            print('Password failed:' + pwd)
            pass

zipFile = zipfile.ZipFile(y)
myLetters = string.ascii_letters + string.digits + string.punctuation
for i in range (1, 16):
    for j in map(''.join, itertools.product(myLetters, repeat=i)):
        t = Thread(target=crack, args=(zipFile, j))
        t.start()