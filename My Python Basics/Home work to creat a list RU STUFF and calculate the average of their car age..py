RU_STUFF=[]
st = {"Owner":"Mr Kapenya","Color":"white","Brand":"IPSUM","Myear":2008}
sd = {"Owner":"Mr Masivi","Color":"black","Brand":"NOTSURE","Myear":2012}
rd = {"Owner":"Mrs Simate","Color":"Grey","Brand":"TOYATA","Myear":2008}
RU_STUFF.append(dict(st ))
RU_STUFF.append(dict(sd ))
RU_STUFF.append(dict(rd ))
print(RU_STUFF)
sumint=0
for i in RU_STUFF:
    Cyear=int(input("Enter the Current year: "))
    Myear=int(input("Enter the Manufacturing year: "))
age=Cyear-Myear
sumint+=i
Average = sumint/len(age)
print("The Average of the car's age is",Average)
    
    
    
