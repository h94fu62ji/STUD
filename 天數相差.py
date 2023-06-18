import datetime as dt
yy,mm,dd = [int(i) for i in input().split()]
y2,m2,d2 = [int(i) for i in input().split()]
x=dt.date(yy,mm,dd) - dt.date(y2,m2,d2)
print(abs(int(str(x).split()[0])))