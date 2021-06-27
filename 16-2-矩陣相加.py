t=[]
t1=[]
sum=0

a=input("為啥矩陣:").split()#第一個矩陣
for i in range(int(a[0])):
    b=input("第"+str(i+1)+"列:").split()
    t.append(b)

a1=input("為啥矩陣:").split()#第二個矩陣
for i in range(int(a1[0])):
    b1=input("第"+str(i+1)+"列:").split()
    t1.append(b1)

if a==a1:
    for i in range(len(t)):#矩陣相加
        for j in range(int(a[1])):
            sum=int(t[i][j])+int(t1[i][j])
            print(sum,end=" ")
        print()
else:
    print("兩個矩陣無法相加")
