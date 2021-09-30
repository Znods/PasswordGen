#!/usr/bin/python
import string, random, time, sys, re
from sys import stdout
from password_strength import PasswordPolicy
from password_strength import PasswordStats

if len(sys.argv) < 3:
    print("Usage:\033[35m python "+sys.argv[0]+"\033[0m <\033[35mlength\033[0m> <\033[35m1\033[0m =\033[35m Unsecure \033[0m/\033[35m 0\033[0m =\033[35m Secure\033[0m>\n\033[7;49;35m-Znods\033[0m")
    sys.exit()

global a
global passwordd
global stats
global addedchars
a = 0
addedchars = 0
passwordLen = int(sys.argv[1])

while True:
    colors = random.randint(31, 37)
    colors = str(colors)
    passwordString = string.ascii_letters + string.digits + string.punctuation
    passwordd = ''.join([random.choice(passwordString) for _ in range(passwordLen)])
    stats = PasswordStats(passwordd)
    if int(sys.argv[2]) == 1:
        break
    if stats.strength() < 0.8:
        passwordLen+=1
        addedchars+=1
        sys.stdout.write("\rScore:\033[31m %0.3f\033[0m is not secure, \033[{0}mRecalculating!\033[0m".format(colors) % stats.strength())
        sys.stdout.flush()
        time.sleep(0.1)
    else:
        print("\nSecure Password! Added %d Chars" % addedchars)
        break
    
print("\n\033[4;49;37mStrength: %0.3f" % stats.strength())
print("\nLength: %s\n\033[0m" % len(passwordd))
print("\033[1;49;90mYour Password Is:\033[32m "+passwordd+"\033[0m\r\n")
