d1={"A":10,"B":11,"C":12,"D":13,"E":14,"F":15,"G":16,
    "H":17,"I":34,"J":18,"K":19,"M":21,"N":22,"O":35,
    "P":23,"Q":24,"T":27,"U":28,"V":29,"W":32,"X":30,"Z":33}
x1="19876543211"
x2="12"
x3=0
a1=input();a2=input()
y1=str(d1.get(a1))+x2[0]+str(a2)
for i in range(len(x1)):
    x3+=int(x1[i])*int(y1[i])
if x3%10==0:
    print("Male")
else:
    print("Female")
#https://judge.ccclub.io/contest/170/problem/03