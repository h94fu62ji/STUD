def BMI計算(身高,體重):
    身高/=100;身高**=2;體重/=身高
    衡量表={18.5:"體重過輕",24:"正常體位",27:"體重過重",30:"輕度肥胖",35:"中度肥胖"}
    for i in 衡量表:
        if 體重<i:
            return(f'你的BMI值為{round(體重,1)},{衡量表.get(i)}')
        elif 體重>=35:
            return(f'你的BMI值為{round(體重,1)},重度肥胖')
print(BMI計算(float(input("請輸入你的身高(公分)\n")),float(input(("請輸入你的體重\n")))))