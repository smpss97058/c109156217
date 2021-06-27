a=int(input("組數為:"))
b=[]

for i in range(a):
    c=0
    b=input("第"+str(i+1)+"組(全 半):").split()
    c=int(b[0])*250+int(b[1])*175
    print("第"+str(i+1)+"組應收費用:"+str(c))
