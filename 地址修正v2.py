import csv
with open("地址資料.csv") as infile:
    data=list(csv.DictReader(infile))
    for i in data:
        print(f'原始資料:{i["姓名"]}{i["縣市"]}{i["住址"]}')
        if "台" in i["縣市"]:
            i["縣市"]=i["縣市"].replace("台","臺")
        if "F" in i["住址"]:
            i["住址"]=i["住址"].replace("F","樓")
        if i["縣市"]=="臺中市" and "中港路" in i["住址"]:
            i["住址"]=i["住址"].replace("中港路","臺灣大道")
        print(f"更新資料:{i['姓名']}{i['縣市']}{i['住址']}")
"""print(data[0].keys())"""
with open("新地址資料.csv","w",newline="") as newfile:
    x=csv.DictWriter(newfile,fieldnames=data[0].keys())
    x.writeheader()
    for e in data:
        print(e)
        x.writerow(e)

    