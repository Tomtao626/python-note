import random

checkcode = ''
for i in range(4):
    current = random.randrange(1,9)
    if current == i:
        tmp = chr(random.randrange(65,90))
    else:
        tmp = random.randint(0,9)
    checkcode += str(tmp)
print(checkcode)
