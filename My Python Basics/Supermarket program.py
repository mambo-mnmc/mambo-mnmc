import os
while True:
    print("Rusangu Supermarket Program")

    Quabght=int(input("The units of quantity bought are  "))
    Quasld=int(input("How many did you sale?  "))
    pp=float(input("what is the purchase price "))
    sp=float(input("what is the selling price "))
    strem=Quabght-Quasld
    strem=int(strem)
    tsqt=Quasld
    tsqt=int(tsqt)
    tsval=Quasld*sp
    tsval=float(tsval)
    tpval=Quabght*pp
    tpval=float(tpval)
    rval=tpval-tsval
    rval=float(rval)
    if rval>0:
        rtype=("benefit")
        rtype=str(rtype)
    elif rval<0:
        rtype=("loss")
    else:
        rtype=("null")
    print("stock remaining ", strem)
    print("total sale in quantity", tsqt)
    print("total sale in value", tsval)
    print("total purchase in value", tpval)
    print("result in valu", rval)
    print("result in type", rtype)
    if input("do you want to continue?(Yes/No)").upper() == "NO":
        break
os.system("pause")
