inv1 = int(input())/100 #輸入相似度的值
data1 = {}

while True: #多重輸入 並以end為結束條件
    inv2 = input().split()
    if inv2 == ["end"]:
        break
    data1[inv2[0]] = inv2[1:]

for i in data1:
    data2 = {} #輸出用資料
    data2[i] = []
    for j in data1: 
        x = 0
        for k in data1[i]:

            if k in data1[j]:
                x += 1

        if x / len(data1[i]) >= inv1:
            data2[i] += data1[j]  

    data3 = list(set(data2[i]))
    data3.sort(key = data2[i].index)
    for s in data1[i]:
        data3.remove(s)
    print(i,end="")
    if len(data3) > 0:
        print(""," ".join(data3),end = "")
    print("")