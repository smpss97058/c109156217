total=[]
subject=["國文","英文","微積分","體育","程式設計"]
average=0
max1=0
min1=100

for i in range(5):
    a=int(input(subject[i]+":"))
    while a<0 or a>100:
        a=int(input(subject[i]+"成績成績輸入錯誤,請重新輸入(0<=成績<=100):"))
    total.append(int(a))

average=sum(total)/5#平均
print("平均分數:"+str("%.2f"%average))

for i in range(5):
    if total[i]>=max1:#最大
        max1=total[i]
        t=i
    if total[i]<=min1:#最小
        min1=total[i]
        t1=i
max2=subject[t]
min2=subject[t1]
print("最高科目分數:"+max2+str(max1)+"分")
print("最低科目分數:"+min2+str(min1)+"分")

