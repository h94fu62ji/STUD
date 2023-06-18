a1 = [int(i) for i in input().split()];x1=1
def abs1(i):
    return(abs(i))
a1 = sorted(a1 ,key = abs1 ,reverse= True)
#print(a1)
if len(a1) == 4:
    for i in range(4):
        x1*=a1[i]
else :
    x2,x3,x4=1,1,1
    for i in range(4):
        x2*=a1[i]
    for i in range(1,5):
        x3*=a1[i]
    x4=a1[0]*a1[1]*a1[3]*a1[4]
    x1=max(x2,x3,x4)
print(x1)