#https://judge.ccclub.io/contest/181/problem/01
d1={};l1=[]
for i in range(int(input())):#輸入抓資料的次數
    x1=(input().split())#抓區域人數資料
    d1[x1[0]]=x1[1]
#print(d1)
x2= input().split()#給出特定區域
for j in x2:#找出特定區域的值
    if j in d1:
        l1.append(j)
#print(l1)
def DD (x):
    return(int(d1.get(x)))
l1=sorted(l1,key=DD)
#print(l1)
for k in range(int(input())):#推薦區域的數量
    print(l1[k],end=" ")#輸出
