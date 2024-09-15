def calculate ():
    """This is my document string for my first statement"""
    ans = "Y"
    while ans == "Y":
        ans=input("confirm you want to proceed (Y or N): ")
        if ans == "Y":
            next="Yes"
            while next == "Yes":
                next=input("do you want to add two numbers? Yes or No : ")
                if next == "Yes":
                    a=int(input("Enter A: "))
                    b=int(input("Enter B: "))
                    total = a+b
                    print("your sum is, " ,total)
                    break
            more="Yes"
            while more == "Yes":
                more=input("do you want to calculate more? Yes or No : ")
                 if next == "Yes":
                     
        elif ans != "":
            print("am sorry i cannot help you further")
            input("press enter to continue")        
    return

calculate()
