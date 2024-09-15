import os
#define a funtion t calculate the fuctorial of a number
while True: #loop will request the user to continue or not.
    def factorial(N):
        fact=1
        for i in range(1, N+1):
            fact *=i
            return fact
    
    def factorial(P):
        factor=1
        for j in range(1, P+1):
            factor *=j
            return factor
    

    N=int(input("Please enter your first Integer, n!:"))
    P=int(input("Please enter your first Integer, p!:"))
    print(factorial(N))
    print(factorial(P))
    
    if input("do you want to continue?(Yes/No)").upper() == "NO": 
        break
    
os.system("pause")
