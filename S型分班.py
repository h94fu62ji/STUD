in1 = input().split()
in2 = input().split()
value_d = {}
x = 0
y = len (in1)
for i in range(len(in1)):
    if in2[i] not in value_d:
        value_d[in2[i]] = []
    value_d[in2[i]].append(in1[i])
#print(value_d)

value1 = sorted(list(set(in2)))
value2 = sorted(value1,reverse=True)

while y != 0:
    if x == 0:
        for i in value1:
            if len(value_d[i]) >= 1:
                print(value_d[i][0],end=" ")
                y-=1
                del value_d[i][0]
        x = 1
    
    elif x == 1:
        for i in value2:
            if len(value_d[i]) >= 1:
                print(value_d[i][0],end=" ")
                y-=1
                del value_d[i][0]
        x = 0