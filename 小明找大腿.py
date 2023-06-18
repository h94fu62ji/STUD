n=int(input());l1=[]
for i in range(n):
    x1=input().split()
    l1.append([x1[0],int(x1[3])/(int(x1[1])**2+int(x1[2])**2),int(x1[3])])
print(l1)  
nn=sorted(l1, key=lambda k:(k[1] , k[2]))
nn1=[x[0] for x in nn ]
print("\n".join(nn1[::-1]))