a=""
b=""

while a!="end":
    s=0
    a=input("檢測的字串(end結束:)")
    if a!="end":
        b=input("檢測的單一字元:")
        for i in range(len(a)):
            if b==a[i]:
                s+=1
        print("字元"+b+"出現的次數為:"+str(s))
    else:
        break
