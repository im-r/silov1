import hashlib, os
from time import sleep
from threading import Thread as td
from __banner__ import *

u='\033[4m'
w='\033[00m'
r='\033[91;1m'
b='\033[36;1m'
y='\033[1;33m'

def cancel():
    print(f"\a\n{r}•> {w}Sorry you can't stop this operation\n")
    sleep(1)

def corrupt():
    print(f'\n\a{r}•> {w}Login failed!\n')

def succses():
    print(f'\n\a{r}•> {w}Login successfully {y}✓\n')

def main():
    os.system('clear')
    randomlogo()
    sprint(banner)
    login()

def login():
  try:
    usr = input(f'{r}•> {w}Username {r}: {y}')
    pwd = input(f'{r}•> {w}Password {r}: {y}')
    auth = pwd.encode()
    auth_hash = hashlib.md5(auth).hexdigest()
    with open('.database.txt', 'r') as f:
        stored_usr, stored_pwd = f.read().split('\n')
        f.close()
        if usr  == stored_usr and auth_hash == stored_pwd:
         succses()
         sleep(1)
         os.system('clear')
         os.system('bash .__silo__v__1__simple__login__by__im__r')
         print('')
        else:
         corrupt()
         sleep(1)
         main()
  except EOFError:
       print('')
       cancel()
       main()
  except KeyboardInterrupt:
       cancel()
       main()

if __name__ == '__main__':
       main()
