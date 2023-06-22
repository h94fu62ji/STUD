x=int(input())
liss=[[1]]
if x == 1:
    print(liss)
elif x == 2:
    liss.append([1,1])
    print(liss)
else:
    liss.append([1,1])
    for j in range(1,x-1):

        lis1=liss[j]
        lis2=[1]
        for i in range(j):
            
            lis2.append(lis1[i] + lis1[i+1])
        lis2.append(1)
        liss.append(lis2)
    #print(liss)
    for k in liss:
        print(k)