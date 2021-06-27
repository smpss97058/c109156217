m=[["123","456","789","336","775","566"],["456","789","888","558","666","221"],["9000","5000","6000","10000","12000","7000"]]
a=int(input("輸入查詢組數:"))
b=""

for i in range(a):
    b=input("輸入:").split()
    for j in range(6):
        if b[0]==m[0][i]:
            if b[1]==m[1][i]:
                print(m[2][i])
                break
        else:
            print("error")
            break
    
    
