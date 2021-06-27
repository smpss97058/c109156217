n=int(input("輸入一整數:"))
while n<11 or 1000<n:
    n=int(input("輸入一整數(11<=n<=1000):"))
if n%2==0 and n%11==0:
    if n%5!=0 and n%7!=0:
        print(str(n)+"為新公倍數?:Yes")
    else:
        print(str(n)+"為新公倍數?:No")