t=input("輸入一組四位數字為:")
a=(int(t[0])+7)%10
b=(int(t[1])+7)%10
c=(int(t[2])+7)%10
d=(int(t[3])+7)%10

print("輸出加密後的數字為:"+str(c)+str(d)+str(a)+str(b))
