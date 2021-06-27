a=list(input("輸入一字元為:"))
b=[]

for i in range(len(a)-1,-1,-1):
    b.append(a[i])

if a==b:
    print("Yes")
else:
    print("No")