import hashlib, os
from time import sleep
from threading import Thread as td
from setup import *

u='\033[4m'
w='\033[00m'
r='\033[91;1m'
b='\033[36;1m'
y='\033[1;33m'

def stop():
    print(f'\a\n{r}•> {w}User Force it to stop!\n\a{r}•> {w}Exiting the program!\n')
    exit(1)

def corrupt():
    print(f'\a\n{r}•> {w}Password is not same as above!\n')

def succses():
    print(f'\a\n{r}•> {w}You have registered successfully {y}✓\n')

def signup():
  print(f'{w}*note:\n      If you forget your username and password then\n      it will really lock your Termux, so try to use a username and password\n      that is easy to remember.\n      {y}PRESS CTRL + C TO CANCEL THE OPERATION\n')
  try:
    usr = input(f'{r}•> {w}Enter Username {r}: {y}')
    pwd = input(f'{r}•> {w}Enter password {r}: {y}')
    conf_pwd = input(f'{r}•>{w} Confirm password {r}: {y}')
    if conf_pwd == pwd:
        enc = conf_pwd.encode()
        hash1 = hashlib.md5(enc).hexdigest()
        with open('.database.txt', 'w') as f:
             f.write(usr + '\n')
             f.write(hash1)
        f.close()
        succses()
        sleep(1)
        setup()
    else:
        corrupt()
  except EOFError:
    stop()
  except KeyboardInterrupt:
    stop()

if __name__ == '__main__':
        signup()
