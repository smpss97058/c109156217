a=input("請輸入正整數:")
b=len(a)
c=t=0

for i in range(b,0,-1):
    for j in range(i):
        r=0
        c=int(a[j:i])
        for k in range(2,c):
            if c%k==0:
                r+=1
        if r==0:
            if c>t:
                t=c

if t!=0:
    print("子字串中最大的值數值為:"+str(t))
else:
    print("子字串中最大的值數值為:No prime found")