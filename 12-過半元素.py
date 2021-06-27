a=input("輸入一整數數列為:").split(" ")

for i in a:
    b=0
    for j in a:
        if i==j:
            b+=1
    if b>=len(a)/2:
        print("過半元素為:"+str(i))
        break
    else:
        b=0
if b==0:
    print("過半元素為:no")

