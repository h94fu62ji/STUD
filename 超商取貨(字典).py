#https://judge.ccclub.io/contest/181/problem/02
ShopValue = {}
while True:
    inp1 = input() .split(",")
    if inp1 == ["end"]:
        break
    else:
        ShopValue[inp1[0][-3:]+" "+inp1[1]] = inp1[2]
print(ShopValue)
while True:
    try:
        print(ShopValue .get(input(),"Check again!"))
    except:
        break