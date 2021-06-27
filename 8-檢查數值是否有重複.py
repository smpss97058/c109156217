n=int(input("輸入第一行正整數為:"))
a=input("第二行中數列中的數字為:").split(" ")
t=0
s=""

for i in a:
    b=0
    for j in a:
        if i==j:
            b+=1
            if b>t:
                t=b
                s=i

if t!=1:
    print("最大出現次數的數字為:"+str(s))
    print("出現次數為:"+str(t))
else:
    print("每個數字剛好只出現1次")


