a=list(eval(input("輸入月租費型式及通話時間為:")))
s=int(a[0])#月租費型式
t=int(a[1])#通話時間(秒)
m=0

if s==186:#$186
    if t*0.09<=s:
        print("通話費為:186")
    elif t*0.09>s:
        if t*0.09/s<=1:
            m=t*0.09*0.9
            print("通話費為:"+str(round(m)))
        else:
            m=t*0.09*0.8
            print("通話費為:"+str(round(m)))

elif s==386:#$386
    if t*0.08<=s:
        print("通話費為:386")
    elif t*0.08>s:
        if t*0.08/s<=1:
            m=t*0.08*0.8
            print("通話費為:"+str(round(m)))
        else:
            m=t*0.08*0.7
            print("通話費為:"+str(round(m)))

elif s==586:#$586
    if t*0.07<=s:
        print("通話費為:586")
    elif t*0.07>s:
        if t*0.07/s<=1:
            m=t*0.07*0.7
            print("通話費為:"+str(round(m)))
        else:
            m=t*0.07*0.6
            print("通話費為:"+str(round(m)))

elif s==986:#$986
    if t*0.06<=s:
        print("通話費為:986")
    elif t*0.06>s:
        if t*0.06/s<=1:
            m=t*0.06*0.6
            print("通話費為:"+str(round(m,0)))
        else:
            m=t*0.06*0.5
            print("通話費為:"+str(round(m,0)))