import os
while True:
    Height=float(input("Enter the Height of your rectangle"))
    Length=float(input("Enter the Length of your rectangle"))
    Perimeter=(Height+Length)*2
    Perimeter=float(Perimeter)
    Area=Length*Height
    Area=float(Area)
    print("The Peremeter is", Perimeter)
    print("The Area is", Area)
    if input("do you want to continue?(Yes/No)").upper() == "NO":
        break
os.system("pause")
