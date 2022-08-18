import random
import os

i = 0
while True:
    os.system("git add .")
    open("data.bin.py","w").write(str(random.randint(0,999999999999)))
    os.system('git commit -m "%s"' % i)
    i += 1