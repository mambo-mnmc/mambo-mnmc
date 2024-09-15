def shownumbers():
    limit = int(input("enter the limit"))
    for i in range(limit):
        if i % 2 == 0:
            print(i, "even")
        elif i % 2:
            print(i, "odd")
    return

shownumbers()
    
