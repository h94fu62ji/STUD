a1=[int(i) for i in input().split(":")]#入場時間
a2=[int(i) for i in input().split(":")]#離場時間
a3=input()#是否有優惠券(Y/N)
x1=(a2[0]*60+a2[1])-(a1[0]*60+a1[1])#計算總時間(分鐘)
x2=x1//30#算錢次數
if x1%30!=0:
    x2+=1
if x1 == 0 :
    print(0)
elif a3 == "Y" and x1 < 30:
    print(0)
elif a3 == "Y":
    print(x2*10)
else:
    print(x2*20)