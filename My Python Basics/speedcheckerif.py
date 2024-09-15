def dscheck(speed,Llim,Mlim,Dp):
    points=0
    x=speed-Llim
    point=x/Dp
    if speed <= Llim:
        result = "Congratulations no point deducted "
    else:
        if speed<=Mlim:
            result="Attention, you are above limit ",str(point)," is deducted "
        else:
            result=" Licence suspended "

    result=result,"you are driving at", str(speed), "km/h, <>"
    print(result)

S = int(input("enter driver speed: "))
L = int(input("enter the low limit: "))
M = int(input("enter max limit: "))
D = int(input("enter demerit point interval: "))
dscheck(S,L,M,D)
