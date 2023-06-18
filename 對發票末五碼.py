win=open("中獎號碼.txt").read().split()
mine=open("我的發票.txt").read().split()
x=0;y=0
for i in mine:
    for j in win:
        if i[2:5] == j[2:5]:
            if i [1:5] == j [1:5]:
                if i == j :
                    print(f'恭喜你，第{x}張中獎4000元，號碼是末五碼{i}')
                    y+=4000
                else:
                    print(f'恭喜你，第{x}張中獎1000元，號碼是末四碼{i[1:5]}')
                    y+=1000
            else:
                print(f'恭喜你，第{x}張中獎200元，號碼是末三碼{i[2:5]}')
                y+=200
            x+=1
        else:
            x+=1
print(f"中獎總額{y}元")