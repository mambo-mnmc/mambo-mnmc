import os
while True:
    import calendar
    calendar.setfirstweekday(6)
    curyear=int(input("Please enter year: "))
    print(calendar.month(curyear, 2))
    if input("do you want to continue?(Yes/No)").upper() == "NO":
        break
os.system("pause")
