mout = {}
for i in range(int(input())):   #輸入路線數量
    hight = 0 #紀錄山的高度
    lt = 3 #涼亭次數
    chs = 3 #廁所次數
    fall = 1
    for _ in range(int(input())):   #輸入路線據點
        in1 = input().split(",")
        hight += int(in1[0])
        if in1[1] == "True":
            lt = 3
        else :
            lt -= 1
        if in1[2] == "True":
            chs = 3
        else :
            chs -= 1
        if lt == 0 or chs == 0:
            fall = 0
    mout[i] = [fall,hight] #編號,廁所、涼亭區間達成,高度
#print(mout)
mout_all = 0 #預設值
mout1 = []

for i in mout: #確認所有的路程是否都不行
    if mout[i][0] != 0:
        mout_all = 1
    mout1.append([i,mout[i][1]])

mout1 = sorted(mout1,key=lambda x:x[1],reverse=True)
if mout_all == 0: #打印結果
    print("stay at home")
else:
    print(mout1[0][0])




