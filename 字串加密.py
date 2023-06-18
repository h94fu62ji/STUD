a1=input();a2=input();x=""
while len(a1) > len(a2):
    a2+=a2
for i in range(len(a1)):
    x+=chr(ord(a1[i])+int(a2[i]))
print(x)
#https://judge.ccclub.io/contest/170/problem/02