import random
import os

for i in range(1337):
    os.system("git add .")
    open("data.bin","w").write(str(random.randint(0,999999999999)))
    os.system('git commit -m "%s"' % i)