win=open("中獎號碼.txt").read().split()
mine=open("我的發票.txt").read().split()
a=0;b=0;x=1;y=0;z=[5,4,3,2,1,0]
D={1:"200",2:"1,000",3:"4,000",4:"10,000",5:"40,000",6:"200,000"}
for i in mine:
    for j in win:
        a=0
        for k in z:
            if i[k:8] == j[k:8]:                
                a+=1
        if a != 0 and a in D.keys():
            print(f"恭喜你，第{x}張中獎{D.get(a)}元")
            y+=int(D.get(a).replace(",",""))
            b+=1
    x+=1
print(f"中獎發票共{b}張，中獎總額共{y}元")