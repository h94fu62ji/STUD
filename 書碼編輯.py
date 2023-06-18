di1={};x1=[0,0,0,0,0,0,0,0,0,0]
def chh(b1):#整理數字
    for i in range(len(b1)-1,-1,-1):
            if b1[i]>=10:
                b1[i-1]+=b1[i]//10
                b1[i]%=10
    return("".join([str(i) for i in x1])) 
while True:
    in1=input()
    if in1=="0":#輸入0中斷
        break
    for i in range(6):#重製書的前六碼序號
        x1[i]=0
    di2=dict(enumerate(di1))#生成字典位置
    di2={v: k for k, v in di2.items()}#顛倒位置
    if in1 in di1:#如果有 增加一組新的編號
        x1[2]=di2[in1]+1#取得書的順序
        x1[5]=len(di1[in1])+1#取得同本書的順序
        x1[-1]+=1#進館順序
        di1[in1].append(chh(x1))
    elif in1 not in di1:#如果沒有 新增並且給編號
        x1[2]=len(di1)+1#建立書的順序
        x1[5]=1#建立書的第一本
        x1[-1]+=1#進館順序
        di1[in1]=[chh(x1)]
for i in di1:
    print(i," ".join((di1[i])))