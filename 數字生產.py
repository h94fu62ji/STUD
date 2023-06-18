import random 
b=[]
for j in range(10000):
    a=""
    for i in range(8):
        a+=str(random.randint(0,9))
    b.append(a)
c="\n".join(b)
"""print(c)"""
with open("我的發票.txt","w")as f:
    f.write(c)