import os
while True:
    n1=int(input("Please enter your first Integer, n1:"))
    n2=int(input("Please enter your second Integer, n2:"))
    l=range(n1+1, n2)
    Sumoint=sum(l)
    print("The sum of your integers is: ", Sumoint)
    if input("do you want to continue?(Yes/No)").upper() == "NO":
        break
os.system("pause")
