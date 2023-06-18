x1=int(input());y1=65
for i in range(1,x1+1):
    for j in range(1,i+1):
        print(chr(y1),end="")
        y1+=1
        if y1==91:
            y1-=26
    print()