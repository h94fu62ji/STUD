
dict1 = {}
for i in range(4):
    in1 = input().split()
    dict1[in1[0]] = in1[1:]
print(dict1)
in2 = input()#要學習的課程

# dict1 = {'a': ['b', 'c'], 'b': ['e'], 'c': ['d'], 'f': []}
# in2 = 'a'
def clse (x):
    if len(dict1.get(x,"")) == 0:
        return [x]
    else:
        list1 = [x]
        for i in dict1.get(x):
            list1.append(clse(i))
        return list1
x1 = clse(in2)

