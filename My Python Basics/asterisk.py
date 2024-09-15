rows = int(input("enter the number of rows"))

for i in range(0, rows):
    for a in range(0, i+1):
        print("*", end = ' ')

    print("\r")
