x=int(input("X軸座標:"))
y=int(input("Y軸座標:"))
a=0

if x>0:
    if y>0:
        a=x**2+y**2
        print("該點位於第一象限,離原點距離為根號"+str(a))
    elif y<0:
        a=x**2+y**2
        print("該點位於第四象限,離原點距離為根號"+str(a))
    else:
        a=x**2+y**2
        print("該點位於X軸上,離原點距離為根號"+str(a))
if x<0:
    if y>0:
        a=x**2+y**2
        print("該點位於第二象限,離原點距離為根號"+str(a))
    elif y<0:
        a=x**2+y**2
        print("該點位於第三象限,離原點距離為根號"+str(a))
    else:
        a=x**2+y**2
        print("該點位於X軸上,離原點距離為根號"+str(a))
if x==0:
    if y==0:
        print("該點位於原點")
    else:
        a=x**2+y**2
        print("該點位於Y軸上,離原點距離為根號"+str(a))
