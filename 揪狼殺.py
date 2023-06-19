time1 = {} #儲存每個時間點的人數
for w in range(24): #建立每個時間點的字典
    time1[str(w)] = []
#print(time1)
for i in range(int(input())): 
    in1 = input().split()   #輸入資料
    #print(in1)
    for j in range(len(in1)):
        time1[in1[j]] += [i] #存入字典

list2  = []
for k in time1: #印出每小時有多少人
    list2.append([k,len(time1[k])])
#print(list2)

#找到連續時間最多的時間
list1 = []
for m in range(24):#計算連續時間
    x = 0
    for n in range(m,24):
        if len(time1[str(n)]) >= 12:
            x += 1
        else:
            break
    list1.append([m,x])
#print(list1)
b = 0
for x in range(24):
    if list1[x][1] == 0:
        b += 1
if b == 24 :
    list2 = sorted(list2,key=lambda x:x[1],reverse=True)
    print(list2[0][0])
else:
    list1 = sorted(list1,key=lambda x:x[0])
    list1 = sorted(list1,key=lambda x:x[1],reverse=True)
    print(list1[0][0])