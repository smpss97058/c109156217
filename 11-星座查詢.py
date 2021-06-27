D=str(input("輸入月及日為:")).split(" ")
a=D[0]
b=D[1]
c=int(a+b)
if 321<=c<=419:
    print("星座為:牡羊座Aries")
elif 420<=c<=520:
    print("星座為:金牛座Taurus")
elif 521<=c<=621:
    print("星座為:雙子座Gemini")
elif 622<=c<=722:
    print("星座為:巨蟹座Cancer")
elif 723<=c<=822:
    print("星座為:獅子座Leo")
elif 823<=c<=922:
    print("星座為:處女座Virgo")
elif 923<=c<=1023:
    print("星座為:天秤座Libra")
elif 1024<=c<=1121:
    print("星座為:天蠍座Scorpio")
elif 1122<=c<=1220:
    print("星座為:射手座Sagittarius")
elif 1221<=c or c<=120:
    print("星座為:摩羯座Capricorn ")
elif 121<=c<=219:
    print("星座為:水瓶座Aquarius")
else:
    print("星座為:雙魚座")