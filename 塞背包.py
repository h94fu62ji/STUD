in1 = int(input())
in2 = int(input())
cpup = []

for i in range(in2):
    in3 = input(). split()
    if int(in3[2]) <= in1:
        cpup.append([in3[0], in3[2], round(int(in3[1]) / int(in3[2]),2)])
new_cpup = sorted(cpup, key=lambda k:(k[1]))
new_cpup = sorted(new_cpup, key=lambda k:(k[2]), reverse=True)

for j in new_cpup:
    if int(j[1]) < in1:
        in1 -= int(j[1])
        print(j[0])