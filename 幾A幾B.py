x1=0
x2=0

inp1=str(input())
inp11=inp1
inp2=str(input())

for i in range(len(inp1)):
    #print(inp1[i],inp2[i])
    if inp1[i] == inp2[i]:
        x1+=1

    if inp2[i] in inp11 :
        x2+=1
        inp11 = inp11.replace(inp2[i],"",1)

print(f"{x1}A{x2-x1}B")