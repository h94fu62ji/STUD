import re
filename1 = input()

list1 = []
dict2 = {}

while True:
    in1 = input().split("\t")
    if "label" in in1[0]:
        list1.append([in1[0],in1[1]])
    else:
        break

while True:
    try:
        in2 = input()
        in3 = re.sub(r"[^a-zA-Z0-9\s]","",in2).lower()
        print(in3)
        dict2[in3] = in2
    except:
        break

for i in list1:
    if i[1] in dict2:
        i[1] = dict2.get(i[1])
        print("\t".join(i))
    else :
        print("\t".join(i))