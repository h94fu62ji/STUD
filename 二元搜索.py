in1 = input().split()
in2 = input().split()
in3 = input()
# if in3 not in in1:
#         print("not found")
# else:
#     for i,j in zip(in1,in2):
#         if i == in3:
#             print(j)



def min(in1,in3):
    sta = 0
    end = len(in1) - 1
    while sta <= end:
        min = (sta + end) // 2
        if in1[min] == in3:
            return min
        elif in1[min] > in3:
            end = min - 1
        else :
            sta = min + 1
    return "no"
x = min(in1,in3)
if x == "no":
    print("not found")
else:
    print(in2[x])