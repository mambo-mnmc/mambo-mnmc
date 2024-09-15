def sumofm():
    m=5
    x=3
    sum_m = 0
    for n in range(0+2, limit):
        if n % m == 0 or n % x == 0:
            sum_m += n
    print("the sum of multiples of, m and x is,", sum_m)
    return
limit = int(input("enter your limit: "))
sumofm()
            
