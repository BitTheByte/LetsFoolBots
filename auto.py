import random
import os

os.system("git add .")
for i in range(1337):
    open("data.bin","w").write(str(random.randint(0,999999999999)))
    os.system('git commit -m "%s"' % i)