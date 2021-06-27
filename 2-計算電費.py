aa=float(input("輸入當期電費:"))
s=0
ns=0
if(aa<=120):
    s=aa*2.10
    ns=aa*2.10
    print("Summer months:"+str(round(s,2)))
    print("Not Summer months:"+str(round(ns,2)))
elif(aa<=330):
    s=(120*2.10)+((aa-120)*3.02)
    ns=(120*2.10)+((aa-120)*2.68)
    print("Summer months:"+str(round(s,2)))
    print("Not Summer months:"+str(round(ns,2)))
elif(aa<=500):
    s=(120*2.10)+((330-120)*3.02)+((aa-330)*4.39)
    ns=(120*2.10)+((330-120)*2.68)+((aa-330)*3.61)
    print("Summer months:"+str(round(s,2)))
    print("Not Summer months:"+str(round(ns,2)))
elif(aa<=700):
    s=(120*2.10)+((330-120)*3.02)+((500-330)*4.39)+((aa-500)*4.97)
    ns=(120*2.10)+((330-120)*2.68)+((500-330)*3.61)+((aa-500)*401)
    print("Summer months:"+str(round(s,2)))
    print("Not Summer months:"+str(round(ns,2)))
elif(aa>700):
    s=(120*2.10)+((330-120)*3.02)+((500-330)*4.39)+((700-500)*4.97)+((aa-700)*5.63)
    ns=(120*2.10)+((330-120)*2.68)+((500-330)*3.61)+((700-500)*401)+((aa-700)*4.50)
    print("Summer months:"+str(round(s,2)))
    print("Not Summer months:"+str(round(ns,2)))