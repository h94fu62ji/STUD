stock = {} #庫存字典
in_stock_times = int(input())
in_stock = input().split()

cooking = {} #菜單字典
cooking_list = [] #菜單串列
in_cooking_times = int(input())


for i in range(0,in_stock_times*2,2): #新增庫存
    stock[in_stock[i]] = int(in_stock[i+1])


for j in range(in_cooking_times): #新增菜單所需食材
    in_cooking = input().split()
    cooking_list .append(in_cooking[0])
    cooking[in_cooking[0]] = []
    for k in range(1,len(in_cooking),2): 
        cooking[in_cooking[0]].append([in_cooking[k],int(in_cooking[k+1])])

in_oder = int(input()) #詢問次數

for i in range(in_oder): #詢問次數
    in_menu = input()
    x=1
    for j in range(len(cooking[in_menu])): #查詢剩餘材料
        stock_v = stock.get(cooking[in_menu][j][0],False)
        if stock_v == False:
            x = 0
            print(False)
            break
        elif stock_v < int(cooking[in_menu][j][1]):
            x = 0
            print(False)
            break
    if x == 1: #材料足夠就會扣除
        for k in range(len(cooking[in_menu])):
            stock[cooking[in_menu][k][0]] = stock.get(cooking[in_menu][k][0]) - cooking[in_menu][k][1]
        print(True)




# stock[in_menu] = stock.get(in_menu) - 1 #食材減少
# print(stock[in_menu])