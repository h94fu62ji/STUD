inv1 = list(input())
inv2 = inv1[::-1]
dict1 = {}
dict1["A"] = int(input())
dict1["B"] = int(input())
for i in inv1:
    if dict1[i] > 0 and inv2[-1] == i:
        dict1[i] -= 1
        inv2.pop(-1)
print(dict1["A"]+dict1["B"])