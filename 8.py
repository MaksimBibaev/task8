try:
    ch=int(input("Введите число"))
    ss=int(input("Введите целевую систему счисления"))
except ValueError:
    print("Ошибка")
else:
    def p():
        res=""
        ssf=ss
        chf=ch
        while chf>0:
            res=str(chf%ssf)+res
            chf//=ssf
        print(res)
    if ss==2 or ss==8:
        if ss==2:
            p()
        else:
            p()
    else:
        print("Доступны только 2 и 8 сс")
        
