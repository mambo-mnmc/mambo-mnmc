def Fizz_Buzz():
    ans = "Y"
    while ans == "Y":
        number=int(input("enter the number: "))
        if number % 3 == 0 and number % 5 == 0:
            result = "fizzbuzz"
            print(result)
        elif number % 3 == 0:
            result = "fizz"
            print(result)
        elif number % 5 == 0:
            result = "buzz"
            print(result)
        else:
            print(number)
        ans=input("confirm you want to proceed (Y or N): ")
   
    return

Fizz_Buzz()
