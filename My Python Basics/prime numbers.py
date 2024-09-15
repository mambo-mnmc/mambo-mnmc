
def prime_numbers(number):
    status = True
    if number < 2:
        status = False
    else:
        for i in range (2, number):
            if number % i == 0:
                status = False
    return status

start = 2
limit = int(input("enter the limit: "))
for number in range (start, limit + 1, 1):
    if prime_numbers(number):
        if number==limit-start:
            print (number)
        else:
            print (number)
        
