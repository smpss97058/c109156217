m=int(input("輸入階層M值:"))
n=a=1

while a<=m:
    a*=n
    n+=1
print("超過M的最小階層N值為:"+str(n-1))
