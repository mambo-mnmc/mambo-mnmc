def classifyNumbers(limit):
    for i in range(0, limit):
        if i in range(2,limit,2):
            print(i, "even")
        elif i in range(1,limit,2+1):
            print(i, "odd")
    return
limit=int(input("enter the limit number"))
classifyNumbers(limit)
    
