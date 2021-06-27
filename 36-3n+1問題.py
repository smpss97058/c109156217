n=int(input("整數n:"))
a=0
print("數列:"+str(n),end=" ")

while n<0 or n>1000000:
    n=int(input("整數n(0<n<1,000,000):"))

while n!=1:
    if n%2!=0:
        n=n*3+1
    else:
        n=n/2
    a+=1
    print(int(n),end=" ")

print()
print("cycle-length:"+str(a+1))