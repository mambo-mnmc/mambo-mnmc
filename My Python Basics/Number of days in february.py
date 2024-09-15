import os
while True:
    import calendar
    curyear=int(input("Please enter year: "))
    curmonth= 2
    print(calendar.month(curyear, curmonth))
    if input("do you want to continue?(Yes/No)").upper() == "NO":
        break
os.system("pause")
