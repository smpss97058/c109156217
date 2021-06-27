a=list(eval(input("輸入值為:")))
max=min=""

a.sort()#取最小值
for i in range(len(a)):
    min=min+str(a[i])


a.reverse()#取最大值
for i in range(len(a)):
    max=max+str(a[i])

print(int(max)-int(min))#相減