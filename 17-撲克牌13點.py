a=input("輸入:").split(" ")
print(a)
for i in range(5):
    for i in range(5):
        if a[i]=="A":
            a[i]=1
        elif a[i]=="J":
            a[i]=11
        elif a[i]=="Q":
            a[i]=12
        elif a[i]=="K":
            a[i]=13
        a[i]=int(a[i])
print(sum(a))