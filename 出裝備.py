d2 = {}

for i in range(int(input())):
    l1=input().split(" ")
    d2[l1[0]]=l1[1:]

#print(d2)

#{'長劍': ['350'], '抗魔斗篷': ['450'], '吸魔劍': ['600', '長劍', '抗魔斗篷']}

def all (x):
    x1 = 0
    if len(d2[x]) >= 2:
        for i in range(1,len(d2[x])):
            x1 += all(d2[x][i])
            #print(d2[x][i])
        x1 += int("".join(d2[x][0]))
        return(x1)
    else :
        x1 += int("".join(d2[x][0]))
        return(x1)

for i in range(int(input())):
    print(all(input()))